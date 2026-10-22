- Tarefa de Aprendizado Supervisionado
	- Saídas esperadas conhecidas
- Envolve encontrar uma função que **MAPEIE** os atributos em valores reais
- Um dos algoritmos mais simples, antigos e usados de aprendizado de máquina
- Nos dará intuições importantes para o entendimento de algoritmos mais complexos, como classificadores e redes neurais
- Objetivo: Mapear os atributos de forma a achar o menor erro possível
- Paradigma: Aprendizado supervisionado
- Função aproximadora é modelada como sendo uma combinação linear dos atributos em relação ao peso
- Em geral usamos polinômios
- Maior grau != melhor modelo
- Flexibilidade excessiva pode levar ao overfitting
- Flexibilidade de menos pode levar ao underfitting
## Como determinar pesos e grau
- Já tendo as entradas e saídas, o objetivo é encontrar pesos ótimos
- Comum utilizar o erro quadrático médio, que é a média aritmética dos erros ao quadrado
- Gradiente descendente:
	- Otimização iterativa
	- Modelo aprendo os pesos "passo a passo"
	- Pode não encontrar a solução ótima devido a vários fatores
	- Inicia com pesos aleatórios e vai caminhando para o mínimo
- Superfície de erro: representação geométrica de quão "errado" o nosso modelo está para cada combinação possível de pesos
## Overfitting
- Ajuste tão bem que modelo não vai saber classificar coisas diferentes
- Matar uma mosca com bazuca
## Underfitting
- Ajuste tão mal feito que modelo não vai saber classificar nada
- Tentar matar um dinossauro com um mata mosca