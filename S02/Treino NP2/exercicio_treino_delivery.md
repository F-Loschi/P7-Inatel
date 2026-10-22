# Exercício de Treino — Cassandra + Redis
## Tema: Plataforma de Delivery de Comida

---

## Contexto

Você está desenvolvendo o backend de dados de um aplicativo de delivery de comida. O sistema tem um volume grande de pedidos e precisa de respostas rápidas pro usuário, então foram escolhidos bancos NoSQL.

Os objetivos do sistema são:

i. cadastrar restaurantes e seus pratos;
ii. cadastrar pedidos feitos pelos clientes;
iii. manter um carrinho de compras temporário pra cada cliente;
iv. calcular e exibir os restaurantes mais bem avaliados de uma cidade;
v. registrar um ranking de pratos mais pedidos.

Para manter as informações de restaurantes e pedidos de forma persistente e distribuída, essas tabelas foram registradas no **Cassandra**. Considere o seguinte esquema (flexível, mas use como base):

- **Restaurante** (id: int, cidade: text, categoria: text, nome: text, avaliacao: float)
- **Prato** (id: int, restaurante_id: int, nome: text, preco: float, categoria: text)
- **Pedido** (id: int, dia: int, mes: int, ano: int, hora: text, cliente_id: int, restaurante_id: int, valor_total: float, itens: list\<frozen\<map\<int, int\>\>\>)

Os administradores querem manter os restaurantes agrupados por **cidade**, usando o **id** pra complementar. Os pratos devem ser agrupados por **restaurante_id**, também usando **id** pra ordenar dentro da partição. Por fim, os pedidos devem ser particionados por **dia, mês e ano**, usando **hora** e **id** para complementar a identificação.

Para consultas rápidas de carrinho e ranking, o **Redis** é utilizado.

---

## Questão 1 (20 pts)

Crie a tabela de restaurantes no Cassandra e registre as informações dadas no caso de teste. Em seguida, realize uma consulta que retorne **todos os restaurantes de uma cidade específica**, ordenando o resultado (em Python, após a consulta) pelo `id`.

## Questão 2 (20 pts)

Crie a tabela de pratos no Cassandra e registre as informações dadas no caso de teste. Em seguida, realize uma consulta que retorne **todos os pratos de um restaurante específico**.

## Questão 3 (20 pts)

Considere que um cliente está montando seu carrinho de compras. Cada vez que ele adiciona um prato, registre esse prato (id, nome e preço) numa lista de carrinho no Redis para aquele cliente específico. Implemente também a consulta que retorna o carrinho completo de um cliente.

> Dica: pense em qual estrutura do Redis comporta uma coleção de itens (dicts) sem precisar de campos fixos.

## Questão 4 (20 pts)

Quando o cliente finaliza o pedido, registre as informações no Cassandra (tabela Pedido), com o `valor_total` calculado a partir da soma dos preços dos itens do carrinho (recuperados do Redis) e a lista de `itens` no formato `[{prato_id: quantidade}, ...]` (considere quantidade sempre 1 por item do carrinho). Depois, recupere os pedidos feitos em uma data específica.

## Questão 5 (20 pts — bônus)

Mantenha no Redis um **ranking dos pratos mais pedidos** (cada vez que um pedido é feito, cada prato do pedido ganha +1 no ranking). Implemente a consulta que retorna os 3 pratos mais pedidos, do maior para o menor número de pedidos.

> Dica: pense em qual estrutura do Redis já ordena automaticamente por um número, e qual comando incrementa esse número.

---

## Casos de Teste (para você validar)

```python
restaurantes = [
    {"id": 1, "cidade": "Itajubá", "categoria": "Italiana", "nome": "Cantina Bella", "avaliacao": 4.5},
    {"id": 2, "cidade": "Itajubá", "categoria": "Japonesa", "nome": "Sushi Mountain", "avaliacao": 4.8},
    {"id": 3, "cidade": "Pouso Alegre", "categoria": "Brasileira", "nome": "Sabor Mineiro", "avaliacao": 4.2},
]
# get_restaurantes_cidade("Itajubá") deve retornar os restaurantes 1 e 2, ordenados por id

pratos = [
    {"id": 10, "restaurante_id": 1, "nome": "Lasanha", "preco": 38.90, "categoria": "Massa"},
    {"id": 11, "restaurante_id": 1, "nome": "Risoto", "preco": 42.00, "categoria": "Arroz"},
    {"id": 12, "restaurante_id": 2, "nome": "Combo Sushi", "preco": 55.00, "categoria": "Sushi"},
]
# get_pratos_restaurante(1) deve retornar os pratos 10 e 11

# Questão 3: cliente_id = 100 adiciona ao carrinho os pratos 10 e 11
# get_carrinho(100) deve retornar:
# [{"id": 10, "nome": "Lasanha", "preco": 38.90}, {"id": 11, "nome": "Risoto", "preco": 42.00}]

# Questão 4: finalizar_pedido(id=1, data_hora=datetime.now(), cliente_id=100, restaurante_id=1)
# valor_total esperado = 38.90 + 42.00 = 80.90
# itens esperado = [{10: 1}, {11: 1}]
```

