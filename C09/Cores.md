[[Transformações Geométricas pt.3]]
- Sensação produzida pela luz que chega aos olhos
- Psicofísico, pois envolve psicologia e física
- Faixa pequena do espectro eletromagnético
## Cores primárias
- RGB é baseado na mistura de luzes
- Quando combinamos cores diferentes, o resultado é sempre mais brilhante do que cada componente individual, por isso o processo é **aditivo**
### Aditivo(RGB):
- Vermelho: (255, 0, 0)
- Verde: (0, 255, 0)
- Azul: (0, 0, 255)
Ao misturar, o aditivo pega o maior valor de cada canal:
- Amarelo: (255, 255, 0)
### Subtrativa(CMYK);
- Ciano: (0, 255, 255)
- Magenta: (255, 0, 255)
- Amarelo: (255, 255, 0)
Ao misturar, o subtrativo pega o menor valor de cada canal:
## Conversão RGB <-> CMYK:
- Feito de forma matricial:
$$\begin{bmatrix} C \\ M \\ Y \end{bmatrix} = \begin{bmatrix} 1 \\ 1 \\ 1 \end{bmatrix} - \begin{bmatrix} R \\ G \\ B \end{bmatrix}$$
- Ou então:
$$\begin{bmatrix} R \\ G \\ B \end{bmatrix} = \begin{bmatrix} 1 \\ 1 \\ 1 \end{bmatrix} - \begin{bmatrix} C \\ M \\ Y \end{bmatrix}$$
## Conversão RBG -> CMYK:
