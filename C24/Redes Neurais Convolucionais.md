- Até agora as MLPs tinham apenas camadas densas, onde os neurônios são conectados, e teremos agora camadas convolucionais
## DNNs vs. CNNs
- Ao invés de aprender os pesos, ela aprende os valores de filtros de convolução(***kernels***) que compreendem o conteúdo de imagens
- --
- CNNs são usadas em tarefas de visão computacional, como classificação de imagens, detecção de objetos, etc.
- --
## Por que não usar DNN
- DNN é ideal para tabulares, representados por linhas e atributos por colunas
- Objetivo é aprender relação entre atributos, sem presumir uma estrutura espacial entre eles
- A posição espacial não influencia no resultado
- DNN aprende padrões globais
- Ignoram localidade de referência ou espacial em dados com topologia de grade, tanto computacional quanto semanticamente
- Pixels vizinhos são importantes por terem relações
- Gera um alto custo computacional, pois o número de pesos é muito maior, risco maior de overfitting
## Por que usar CNN
- Mais eficientes por identificarem padrões nos kernels
- Propriedade de localidade diz que pixels próximos tendem a estar correlacionados
- A primeira camada aprendem pequenos padrões da imagem e as camadas seguinte juntam isso para criar alguma informação
- Existem regiões que trazem informações importantes e outras que não(cabeça e corpo respectivamente)
- Cada neurônio olha apenas para uma pequena região chamada de campo receptivo
- O tamanho do campo é definido por uma matriz chamada de filtro de convolução ou kernel
- Estacionariedade significa que o mesmo padrão pode aparecer em qualquer posição da imagem(um olho pode estar em qualquer parte da imagem)
- CNNs compartilham os pesos: mesmo filtro é aplicado em toda a imagem, ou seja, um filtro que detecta bordas é o mesmo para todas as posições
	- Muitos menos parâmetros
	- Melhora generalização
	- Capacidade de detectar o mesmo padrão em qualquer posição
- Imagens possuem estrutura hierárquica
- Padrões simples formam padrões complexos
	- Simples: contorno da orelha, bordo do nariz e do olho
	- Intermediário:
	- Avançado:
## CNN
- Composta por:
	- Imagem de entrada
	- Um ou mais grupos de camadas de convolução ou pooling
	- Camada flatten
	- Uma ou mais camadas totalmente conectadas
	- Função de ativação softmax
### Camada de Convolução
- Responsável por extrair características da imagem
- Aplica filtros sobre a imagem
- Após o filtro, aplica-se uma função de ativação
- Processo é repetido por toda a imagem
- O resultado é um mapa de características detectadas
### Filtros de convolução
- Filtros são treinados para detectar características
- Baseado no córtex visual
- Respondem a padrões específicos em pequenas regiões do campo visual chamadas campos receptivos
- À medida que o sinal visual perc
- Um kernel é um tensor responsável
- Detecta um tipo particular de característica, como bordas, etc
- Resultado da operação de convolução é chamado de mapa de características ou de ativação
- Fornece