---
---

# GABARITO COMENTADO

> Tente resolver sozinho primeiro! O gabarito abaixo é só pra conferência.

## Questão 1

```python
class RestauranteDAO:
    def __init__(self):
        self.cassandra_session = CassandraDBConnector.get_session()

    def criar_tabela(self):
        query = """
            CREATE TABLE restaurante(
                id INT,
                cidade TEXT,
                categoria TEXT,
                nome TEXT,
                avaliacao FLOAT,
                PRIMARY KEY((cidade), id)
            );
        """
        self.cassandra_session.execute(query)

    def adicionar(self, restaurante):
        query = "INSERT INTO restaurante(id, cidade, categoria, nome, avaliacao) VALUES (?, ?, ?, ?, ?);"
        prepared = self.cassandra_session.prepare(query)
        self.cassandra_session.execute(prepared, [
            restaurante.id, restaurante.cidade, restaurante.categoria,
            restaurante.nome, restaurante.avaliacao
        ])

    def get_restaurantes_cidade(self, cidade: str):
        # cidade é a partition key COMPLETA aqui -> não precisa de ALLOW FILTERING
        query = "SELECT * FROM restaurante WHERE cidade = ?;"
        prepared = self.cassandra_session.prepare(query)
        resultado = self.cassandra_session.execute(prepared, [cidade])

        restaurantes = []
        for r in resultado:
            restaurantes.append(Restaurante(
                id=r["id"], cidade=r["cidade"], categoria=r["categoria"],
                nome=r["nome"], avaliacao=r["avaliacao"]
            ))
        return sorted(restaurantes, key=lambda x: x.id)
```

**Pontos de atenção:** como `cidade` é a partition key inteira (não é parte de uma chave composta), **não precisa** de `ALLOW FILTERING` — diferente do exercício do aluno, onde `pais` era só parte de `(pais, cidade)`.

---

## Questão 2

```python
class PratoDAO:
    def __init__(self):
        self.cassandra_session = CassandraDBConnector.get_session()

    def criar_tabela(self):
        query = """
            CREATE TABLE prato(
                id INT,
                restaurante_id INT,
                nome TEXT,
                preco FLOAT,
                categoria TEXT,
                PRIMARY KEY((restaurante_id), id)
            );
        """
        self.cassandra_session.execute(query)

    def adicionar(self, prato):
        query = "INSERT INTO prato(id, restaurante_id, nome, preco, categoria) VALUES (?, ?, ?, ?, ?);"
        prepared = self.cassandra_session.prepare(query)
        self.cassandra_session.execute(prepared, [
            prato.id, prato.restaurante_id, prato.nome, prato.preco, prato.categoria
        ])

    def get_pratos_restaurante(self, restaurante_id: int):
        query = "SELECT * FROM prato WHERE restaurante_id = ?;"
        prepared = self.cassandra_session.prepare(query)
        resultado = self.cassandra_session.execute(prepared, [restaurante_id])

        pratos = []
        for p in resultado:
            pratos.append(Prato(
                id=p["id"], restaurante_id=p["restaurante_id"], nome=p["nome"],
                preco=round(float(p["preco"]), 2), categoria=p["categoria"]
            ))
        return pratos
```

**Pontos de atenção:** `round(float(...), 2)` no preço, pela mesma imprecisão de `FLOAT` que vimos na prova.

---

## Questão 3

```python
import json

class CarrinhoDAO:
    def __init__(self):
        self.redis_connection = RedisDBConnector.get_connection()

    def adicionar_ao_carrinho(self, cliente_id: int, prato_id: int, nome: str, preco: float):
        item = {"id": prato_id, "nome": nome, "preco": preco}
        self.redis_connection.rpush(f"carrinho:{cliente_id}", json.dumps(item))

    def get_carrinho(self, cliente_id: int):
        itens_string = self.redis_connection.lrange(f"carrinho:{cliente_id}", 0, -1)
        return [json.loads(item) for item in itens_string]
```

