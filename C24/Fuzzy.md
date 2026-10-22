## Lógica Fuzzy
- Paradigma probabilístico/estatístico
- Trabalho com informações imprecisas ou aproximadas
- Região nebulosa: pode estar nos dois estados, é necessário analisar outros fatores para decidir a qual grupo pertence
- Características:
	- Expressam imprecisões/incertezas
	- Sistemas baseados em regras do tipo linguísticas
	- "Raciocínio" executado de forma aproximada
	- Conclusões obtidas de forma paralela
- Conceito de pertinência:
	- Teoria clássica: Dado um conjunto A em um universo X, os elementos deste universo simplesmente pertencem ou não pertencem àquele conjunto.
	- Conjunto Fuzzy: Um conjunto fuzzy A em um universo X pode ser definido por uma função de pertinência:
		- $$\mu_A(x):X \rightarrow [0, 1]$$
	- e representado por um conjunto de pares ordenados:
		- $$A = \{\mu_A/x\} \text{ }x\in X$$
	- A função define o grau de pertinência de um elemento em um conjunto Fuzzy, levando-se em conta seu universo é discurso, é definida como função de pertinência:
		- $$\mu_A(x):X \rightarrow [0,1]$$
- Tipos de funções de pertinência:
	- Podem ser usadas vários tipos de funções, sendo definido de acordo com a aplicação
- Altura de um conjunto Fuzzy: Maior grau de pertinência assumido por um de seus elementos
- Suporte de Conjunto Fuzzy(Conjunto Suporte): Conjunto de todos os elementos de A que possuem graus de pertinência maior que zero
- **Normalizado** se pelo **pelo menos** um elemento tem grau de pertinência 1
- Conjunto Fuzzy é Convexo **se e somente se** for observada a seguinte desigualdade:
	- $$\mu_A(\lambda\times x_1+(1-\lambda)\times x_2) \geq MIN[\mu_A(x_1),\mu_A(x_2)]$$
	- $$x_1,x_2 \in X; \lambda \in [0;1]$$
- Cardinalidade do Conjunto Fuzzy: Soma dos graus de pertinência de todos os elementos do conjunto. Em conjuntos discretos varia de 0 ao número de elementos no conjunto. Em conjuntos contínuos, pode tender ao infinito.
- Corte em Conjuntos Fuzzy: Todos os elementos do conjunto cujos quais possuem um grau de pertinência maior que um limiar alpha a ser definido.
## Operações em Conjuntos Fuzzy
- Conjunto Fuzzy Vazio: **se e somente se** sua função de pertinência é igual a zero para todo X
- Conjunto Fuzzy Complemento: 1 - pertinência da amostra
- Igualdade de Conjuntos Fuzzy: **se e somente se** a pertinência de todos os elementos do conjunto forem iguais
- Subconjunto Fuzzy: um conjunto A é um subconjunto de B se sua função de pertinência for menor ou igual a de B para todos seus elementos
- Conjunto União: Tira-se o máximo para todos os elementos
- Conjunto Interseção: Tira-se o mínimo para todos os elementos
## Sistemas Fuzzy
- Fazer uma lista do que realmente importa para se chegar as condições ou regras descritivas
- A ordem em que as regras são apresentadas é arbitrária, ou seja, não importa quem vem primeiro
- Aquele em que as variáveis de entrada e saída são representadas por funções de pertinência através de variáveis linguísticas e relacionadas através de regras do tipo: Se <condição> então <ação>
### Funcionamento
![[Pasted image 20260618143240.png]]
- Fuzzificação:
	- Classificar o valor numérico de entrada de acordo com termos linguísticos relacionados aos conjuntos fuzzy que definem a função de pertinência
	- Ocorre também a ativação de regras relevantes para uma dada situação
	- Qual o grau de pertinência para cada função
- Inferência:
	- "Raciocínio do sistema"
	- Identifica quais regras foram ativadas e quais conjuntos fuzzy de saída serão ativados e com qual intensidade
	- Obtém o conjunto fuzzy de saída através do processo de Inferência
- Defuzzificação:
	- Papel inverso à fuzzificação, ou seja, produz uma saída numérica correspondente aos conjuntos de saída atividos
	- Necessários pois geralmente são necessárias saídas precisas
	- $$ CoG = \sum x \times \mu(x)/\sum\mu(x) $$
	- Método da Média dos Máximos(MoM): Gera uma ação de controle que representa o valor médio de todas as ações de controle individuais cujos funções de pertinência assumem o máximo
	- Método do Centro de Gravidade(CoG): A ação de controle numérica é calculada obtendo-se o centro de gravidade da distribuição de possibilidades da ação de controle global
### Sistemas Fuzzy SISO
- SISO: single input, single output
### Sistemas Fuzzy MISO
- MISO: multiples input, single output
