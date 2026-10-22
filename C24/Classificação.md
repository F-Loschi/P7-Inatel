- Tarefa de aprendizado supervisionado
- Envolve encontrar uma função que mapeie os atributos de entrada em um **conjunto finito de valores discretos**, ou seja, **classes**.
## Tipos de Classificadores
- Organizamos os tipos de classificadores seguindo dois critérios:
	- Número total de classes possíveis
	- Quantidade de classes atribuídas a cada amostra
- Dependendo do número de classes possíveis, Q, podemos separar os classificadores em dois tipos:
	- Binários
	- Multiclasses
- Podemos separaar os classificadores dependendo de quantas classes podem ser atribuídas a uma única instância:
	- Classe **single-label**: apenas uma classe. Inclui binária e multiclasses. Mutuamente exclusivas.
	- Classificação **multilabel**: Amostra pode ter várias classes simultaneamente. Não são mutuamente exclusivas.
## Algoritmos de classificação
### Regressor logístico
Classificador binário e single-label
### Regressor softmax
Classificador multiclasses e single-label
### Árvore de decisão
### Redes neurais
## Classificação binária
Única saída escalar para indicar a classe a que pertence o i-ésimo vetor de atributos, x(i).
Possível utilizar 0 e 1 e -1 e 1.
## Classificação Multiclasse
- Quando possui Q saídas escalares, uma para cada classe, para indicar a classe a que pertence o i-ésimo vetor de atributos, x(i).
- Rótulos são representados como vetores binários
- Codificação one-hot
## Classificação Multilabel
- Tem Q saídas escalares, uma para cada classe, porém, cada i-ésimo vetor de atributos, x(i) pode pertencer a várias classe simultaneamente
- Rótulos também são representados como vetores binários
## Fronteiras de Decisão de um Classificador
Usamos funções hipótese para aproximar o comportamento do conjunto de dados, agora usaremos para separar grupos de dados em classes.
![[Pasted image 20260326175445.png]]
- Objetivo é encontrar uma função chamada de discriminante, g(x), que separe as classes
- Chamamos de fronteira de decisão onde essa função corta o espaço de atributos
- Podem ser lineares ou não lineares
### Caso binário
Objetivo é encontrar o grau e os pesos da função discriminante de tal forma que a classe atribuída a x(i) seja: 
$$C_q = \begin{cases} q = 1, & g(x(i)) < 0 \quad \text{(Amostra acima da função)} \\ q = 2, & g(x(i)) > 0 \quad \text{(Amostra abaixo da função)} \\ \text{Indeterminação}, & g(x(i)) = 0 \quad \text{(Amostra sobre a função)} \end{cases}$$

- Em caso de indeterminação podemos:
	- Atribuir arbitrariamente a uma das duas classes
	- Escolher a classe que possui mais amostras ou a mais frequente
- Quanto mais distante a amostra estiver da fronteira de decisão, maior é o valor absoluto de g(x) e vice versa
## Como encontramos o grau e pesos das funções discriminantes
- Para calcular o erro entre os rótulos, y, e a saída do modelo, ^y, ela deve estar no intervalo [0, 1].
- Podemos treinar modelos de classificação, essa função deve ser contínua e diferenciável
- Chamada função de limiar de decisão ou de ativação
- Uma função que apresenta tais características é a **função logística**, também conhecida como **sigmoide**.
- A saída pode ser interpretada como a **probabilidade de a classe positiva C2, dado os vetores x(i) e a, a probabilidade de C2**.
.
.
.
## Função de erro
Nosso objetivo será, assim como na regressão linear, dado uma função discriminante, encontrar seus pesos de forma que o erro de classificação seja minimizado.
Precisamos de uma função de erro para treinarmos um regressor logístico. Porém, usar a função do erro quadrático médio não é uma boa escolha no caso da regressão logística e classificadores em geral.