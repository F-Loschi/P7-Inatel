Felipe Silva Loschi
GES - 601
## Questão 1:
### a) RGB vs. CMYK
- RGB(Red, Green, Blue) é um modelo aditivo: começa no preto e adiciona luz. Usado em dispositivos emissores de luz, como monitores, TVs, projetores. Quanto mais cor, mais claro fica. O máximo das três resulta em branco.

- CMYK(Cyan, Magenta, Yellow, Black) é um modelo subtrativo: começa no branco e subtrai luz com pigmentos. Usado em impressão. Quanto mais tinta, mais escuro fica. O máximo das três resulta teoricamente em preto (na prática, um marrom escuro, por isso o K existe).
A distinção existe porque luz e tinta se comportam de forma oposta: telas emitem fótons, impressoras absorvem fótons com pigmento.
### b) HSV
- H(Matiz / Hue): a cor em si, representado por um ângulo de 0° a 360° no círculo cromático. 
- S(Saturação): a pureza da cor. 0% = cinza puro, 100% = cor totalmente vívida.
- V(Valor / Brilho): a luminosidade. 0% = preto, 100% = cor no máximo brilho.
Variando S de 0% a 100% com H e V fixos: a cor parte de um cinza neutro e vai gradualmente ganhando vivacidade até atingir a cor pura e saturada.
### c) Conversão RGB → CMYK e diferença visual na impressão
$$\begin{bmatrix} C \\ M \\ Y \end{bmatrix} = \begin{bmatrix} 255 \\ 255 \\ 255 \end{bmatrix} - \begin{bmatrix} 255 \\ 128 \\ 0 \end{bmatrix} = \begin{bmatrix} 0 \\ 127 \\ 255 \end{bmatrix}$$
A cor pode parecer visualmente diferente por algumas razões:
- CMYK reproduz uma gama de cores menor que RGB. 
- Tintas reais não absorvem luz de forma ideal. M + Y na impressão raramente produz o mesmo laranja que R=255, G=128, B=0 na tela.
- O papel absorve tinta e afeta a cor final; a tela emite luz própria.
- Sem gerenciamento de cor, a conversão é apenas matemática e ignora as características físicas da impressora.
## Questão 2:
### a) Hermite vs. Bézier
- Curva de Hermite: Definida por dois pontos de extremidade e dois vetores tangentes. A entrada são os próprios vetores tangentes, o que dá controle direto sobre a direção e "velocidade" da curva nos extremos.
- Curva de Bézier: Definida por pontos de controle (incluindo os extremos). A curva passa pelos pontos inicial e final, mas é apenas atraída pelos pontos intermediários. A entrada é o conjunto de pontos de controle e as tangentes são implícitas pela posição deles.
### b) Pontos de controle em Bézier
Os pontos de controle são pontos no espaço que atraem a curva sem que ela necessariamente passe por eles. Ao mover um ponto de controle intermediário toda a curva se deforma suavemente em direção ao novo ponto. Isso é uma limitante da Bézier clássica, pois, não há controle local, qualquer alteração afeta a curva inteira.
### c) Superfícies B-spline na indústria
Aplicação: Design de carrocerias automotivas (ex: capô, portas, para-lamas).

As superfícies B-spline são preferidas em relação a malhas poligonais nesse contexto por causa do controle local, da suavidade garantida pela continuidade matemática C² ou superior, pela representação compacta e pela precisão para manufatura. Malhas poligonais exigem altíssima densidade de vértices para simular a mesma suavidade, tornando-as impraticáveis para design de superfícies de classe A na indústria.
## Questão 3:
### a) Componentes do modelo de iluminação local
- Ambiente: Simula a luz indireta que chega de todas as direções, como reflexos, bounces, luz espalhada pelo ambiente. É uma constante aplicada uniformemente ao objeto, sem considerar posição de luz ou câmera. Evita que áreas não iluminadas fiquem completamente pretas.

- Difusa: Simula superfícies rugosas/opacas que espalham a luz igualmente em todas as direções. Depende do ângulo entre a normal da superfície e a direção da luz. Responsável pelo sombreamento suave que revela o volume do objeto.

