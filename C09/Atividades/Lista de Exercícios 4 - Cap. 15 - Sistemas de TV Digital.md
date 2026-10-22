Felipe Silva Loschi
GES - 601
## 1. Explique o conceito de varredura entrelaçada (interlaced scanning) e descreva como ela permitia reduzir a percepção de cintilação sem aumentar a banda de frequências necessária.
A varredura entrelaçada é usada para reduzir a percepção de cintilação sem aumentar a banda necessária. Ele funciona dividindo o quadro em dois campos: um contendo apenas as linhas ímpares e o outro apenas as linhas pares. Cada campo possui 262,5 linhas e é desenhado em 1/60 de segundo. O olho funde os dois em uma única imagem e passa a percepção de que a tela é atualizada 60 vezes por segundo, quando na verdade é apenas 30 quadros completos por segundo.

## 2. Explique o teorema de Nyquist aplicado a digitalização de sinais de TV. O que e o fenômeno de aliasing é, como ele pode ser evitado?
O teorema de Nyquist diz que a frquência de amostragem deve ter pelo menos o dobro da frequência máxima do sinal amostrado. 

## 3. Descreva o "efeito penhasco" (cliff effect) da TV digital e compare-o com o comportamento da TV analógica.
O efeito penhasco da TV digital descreve como funciona o desvanecimento do sinal, que na TV digital ocorre de uma vez, fazendo com que a tela congele ou exiba tela preta. Ao contrário da TV digital, na TV analógica há a degradação gradual, o que gera efeitos como "fantasmas" e faixas na tela.
## 4. Por que o desafio do baixo custo é mais crítico no projeto de receptores do que no de transmissores?
Devido a diferença entre a quantidade de ambos, é necessário apenas um transmissor por estação, o que dilui o preço entre os telespectadores, mas na recepção é necessária milhões de unidades de receptores, sendo que todos devem ser acessíveis a população para viabilizar a TV digital.
## 5. No sistema de TV Digital, qual é a etapa responsável por converter os dados digitais em sinais analógicos de radiofrequência (no transmissor) e, posteriormente, reverter esse processo para o formato digital (no receptor)?
No transmissor é o modulador, responsável por imprimir o fluxo de bits digitais da portadora. No receptor é o demodulador, responsável por extrair o fluxo de bits da portadora, reconstruindo os dados digitais para serem descomprimidos.
## 6. Explique de forma geral como são aplicadas compressões através de Redundância Temporal.
Quando quadros vizinhos são muito parecidos, assim, transmite-se apenas as diferenças com relação ao quadro anterior em um vetor de movimento que indica o deslocamento entre cada bloco. 
## 7. Explique de forma geral como são aplicadas compressões através de Redundância Espacial.
Olho humano é pouco sensível a altas frequências espaciais, então, quando uma imagem é dividida em blocos de 8x8 pixels, é aplicada a DCT e a energia se concentra em poucos coeficientes de baixa frequência, o que faz com que os coeficientes de alta frequência possam ser eliminados na quantização.
## 8. Explique os três tipos de quadros usados na compressão MPEG-2: quadros I, P e B. Qual é a função do Group of Pictures (GOP) e como os parâmetros N e M definem a sua estrutura?

| Tipo | Nome          | Descrição                                                             |
| ---- | ------------- | --------------------------------------------------------------------- |
| I    | Intra Frame   | Quadro completo, independente - âncora do GOP                         |
| P    | Predicted     | Baseado no quadro anterior; alta compressão                           |
| B    | Bidirectional | Diferença em relação ao quadro anterior e posterior, maior compressão |
O GOP define como os quadros são organizados em sequência, sendo N o total de quadros e M quantos Bs existem para cada P.