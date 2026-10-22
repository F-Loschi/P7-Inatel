# Resumo — Cassandra + Redis com Python

---

# 🐍 PYTHON — conceitos usados o tempo todo

### `self.` dentro de classes (DAOs)
Quando a conexão está guardada como atributo da classe, **sempre** usa `self.`:
```python
class AlunoDAO:
    def __init__(self):
        self.cassandra_session = CassandraDBConnector.get_session()
        self.redis_connection = RedisDBConnector.get_connection()

    def metodo(self):
        self.redis_connection.hset(...)   # não dá pra usar "redis_conn" direto
        self.cassandra_session.execute(...)
```

### dict vs objeto — como acessar campos
```python
dado_dict = {"id": 1, "nome": "Ana"}
dado_dict["nome"]          # dict usa colchetes

dado_objeto = Aluno(id=1, nome="Ana")
dado_objeto.nome           # objeto usa ponto
```
⚠️ Erro recorrente: tentar `objeto["campo"]` ou `dict.campo` — sempre checar qual tipo a função está recebendo antes de acessar.

### `f-strings` para montar chaves
```python
f"aluno:{aluno.id}"           # objeto
f"aluno:{aluno['id']}"        # dict
f"aluno:{aluno_id}:areas"     # chave "filha"/relacionada
```

### List comprehension com filtro
```python
[p for p in lista if condicao]
# Ex: filtrar chaves que NÃO terminam com "tags"
[p for p in redis_conn.keys("post:*") if not p.endswith("tags")]
```

### `sorted()` com chave customizada e desempate
```python
sorted(lista, key=lambda x: x["campo"])                       # ordena por 1 campo
sorted(lista, key=lambda x: x["campo"], reverse=True)          # DESC
sorted(lista.items(), key=lambda x: (-x[1], x[0]))             # desempate: 1º critério, depois 2º
```

### `.split()` e `.join()` — string ↔ lista
```python
"a, b, c".split(", ")           # → ["a", "b", "c"]
"post:345".split(":")[1]        # → "345"  (extrair id de uma chave composta)
```

### `import json` — não precisa instalar, já vem no Python
```python
import json
json.dumps(dict_objeto)   # dict → string (pra GUARDAR em algo que só aceita string, como Redis)
json.loads(string_json)   # string → dict (pra LER de volta)
```
| Função | Trabalha com | Quando usar |
|---|---|---|
| `json.dump()` / `json.load()` | arquivo | salvar/ler de um `.json` no disco |
| `json.dumps()` / `json.loads()` | string | **é o que usamos com Redis** (Redis só guarda strings) |

### `datetime` — extrair partes de uma data/hora
```python
from datetime import datetime
agora = datetime.now()

agora.day            # dia (int)
agora.month          # mês (int)
agora.year           # ano (int)
agora.strftime("%H:%M")   # formata como string "HH:MM"
```

### Converter tipos (`float`, `int`, `round`)
```python
float("199.90")          # string → float
round(349.79998, 2)      # arredonda pra 2 casas decimais
round(float(valor), 2)   # combo comum: converte E arredonda
```
⚠️ Erro recorrente: somar/comparar valores que vêm como **string** sem converter antes (`"199.90" + "149.90"` concatena texto, não soma número).

---

# 🟦 CASSANDRA (cassandra-driver)

## Conceito chave: como pensar o modelo de dados

Diferente do Mongo/Neo4j, no Cassandra **você modela a tabela pensando em como vai consultar os dados**, não no formato "natural" da entidade. A pergunta sempre é: *"que filtros eu vou usar nessa tabela?"* — e a resposta vira a `PRIMARY KEY`.

```
PRIMARY KEY ((partition_key1, partition_key2), clustering_key1, clustering_key2)
              └────── agrupa os dados juntos ──────┘  └── ordena dentro do grupo ──┘
```

- **Partition Key** (dentro do primeiro parênteses): define em qual "partição"/grupo físico os dados ficam. Pra fazer um `WHERE` eficiente, você **precisa** filtrar pela partition key completa.
- **Clustering Key** (depois): ordena os registros dentro da mesma partição, e complementa a identificação (evita duplicar a partition key).

**Exemplos do que vimos:**
```sql
-- Alunos agrupados por país+cidade, ordenados/identificados por id
PRIMARY KEY((pais, cidade), id)

-- Cursos agrupados por categoria, identificados por id
PRIMARY KEY((categoria), id)

-- Matrículas agrupadas por dia+mes+ano, ordenadas por hora e id
PRIMARY KEY((dia, mes, ano), hora, id)
```

---

## Conexão

```python
from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
from cassandra.query import dict_factory

# Local
cluster = Cluster(['localhost'], port=9042)
session = cluster.connect()
session.row_factory = dict_factory   # <- IMPORTANTE: faz cada linha vir como dict
session.set_keyspace("nome_keyspace")

# Cloud (Astra) - usa secure connect bundle
import os
cloud_config = {"secure_connect_bundle": os.path.join(os.path.dirname(__file__), "arquivo.zip")}
auth_provider = PlainTextAuthProvider("client_id", "client_secret")
cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
session = cluster.connect()
```

⚠️ **Erro que caímos:** `secure_connect_bundle` com caminho relativo falha se o pytest rodar de outra pasta. Usar `os.path.join(os.path.dirname(__file__), "arquivo.zip")` resolve, OU rodar o pytest sempre de dentro da pasta correta do arquivo.

⚠️ **Criar keyspace** (se for local, não cloud):
```python
session.execute("""
    CREATE KEYSPACE IF NOT EXISTS nome_keyspace
    WITH replication = { 'class': 'SimpleStrategy', 'replication_factor': '1' }
""")
```

---

## Criar tabela (CQL)

```python
query = """
    CREATE TABLE alunos(
        id INT,
        pais TEXT,
        cidade TEXT,
        endereco TEXT,
        nome TEXT,
        email TEXT,
        areas_estudo LIST<TEXT>,
        PRIMARY KEY((pais, cidade), id)
    );
"""
session.execute(query)
```

### Tipos importantes
| Tipo CQL | Equivalente Python |
|---|---|
| `TEXT` | str |
| `INT` | int |
| `FLOAT` | float (⚠️ ver aviso abaixo) |
| `DECIMAL` | precisão exata — preferir pra dinheiro |
| `BOOLEAN` | bool |
| `LIST<TEXT>` | list |
| `MAP<INT, INT>` | dict |
| `LIST<MAP<INT,INT>>` | precisa de `FROZEN` (ver abaixo) |
| `UUID` | identificador único (não usamos, mas pode cair) |

⚠️ **Erro que caímos: `FLOAT` perde precisão.** `199.90` virava `199.9` ou pior. Pra valores monetários, usar `DECIMAL` em vez de `FLOAT`, e mesmo assim aplicar `round(float(valor), 2)` no Python ao recuperar, por segurança.

⚠️ **Erro que caímos: coleção dentro de coleção precisa de `FROZEN`.**
```sql
-- ERRO: non-frozen collections are only supported at top-level
cursos_quantidade LIST<MAP<INT, INT>>

-- CORRETO:
cursos_quantidade LIST<FROZEN<MAP<INT, INT>>>
```
Regra geral: sempre que tiver uma coleção (list/map/set) **dentro** de outra coleção, a de dentro precisa ser `FROZEN`.

### Apagar/checar tabela
```sql
DROP TABLE IF EXISTS nome_tabela;
```

---

## Update e Delete

```sql
-- Update: parecido com insert, mas com WHERE pela chave primária completa
UPDATE alunos SET nome = ? WHERE pais = ? AND cidade = ? AND id = ?;

-- Delete
DELETE FROM alunos WHERE pais = ? AND cidade = ? AND id = ?;
```
No Cassandra, `INSERT` com a mesma chave primária **sobrescreve** o registro — então muitas vezes nem precisa de `UPDATE` explícito, um novo `INSERT` já resolve.

---

## Insert (sempre com Prepared Statement)

```python
query = "INSERT INTO alunos(id, pais, cidade, endereco, nome, email, areas_estudo) VALUES (?, ?, ?, ?, ?, ?, ?);"
prepared = session.prepare(query)
session.execute(prepared, [aluno.id, aluno.pais, aluno.cidade, aluno.endereco, aluno.nome, aluno.email, aluno.areas_estudo])
```

- `?` é o placeholder (não é `%s` nem `$1`)
- Sempre passar os valores como **lista**, na mesma ordem dos `?`
- O `prepare()` não é obrigatório, mas é boa prática (mais seguro e eficiente)

---

## Select