**Por que List, não Hash?** Porque o carrinho é uma **coleção de itens variados** (pode ter 1, 2, 10 pratos), não um objeto de campos fixos. Hash serviria se fosse "um carrinho = um objeto com campos nome/total/etc", mas aqui cada item é um dict completo — por isso List + JSON.

---

## Questão 4

```python
class PedidoDAO:
    def __init__(self):
        self.cassandra_session = CassandraDBConnector.get_session()
        self.redis_connection = RedisDBConnector.get_connection()

    def criar_tabela(self):
        query = """
            CREATE TABLE pedido(
                id INT,
                dia INT,
                mes INT,
                ano INT,
                hora TEXT,
                cliente_id INT,
                restaurante_id INT,
                valor_total FLOAT,
                itens LIST<FROZEN<MAP<INT, INT>>>,
                PRIMARY KEY((dia, mes, ano), hora, id)
            );
        """
        self.cassandra_session.execute(query)

    def finalizar_pedido(self, id: int, data_hora: datetime, cliente_id: int, restaurante_id: int):
        carrinho_dao = CarrinhoDAO()
        carrinho = carrinho_dao.get_carrinho(cliente_id)

        valor_total = sum(float(item["preco"]) for item in carrinho)
        itens = [{int(item["id"]): 1} for item in carrinho]

        dia = data_hora.day
        mes = data_hora.month
        ano = data_hora.year
        hora = data_hora.strftime("%H:%M")

        query = """
            INSERT INTO pedido(id, dia, mes, ano, hora, cliente_id, restaurante_id, valor_total, itens)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);
        """
        prepared = self.cassandra_session.prepare(query)
        self.cassandra_session.execute(prepared, [
            id, dia, mes, ano, hora, cliente_id, restaurante_id, valor_total, itens
        ])

    def get_pedidos_data(self, data_hora: datetime):
        dia = data_hora.day
        mes = data_hora.month
        ano = data_hora.year

        query = "SELECT * FROM pedido WHERE dia = ? AND mes = ? AND ano = ?;"
        prepared = self.cassandra_session.prepare(query)
        resultado = self.cassandra_session.execute(prepared, [dia, mes, ano])

        pedidos = []
        for p in resultado:
            pedidos.append({
                "id": p["id"],
                "cliente_id": p["cliente_id"],
                "hora": p["hora"],
                "valor_total": round(float(p["valor_total"]), 2)
            })
        return pedidos
```

**Pontos de atenção:**
- `LIST<FROZEN<MAP<INT, INT>>>` — mesma regra de coleção dentro de coleção que vimos na prova.
- `sum(float(item["preco"]) for item in carrinho)` é um jeito mais enxuto da função `soma_cursos` que você escreveu na manhã da prova — é uma generator expression dentro do `sum()`, faz a mesma coisa que um loop com acumulador.

---

## Questão 5 — Bônus

```python
class RankingDAO:
    def __init__(self):
        self.redis_connection = RedisDBConnector.get_connection()

    def registrar_pedido_no_ranking(self, itens_pedido: list):
        # itens_pedido: lista de dicts {prato_id: nome} vindos do carrinho, por exemplo
        for item in itens_pedido:
            self.redis_connection.zincrby("ranking:pratos", 1, item["nome"])

    def get_top_3_pratos(self):
        # zrevrange já retorna do maior pro menor score
        return self.redis_connection.zrevrange("ranking:pratos", 0, 2, withscores=True)
```

**Por que Sorted Set?** Porque você precisa de uma coleção **ordenada por um número** (quantidade de pedidos) — é a definição exata de pra que serve o ZSet. E o `zincrby` é o comando ideal aqui: em vez de você ler o score atual, somar +1 em Python e regravar, ele já faz o incremento atômico direto no Redis.

---

## Resumo do que esse exercício treina

| Questão | Conceito principal |
|---|---|
| 1 | Partition key simples (1 campo só) — sem `ALLOW FILTERING` |
| 2 | Mesma lógica da Q1, reforçando o padrão |
| 3 | List + JSON pra guardar dicts variados (não confundir com Hash) |
| 4 | `LIST<FROZEN<MAP>>>`, extração de data/hora, soma com conversão de tipo |
| 5 | Sorted Set + `zincrby` (variação do que vimos, que usava `zadd` direto) |