- Especular: Simula reflexos brilhantes de superfícies lisas, como plástico, metal, vidro. Depende do ângulo entre o vetor de reflexão e o vetor da câmera, elevado ao expoente de brilho n. Quanto maior n, menor e mais concentrado o reflexo.
### b) Flat vs. Gouraud vs. Phong Shading
- Flat Shading: A cor é calculada uma vez por polígono, usando a normal da face. Todos os pixels do polígono recebem a mesma cor. Resultado: aparência facetada, sem suavidade. Muito rápido, usado em tempo real com baixo custo.

* Gouraud Shading: A iluminação é calculada nos vértices do polígono usando as normais de cada vértice. A cor dos pixels internos é obtida por interpolação bilinear das cores dos vértices. Resultado: transições suaves, mas reflexos especulares podem desaparecer ou ficar distorcidos se o pico especular estiver no interior do polígono.

* Phong Shading: As normais são interpoladas dos vértices para cada pixel, e o cálculo de iluminação completo é feito por pixel. Resultado: reflexos especulares precisos e suaves em qualquer posição do polígono. Melhor qualidade visual, maior custo computacional.

O Phong Shading apresenta o melhor resultado visual.
### c) Diagnóstico do problema da esfera
O artista provavelmente está usando Gouraud Shading, já que no Gouraud, a iluminação é calculada apenas nos vértices e interpolada linearmente entre eles. Se o pico do reflexo especular cair no interior de um polígono (longe dos vértices), ele não é capturado corretamente, resultando em bordas "quadradas" e reflexos pouco suaves, exatamente o sintoma descrito.

Ele deveria adotar Phong Shading, que interpola as normais e recalcula a iluminação por pixel. Isso garante que o reflexo especular seja calculado com precisão em qualquer ponto da superfície, produzindo o brilho suave e arredondado esperado em uma esfera.
## Questão 4:
### a) Algoritmo Z-Buffer
 Z-buffer armazena a profundidade z do fragmento mais próximo já processado em cada pixel. Para cada fragmento gerado:

$$\text{se } z_{fragmento} < z_{buffer}[x][y] \Rightarrow \text{atualiza cor e profundidade}$$
$$\text{senão} \Rightarrow \text{descarta o fragmento}$$

Ao final, apenas o fragmento mais próximo da câmera em cada pixel permanece. a principal vantagem é a simplicidade de implementação e compatibilidade com pipeline paralelo em GPU. A principal desvantagem é que a transparência é difícil de tratar corretamente, pois o algoritmo só mantém um fragmento por pixel. Objetos translúcidos exigem ordenação ou técnicas adicionais.
### b) Ray Tracing vs. Rasterização
- Ray Tracing: para cada pixel da tela é lançado um raio a partir da câmera. Esse raio testa interseção com todos os objetos da cena e, ao acertar uma superfície, lança raios secundários (sombra, reflexo, refração) recursivamente.
- Rasterização convencional: cada polígono é projetado na tela e seus pixels são preenchidos, é um processo objeto → pixel, local e sem visão global da cena.

Efeitos naturais no Ray Tracing difíceis de obter com rasterização:
- Reflexos e refrações: o raio simplesmente continua pela superfície espelhada ou transparente
- Sombras suaves: raios de sombra testam oclusão diretamente em relação à fonte de luz
### c) Mapeamento de textura vs. Normal Mapping
- Mapeamento de textura: Aplica uma imagem 2D à superfície do objeto, associando coordenadas UV de cada vértice a pixels da textura. Adiciona cor e detalhes visuais, mas não altera a geometria nem as normais, a silhueta e o sombreamento continuam revelando a malha real.
- Normal Mapping: Armazena em uma textura (mapa de normais, em espaço tangente) vetores normais perturbados para cada texel. Durante o shading, a normal real da superfície é substituída pela normal lida do mapa antes do cálculo de iluminação.

O efeito é que a luz interage com a superfície como se ela tivesse relevos e detalhes geométricos reais, como saliências, rachaduras, rebaixos, sem que nenhum polígono extra seja adicionado à malha. A ilusão se mantém enquanto o ângulo de visão não revelar a silhueta plana. É amplamente usado em jogos para simular detalhes de alta resolução em malhas de baixo custo computacional.