```python
# Filtro pela partition key completa - não precisa de ALLOW FILTERING
query = "SELECT * FROM cursos WHERE categoria = ?;"

# Filtro por SÓ PARTE da partition key - precisa de ALLOW FILTERING
query = "SELECT * FROM alunos WHERE pais = ? ALLOW FILTERING;"

# Filtro pela partition key + clustering key (sempre permitido, sem ALLOW FILTERING)
query = "SELECT * FROM matricula WHERE dia = ? AND mes = ? AND ano = ?;"

# Selecionar só alguns campos (não precisa pegar tudo com *)
query = "SELECT id, nome, preco FROM curso WHERE categoria = ?;"
```

⚠️ **Erro que caímos:** tentar filtrar só por `pais` quando a partition key é `(pais, cidade)` — dá erro sem o `ALLOW FILTERING`. Regra: se você não está usando a partition key **inteira**, precisa de `ALLOW FILTERING` (em produção isso é evitado por ser lento — faz table scan — mas funciona e é aceito em exercícios).

### Regra geral de quando precisa de `ALLOW FILTERING`
| Situação | Precisa de ALLOW FILTERING? |
|---|---|
| Filtra pela partition key inteira | Não |
| Filtra pela partition key inteira + clustering key | Não |
| Filtra por só parte da partition key | Sim |
| Filtra por um campo que não é chave nenhuma | Sim |

### Funções agregadas
```sql
SELECT COUNT(*) FROM alunos;
SELECT SUM(custo_producao) FROM curso;
SELECT AVG(preco) FROM curso;       -- também existe, mesma lógica
SELECT MIN(preco) FROM curso;
SELECT MAX(preco) FROM curso;
```
Essas só funcionam sem `WHERE` complexo de boa forma quando rodam sobre a tabela toda ou uma partição só — Cassandra não é feito pra agregações pesadas como SQL tradicional.

### Lendo o resultado
```python
resultado = session.execute(prepared, [valor])

# resultado é ITERÁVEL de dicts (por causa do dict_factory)
for linha in resultado:
    print(linha["campo"])

# Pra pegar só a primeira/única linha:
resultado[0]["campo"]
# (gera DeprecationWarning, mas funciona; alternativa: resultado.one()["campo"])
```

⚠️ **Erro que caímos:** confundir `resultado[0]` (primeira linha) com `resultado` (iterável completo). Pra contar/somar (`COUNT`, `SUM`) sempre é `resultado[0][...]` pois retorna **uma linha só**. Pra listar vários registros, itera com `for linha in resultado`.

### Funções agregadas — nome da chave no retorno
```python
"SELECT COUNT(*) FROM alunos;"        → resultado[0]["count"]
"SELECT SUM(custo_producao) FROM curso" → resultado[0]["system.sum(custo_producao)"]
```
⚠️ **Dica:** se não souber o nome exato da chave, dar um `print(resultado[0])` primeiro pra descobrir — o nome muda conforme a função e a versão do driver.

---

## Rodando testes específicos (pytest)

```bash
# Rodar um teste específico
pytest arquivo.py::nome_da_funcao_teste

# Rodar com prints visíveis (sem isso, print() não aparece!)
pytest arquivo.py -s
```
⚠️ **Pegadinha:** se a função de teste **não começar com `test_`** (ex: `teste_questao_1_b`), o pytest **não roda ela automaticamente** na coleção — precisa chamar explicitamente pelo nome.

---

# 🟥 REDIS (redis-py)

## Conexão

```python
import redis

redis_conn = redis.Redis(
    host="localhost",
    port=6379,
    decode_responses=True   # IMPORTANTE: sem isso, tudo volta como bytes (b"texto") em vez de string
)

redis_conn.flushall()    # limpa o banco inteiro - útil pra resetar entre execuções de teste
redis_conn.close()       # fecha a conexão
```

## Conceito chave: Redis só guarda STRINGS (ou coisas feitas de strings)
Toda estrutura do Redis, no fundo, lida com texto. Números, listas, objetos — tudo precisa ser convertido pra string em algum nível. Isso explica por que:
- `Hash` armazena cada campo como string (o redis-py converte número→string sozinho ao salvar, mas ao **ler de volta**, pode vir como string mesmo sendo originalmente número — atenção a isso em comparações/somas)
- Pra guardar uma lista de **dicts**, precisa de `json.dumps()` antes
- IDs usados em chaves (`f"post:{id}"`) viram string automaticamente dentro do f-string

---

## Estruturas — como escolher

