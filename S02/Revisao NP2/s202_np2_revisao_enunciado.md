# NP2 - Revisão

Nessa atividade você deve usar seus conhecimentos sobre banco de dados baseados em colunas e chave-valor, mais especificamente sobre Cassandra e Redis para atender os requisitos pedidos.
Todos as questões têm um exemplo de caso de teste (com dados de entrada e saída esperada) para que você valide a sua solução.

_Construa os métodos das classes de acesso aos dados (DAO) de acordo com a descrição das questões e com base na implementação de cada caso de teste._

**Contexto**: Imagine que você está desenvolvendo um banco de dados para uma plataforma de streaming de conteúdo educacional. Essa plataforma tem um volume muito grande de acessos e visualizações e por isso foram escolhidos sistemas de gerenciamento de bancos de dados NoSQL. Os principais objetivos do sistema são:

i. cadastrar alunos e manter um registro de suas áreas de estudo preferidas ao longo do tempo;
ii. cadastrar cursos e suas categorias;
iii. exibir uma lista de cursos mais recomendados para um determinado aluno;
iv. armazenar temporariamente as informações de cursos na lista de desejos;
v. e registrar as informações de uma matrícula efetivada.

Para manter as informações das matrículas realizadas de forma persistente e distribuída, as tabelas de matrículas, cursos e alunos foram registrados no Cassandra.
Apesar de ter um esquema flexível, considere as seguintes informações:

- Aluno (id: int, pais: text, cidade: text, endereço: text, nome: text, email: text, areas_estudo: list<text>)
- Curso (id: int, categoria: text, nome: text, custo_producao: float, preco: float, duracao_horas: int)
- Matricula (id: int, dia: int, mês: int, ano: int, hora: text, valor_total: float, cursos_quantidade: list<map<int, int>>, aluno_id: int)

Os administradores da plataforma querem manter os dados de alunos de um **mesmo país e cidade juntos no banco de dados** para facilitar a busca, **usando o id para complementar**. **Cursos devem ser agrupados por categoria, também usando id para ordenar os cursos em uma mesma partição.** Por fim, os dados das **matrículas devem ser particionados por dia, mês e ano, usando a hora e o id para complementar a identificação de uma matrícula**.

A fim de manter consultas rápidas, algumas informações do aluno, suas preferências e seus cursos na lista de desejos são mantidas no Redis.

**Questão 1** Crie as tabelas de alunos e cursos e registre as informações no Cassandra. Em seguida realize as consultas que retornem:

a. a quantidade de alunos registrados;
b. e o custo total de produção de todos os cursos (obs.: o custo registrado é apenas o custo unitário de produção de cada curso).

**Questão 2** Carregue do Cassandra as informações de cada um dos alunos do país "Brasil", incluindo a lista de áreas de estudo, registre no Redis e realize a consulta no Redis para apresentar os dados registrados.

**Questão 3** Considere que o aluno 2 acessa o feed dele. Use a lista de áreas de estudo desse aluno registrada no Redis para buscar as informações sobre cursos mais interessantes no Cassandra (considere que a lista de áreas de estudo contém os nomes das categorias de cursos interessantes).

**Questão 4** Considere que o aluno 2 seleciona alguns cursos para a sua lista de desejos. Registre essas informações no Redis e realize uma consulta para mostrar os dados cadastrados.

**Questão 5** Crie a tabela de matrículas no Cassandra. Considere que o aluno 2 efetiva a matrícula dos cursos em sua lista de desejos. Realize uma consulta no Redis dos dados da lista de desejos desse aluno e registre as informações sobre essa matrícula no Cassandra. Por fim, recupere os dados de todas as matrículas no Cassandra.
