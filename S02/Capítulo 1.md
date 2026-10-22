[[S02/Introdução|Introdução]]
## O que é NoSQL
- "Not Only SQL"
	- Aproveita coisa de SQL
- Não segue filosofia base de Banco de Dados Relacional
- Banco de dados para trabalhar com "Big Data"
	- Grande quantidade de dados que são gerados a todo momento e com alta variedade
- Empresas normalmente não usam tudo em um ou outro, mas uma mistura para o que for necessário
- São tipos de SGBD's
## Principais Objetivos
- Criado em uma época que não existia a ideia do Big Data, por isso não veio pra substituir, mas pra complementar
1. Schemaless:
	- Não tem esquema, se tiver ele é mais permissível
2. Escalabilidade:
	- Adiciona e reorganiza nós de armazenamento com facilidade
	- Consegue particionar os dados para guardar em várias máquinas diferentes mais rápido abrindo mão do ACID
3. Abre mão do ACID e segue o modelo BASE
4. Precisa mais de **disponibilidade** do que de **consistência**
	- Dependendo da sua aplicação é importante, como o IFood, diferente de um banco que precisa da consistência
## Modelo BASE
- Não pode virar várzea também
- BA(Basically Available): algumas partes ficam disponíveis mesmo com falhas parciais
- S(Soft State): sempre que houver uma mudança no dado, o sistema não necessariamente muda todas as réplicas imediatamente. Necessariamente dados **não** cruciais.
- E(Consistência eventual): eventualmente os dados são atualizados, mudando o soft state para o correto.
- Em um mesmo momento pode se ter dois estados diferentes de um mesmo nó, até o banco sincronizar.

| **Característica**  | **ACID**                                                                                    | **BASE**                                                                               |
| ------------------- | ------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| **Consistência**    | **Alta consistência** (garante que todas as réplicas tenham o mesmo valor simultaneamente). | **Consistência mais fraca** (ex: _Eventually Consistent_ - consistente eventualmente). |
| **Disponibilidade** | Menor disponibilidade em favor da precisão.                                                 | **Maior disponibilidade** (prioridade total ao acesso).                                |
| **Operações**       | Isolamento de operações (mais demoradas, porém mais precisas).                              | Sistema mais simplificado e veloz.                                                     |
| **Transações**      | O **banco de dados** é responsável pelo gerenciamento das transações.                       | As transações devem ser implementadas pelo **programador**.                            |
| **Flexibilidade**   | Evolução de dados mais lenta (exige **Esquemas/Schemas**).                                  | Evolução rápida dos tipos de dados (**Schemaless/Sem esquema**).                       |
| **Perfil**          | Sistema mais conservador.                                                                   | Sistema focado em escalabilidade e disponibilidade.                                    |

## Tipos de BDs NoSQL
 - Diferente dos relacionais que utilizam tabelas para armazenamento de dados, NoSQL incluem diferentes modelos de acesso e armazenamento de dados, cada um adequado para um uso:
	 - Documento
	 - Grafos
	 - Chave-Valor
	 - Colunas
### Documentos:
- Armazenados em JSON documents
- Mais rápida de criar novos atributos em documentos individuais, só criar uma nova chave
- Um só documento pode possuir todas as informações necessárias
- Bom para uso de coisas que precisam de uma adição rápida de atributos, como uma rede social com comentários e likes em um post.
### Grafos:
- Não lineares
- Feito para fazer conexões diversas 
- Suas conexões podem ter peso que possui uma relevância que pode ser maior que o vértice em si
- Cada nó e cada aresta pode ser um único documento JSON
- Nós(Vértices), Relacionamentos(Arestas) e propriedades(atributos dos nós e relacionamento)
- Exemplo de uso: Responder facilmente a relação entre alguns dos personagens de um filme. Sistemas de recomendações também.
### Chave-Valor:
- Pares de chave-valor
- Ao invés de ter vários documentos com chave-valor dentro deles, esse é um único documentuzão com muitas chave-valores, como uma tabela HASH, Map do Java ou Dictionary do Python.
- Feitas para acesso rápido, já que você só precisa saber a chave
- De começo a ideia era rodar na RAM, pra você ter uma performance ainda maior.
- Exemplo: Qualquer lugar que tem dados voláteis e precisa de acesso rápido, como um carrinho de compra na web
### Colunas:
Não entendi legal
- Também usa chave-valor que tenta resolver o problema da horizontalidade dos SQLs
- Se o banco de dados não tem uma coluna, eu posso simplesmente não ter
- Cada registro tem uma chave pra uma coluna
- Definem Partition Key, que é o id da instância computacional que o dado está
- Cada máquina é responsável por uma partição
- Torna os dados mais enxutos e partidos
- Foco em volume 
## Teorema CAP
- Não existe BD dos sonhos, alguma coisa você joga fora para ter duas outras.
- C - Consistency
- A - Availability
- P - Partitioning Tolerance
- Usado para definir o perfil de armazenamento de dados distribuídos
- Redes sociais abrem mão de Consistência para ter Disponibilidade(estar disponível sempre) e particionar os dados(não tem como guardar todos os dados em um único lugar)
## O que falta nos NoSQLs
Não garante essas coisas, sua aplicação deve garantir isso por ela mesma.
- Joins
- Suporte a transações(Transactions): roleback
- Suporte a restrições(Constraints): chave estrangeira, chave primária
## O que geralmente oferecem:
- Sua própria Query Language
- Melhor desempenho, principalmente em bases de dados distribuídas
- Escalabilidade horizontal