Felipe Silva Loschi
GES - 601
## Questão 1:
### a) Organize em ordem cronológica
CRT, LCD, OLED e MicroLED
### b) Vantagem e desvantagem
CRT:
- Vantagens: Preto verdadeiro, contraste infinito, tempo de resposta instantâneo, qualquer resolução nativa, ângulos de visão perfeitos
- Desvantagens: Volumoso e pesado, alto consumo de energia, burn-in, radiação eletromagnética
LCD:
- Vantagens: Fino e leve, baixo consumo com LED (20-60W), alta resolução fácil (4K, 8K), sem burn-in permanente, custo baixo
- Desvantagens: Pretos imperfeitos (backlight sempre ligado), contraste limitado, motion blur, uniformidade (backlight bleeding)
OLED:
- Vantagens: Preto perfeito (pixel desligado = zero luz), contraste infinito, tempo de resposta <0.1ms, cores vibrantes (100% DCI-P3), fino (sem backlight), flexível
- Desvantagens: Burn-in permanente, vida útil limitada (30-50k horas, azul pior), sensível a umidade/oxigênio, custo alto, brilho sustentado limitado
MicroLED:
- Vantagens: Brilho extremo (5000-100.000 cd/m²), contraste infinito, sem burn-in (inorgânico), vida útil longa (100k+ horas), eficiência energética, cores puras
- Desvantagens: Custo absurdo (processo de mass transfer extremamente difícil), rendimento baixo, LED verde problema
### c)Amoled evolução do OLED e onde é usado
O AMOLED não é fundamentalmente diferente do OLED, mas uma evolução que busca resolver problemas critícos do OLED. O que muda é que a matriz ativa resolve problemas críticos de OLED passivo: permite resolução muito maior (cada pixel individualmente endereçável), elimina crosstalk entre pixels, e possibilita refresh rates altos essenciais para smartphones modernos. Atualmente, seu ele é o padrão para smartphones/tablets premium
## Questão 2:
### a) Translação de Tx=2 e Ty=-3
$$
\mathbf{p'} = \mathbf{T} \cdot \mathbf{p} = \begin{bmatrix} 1 & 0 & 2 \\ 0 & 1 & -3 \\ 0 & 0 & 1 \end{bmatrix} \begin{bmatrix} 3 \\ 5 \\ 1 \end{bmatrix} = \begin{bmatrix} 3+2 \\ 5-3 \\ 1 \end{bmatrix} = \begin{bmatrix} 5 \\ 2 \\ 1 \end{bmatrix}
$$
### b) Escala de Sx=2 e Sy=3 em relação à origem
$$
\mathbf{p''} = \mathbf{S} \cdot \mathbf{p'} = \begin{bmatrix} 2 & 0 & 0 \\ 0 & 3 & 0 \\ 0 & 0 & 1 \end{bmatrix} \begin{bmatrix} 5 \\ 2 \\ 1 \end{bmatrix} = \begin{bmatrix} 10 \\ 6 \\ 1 \end{bmatrix}
$$
### c) Coordenada final após ambos
$$
\mathbf{M} = \mathbf{S} \cdot \mathbf{T} = \begin{bmatrix} 2 & 0 & 0 \\ 0 & 3 & 0 \\ 0 & 0 & 1 \end{bmatrix} \begin{bmatrix} 1 & 0 & 2 \\ 0 & 1 & -3 \\ 0 & 0 & 1 \end{bmatrix} = \begin{bmatrix} 2 & 0 & 4 \\ 0 & 3 & -9 \\ 0 & 0 & 1 \end{bmatrix}
$$

$$
\mathbf{p''} = \mathbf{M} \cdot \mathbf{p} = \begin{bmatrix} 2 & 0 & 4 \\ 0 & 3 & -9 \\ 0 & 0 & 1 \end{bmatrix} \begin{bmatrix} 3 \\ 5 \\ 1 \end{bmatrix} = \begin{bmatrix} 10 \\ 6 \\ 1 \end{bmatrix}
$$
O resultado de ambos é o mesmo..
## Questão 3:
### a) Coordenadas projetadas de P
$$X_p = \frac{X \cdot d}{Z} \qquad Y_p = \frac{Y \cdot d}{Z}$$

$$X_p = \frac{6 \cdot 5}{15} = \frac{30}{15} = 2 \qquad Y_p = \frac{4 \cdot 5}{15} = \frac{20}{15} = \frac{4}{3} \approx 1{,}33$$

$$\boxed{(X_p,\ Y_p) = \left(2,\ \tfrac{4}{3}\right)}$$
### b)Efeito do afastamento e fator de escala homogêneo
A medida que Z aumenta, w tende a 0 e o objeto projetado fica menor no plano de projeção, dando o efeito visual de perspectiva. Quando Z tende ao infinito, o ponto converge para um ponto de fuga.
### c) Projeção de Q=(6,4,30)Q = (6, 4, 30) Q=(6,4,30) e comparação
$$X_p = \frac{6 \cdot 5}{30} = 1 \qquad Y_p = \frac{4 \cdot 5}{30} = \frac{2}{3} \approx 0{,}67$$

$$\boxed{(X_p,\ Y_p) = \left(1,\ \tfrac{2}{3}\right)}$$
Q está ao dobro de distância de P e suas coordenadas projetadas são metade de P, o que demonstra a relação inversamente proporcional entre Z e o tamanho projetado.
## Questão 4:
### a) Siglas e funções de cada sistema
#### SRO - Sistema de Referência do Objeto
Espaço local de cada objeto 3D. As coordenadas são em relação ao próprio objeto. É onde os modelos são criados.
#### SRU - Sistema de Referência do Universo
Espaço global da cena. Todos os objetos são posicionados nesse sistema após suas transformações. Sistema compartilhado por todos os objetos.
#### SRN - Sistema de Referência Normalizado
Espaço intermediário onde as coordenadas são normalizadas em um intervalo padrão. Remove a dependência do volume de visão específico da câmera.
#### SRD - Sistema de Referência do Dispositivo
Espaço final em pixels da tela. As coordenadas normalizadas são mapeadas para a resolução real do dispositivo de saída.
### b) Etapa do recorte (clipping)
O clipping normalmente ocorre entre o SRU e SRN, mas pode ocorrer entre SRN e SRD dependendo da aplicação, já que nessa etapa o volume de visão já está definido e os objetos ou triângulos fora do volume são descartados ou cortados nos seus limites antes de serem projetados na tela, evitando processamento desnecessário e artefatos visuais.
### c) Projeção paralela ortográfica vs. projeção oblíqua cavaleira
#### Projeção paralela ortográfica:
Os raios de projeção são perpendiculares ao plano de projeção. Não há perspectiva. Objetos do mesmo tamanho aparecem iguais independente da profundidade. Preserva medidas e ângulos retos.

- Uso: CAD, plantas arquitetônicas, engenharia, modelagem técnica.
#### Projeção oblíqua cavaleira:
Os raios de projeção são oblíquos ao plano de projeção. A face frontal é desenhada sem distorção, e a profundidade é representada por linhas em ângulo (geralmente 45°) com fator de escala =1(cavaleira) ou = 0,5 (cabinet).

- Uso: ilustrações técnicas, desenho manual, diagramas didáticos onde se quer mostrar a face frontal sem deformação.