| Situação | Estrutura | Comandos |
|---|---|---|
| Objeto com campos nomeados | **Hash** | `hset(mapping=...)` / `hgetall` / `hget(chave, campo)` |
| Coleção ordenada por inserção, com duplicatas | **List** | `rpush` / `lrange(chave, 0, -1)` |
| Coleção sem ordem, sem duplicatas | **Set** | `sadd` / `smembers` / `sismember` |
| Coleção ordenada por número (score) | **Sorted Set** | `zadd({membro: score})` / `zrange(chave, 0, -1, withscores=True)` |
| Valor simples | **String** | `set` / `get` |

### Frases-chave pra identificar qual usar
- "tenho vários campos nomeados de uma coisa" → Hash
- "tenho uma lista de itens variados/dicts" → List (serializando com JSON)
- "preciso checar rapidamente se X está dentro do grupo" → Set (`sismember`)
- "preciso ordenar por um número/score" → Sorted Set
- "esses dados têm um prazo de validade" → qualquer estrutura + `expire()`

---

## Hash — objeto com campos nomeados

```python
redis_conn.hset(f"aluno:{id}", mapping={"nome": "...", "email": "..."})
dados = redis_conn.hgetall(f"aluno:{id}")     # retorna dict completo
valor = redis_conn.hget(f"aluno:{id}", "nome") # retorna só um campo
redis_conn.hdel(f"aluno:{id}", "campo")        # remove um campo do hash
redis_conn.hexists(f"aluno:{id}", "campo")     # True/False - campo existe?
redis_conn.hincrby(f"aluno:{id}", "campo", 1)  # incrementa campo numérico
```
⚠️ **Hash não guarda listas dentro dele.** Se o objeto tem um campo que é lista (ex: `areas_estudo`), salva em uma **List separada** com chave relacionada por convenção: `aluno:{id}:areas`.

⚠️ **Hash não guarda o id automaticamente** — se você não incluir o id no `mapping`, ele não vai estar no `hgetall`. Solução: extrair da própria chave com `.split(":")[1]`, ou incluir manualmente: `doc["id"] = id`.

---

## List — coleção ordenada / sequência de itens

```python
redis_conn.rpush("chave", elemento1, elemento2)  # adiciona no FINAL
redis_conn.lpush("chave", elemento)              # adiciona no INÍCIO
redis_conn.rpush("chave", *lista_python)         # * desempacota a lista
itens = redis_conn.lrange("chave", 0, -1)         # 0 = início, -1 = fim (todos)
redis_conn.llen("chave")                          # tamanho da lista
redis_conn.lindex("chave", 0)                     # pega elemento por índice
```

### Guardando dicts numa List → serializar com JSON
Redis só aceita strings, não dicts. Pra guardar uma lista de objetos complexos:
```python
import json

# Salvar
redis_conn.rpush("chave", json.dumps(dict_objeto))

# Recuperar
itens_string = redis_conn.lrange("chave", 0, -1)
itens_dict = [json.loads(item) for item in itens_string]
```

**`dump/load` vs `dumps/loads`:**
| Função | Trabalha com |
|---|---|
| `json.dump()` / `json.load()` | arquivo |
| `json.dumps()` / `json.loads()` | string (o `s` = *string*) — **é o que usamos com Redis** |

---

## Set — coleção sem ordem/duplicata

```python
redis_conn.sadd("chave", elemento1, elemento2)
redis_conn.smembers("chave")                  # retorna o Set inteiro
redis_conn.sismember("chave", elemento)       # True/False - elemento está no set?
redis_conn.srem("chave", elemento)            # remove elemento
redis_conn.scard("chave")                     # conta quantos elementos tem
redis_conn.sinter("chave1", "chave2")         # interseção entre dois sets
redis_conn.sunion("chave1", "chave2")         # união entre dois sets
```
`sinter` é útil quando você precisaria cruzar dois conjuntos (ex: tags do post ∩ interesses do usuário) sem precisar fazer o loop manual em Python.

---

## Sorted Set (ZSet) — ordenado por score

```python
redis_conn.zadd("chave", {"membro": score})
redis_conn.zrange("chave", 0, -1, withscores=True)
# retorna [(membro, score), ...] já ordenado ASC (crescente) pelo score

redis_conn.zrevrange("chave", 0, -1, withscores=True)  # ordenado DESC (decrescente)
redis_conn.zscore("chave", "membro")                    # pega o score de um membro específico
redis_conn.zrem("chave", "membro")                       # remove um membro
redis_conn.zincrby("chave", incremento, "membro")        # incrementa o score de um membro
```

---

## Keys — descobrir chaves existentes

```python
redis_conn.keys("post:*")   # todas as chaves que começam com "post:"
```
⚠️ **Erro que caímos:** isso traz junto chaves "filhas" tipo `post:345:tags`. Filtrar com list comprehension:
```python
[p for p in redis_conn.keys("post:*") if not p.endswith("tags")]
```

---

## TTL — expiração automática

```python
redis_conn.expire("chave", segundos)
# Ex: 5 horas = 18000 segundos

redis_conn.ttl("chave")        # quantos segundos faltam pra expirar (-1 = sem TTL, -2 = não existe)
redis_conn.persist("chave")    # remove o TTL, torna a chave permanente de novo
```
Usado quando o enunciado fala em "dados recentes", "expirar após X tempo", "remover automaticamente".

---

## Padrão: relacionar chaves por convenção de nome
Como o Redis não tem "relacionamentos" nativos como bancos relacionais ou de grafo, a prática comum é **usar o mesmo prefixo** pra ligar dados relacionados:

```
post:345          → Hash com os dados do post
post:345:tags     → Set com as tags desse mesmo post

aluno:2           → Hash com os dados do aluno
aluno:2:areas     → List com as áreas de estudo desse aluno

desejos:2         → List com a lista de desejos do aluno 2
```

Pra "navegar" dessas relações, normalmente combina-se `keys("prefixo:*")` pra descobrir os IDs existentes, com leituras subsequentes para os dados relacionados.

---

## Erros recorrentes que cometemos (Redis)

1. **Confundir dict com objeto**: dict usa `dado["campo"]`, objeto usa `dado.campo`. Sempre checar o tipo do parâmetro recebido pela função.
2. **Esquecer o `self.` em métodos de classe**: quando a conexão Redis está em `self.redis_connection`, não dá pra usar `redis_conn` direto (isso só existia em scripts soltos).
3. **Inverter a ordem de loops aninhados**: ao calcular "soma de scores que batem com tags", o `score_total` precisa **zerar a cada post** (loop externo = post, loop interno = soma os interesses).
4. **Esquecer o `return`** no final da função.
5. **Montar a chave errado na concatenação**: `f"post:{chave}"` quando `chave` já é `"post:345"` → vira `"post:post:345"`. Cuidado ao reusar uma variável que já é uma chave completa.
6. **`zrange`/`lrange` sem os índices** `0, -1` — são obrigatórios, não tem valor default.
7. **Desempate em ordenação por score**: quando há empate, usar uma chave secundária no `sorted`, ex: `key=lambda x: (-x[1], int(x[0].split(":")[1]))` (score decrescente, id crescente em caso de empate).

---

## Comparativo final rápido — Cassandra x Redis

| Aspecto | Cassandra | Redis |
|---|---|---|
| Tipo de banco | Colunar, distribuído, persistente | Chave-valor, em memória (cache) |
| Quando usar | Dados que precisam durar, volume grande, consultas previsíveis | Dados temporários, acesso rapidíssimo, cache |
| Conexão | `Cluster(...).connect()` | `redis.Redis(...)` |
| Modelagem | Pensa primeiro nas queries → define PRIMARY KEY | Pensa no formato do dado → escolhe a estrutura |
| Inserir | `INSERT INTO` (prepared statement) | `hset` / `rpush` / `sadd` / `zadd` conforme estrutura |
| Buscar | `SELECT` (prepared statement) | `hgetall` / `lrange` / `smembers` / `zrange` |
| Atualizar | novo `INSERT` com mesma PK sobrescreve, ou `UPDATE` | `hset` (sobrescreve campo) |
| Deletar | `DELETE FROM` | `delete` / `hdel` / `srem` / `zrem` |
| Evitar duplicata | `PRIMARY KEY` única | Set nativo (`sadd` não duplica) |
| Expiração automática | TTL nativo por coluna (menos comum em exercícios) | `expire()` — bem mais usado |
| Filtro "está numa lista" | `IN` (menos comum) | `sismember` |
| Relacionar dados | Tudo na mesma tabela/linha, ou JOIN manual em Python | Convenção de nome de chave (`post:345:tags`) |
| Serialização de objetos complexos | Tipos nativos (`LIST`, `MAP`, `FROZEN`) | `json.dumps()` / `json.loads()` |
