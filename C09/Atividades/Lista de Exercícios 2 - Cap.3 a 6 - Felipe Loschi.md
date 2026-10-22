## 1. Explique a diferença entre o modelo RGB e o modelo CMY, citando um exemplo de dispositivo que utiliza cada um deles.
O RGB é baseado na ideia de mistura de luzes, sendo o resultado de uma mistura sempre mais brilhante que os componentes individuais, usado em monitores, telas de smartphones, etc. Já o CMY é baseado na ideia de mistura de pigmentos, onde os pigmentos absorvem alguns comprimentos de luz e emitem outros, exemplos são os vários tipos de impressoras.
## 2. Dado o valor RGB = (56, 138, 214) calcule os valores correspondentes em CMY.
RBG(56, 138, 214) -> Faixa não normalizada, portanto, 255
$\begin{bmatrix} C \\ M \\ Y \end{bmatrix} = \begin{bmatrix} 255 \\ 255 \\ 255 \end{bmatrix} - \begin{bmatrix} R \\ G \\ B \end{bmatrix}$

$\begin{bmatrix} C \\ M \\ Y \end{bmatrix} = \begin{bmatrix} 255 \\ 255 \\ 255 \end{bmatrix} - \begin{bmatrix} 56 \\ 138 \\ 214 \end{bmatrix}$

$\begin{bmatrix} C \\ M \\ Y \end{bmatrix} = \begin{bmatrix} 199 \\ 117 \\ 41 \end{bmatrix}$

## 3.  O modelo HSV é considerado orientado ao usuário. Explique o que representam cada uma das três componentes H, S e V, e por que esse modelo é mais intuitivo para um artista ou designer do que o modelo RGB.
- H: Hue, ou matiz, é a cor propriamente dita, expresse em um ângulo de 0° a 360°.
- S: Saturation, ou saturação, é a vivacidade da cor, variando de 0%, cinza, a 100%, cor pura.
- V: Value, ou valor, é o brilho da cor, variando de 0%, preto, a 100%, brilho máximo.
- Esse modelo é mais intuitivo para humanos pois é usado em forma de um seletor nos softwares, podendo escolher o valor de cada um pelo ângulo e porcentagem, o que o torna intuitivo ao olho humano.
## 4. Explique os três níveis de continuidade estudados (C⁰, C¹ e C²) e descreva o que diferencia cada um deles no ponto de junção entre dois segmentos de curva.
- $C^0$: Continuidade de ordem 0, onde as curvas se encontram em um ponto, mas podem representar uma quina ou mudança de direção. Garante que não há descontinuidade.
- $C^1$: Continuidade de ordem 1, onde as curvas se encontram em um ponto e a derivada primeira é igual. Garante que não há mudança abrupta de direção.
- $C^2$: Continuidade de ordem 2, onde a derivada segunda também é contínua. Garante que há uma transição mais suave e sem variações bruscas nas curvas.
## 5. Qual a diferença entre a representação analítica não paramétrica e a representação analítica paramétrica de uma curva? Dê um exemplo de cada caso.
A representação paramétrica utiliza um parâmetro θpara definir as coordenadas dos pontos na curva, sendo cada coordenada expressa como uma função independente desse parâmetro. Um exemplo é a equação de um quarto de círculo de um raio qualquer.
Na não paramétrica, uma coordenada é função de outra, sendo dividida em:
- Forma Explícita: um único valor de X para um único valor de Y. Exemplo: $Y = X$.
- Forma Implícita: cada valor de variável pode gerar mais de um valor para outra. Exemplo: $Y^2 - X^2 + r^2 =0$.
## 6. Compare as curvas de Hermite e Bézier
Para gerar uma curva de Hermite é necessário de dois pontos, inicial e final, e dois vetores tangente a esses dois pontos. Já em Bézier, que se baseou nas ideias de Hermite, usa-se pontos de controle para controlar a forma da curva ao invés das tangentes. Bézier define a curva passando pelo primeiro e último ponto de controle e sendo tangente ao primeiro e último segmento do polígono de controle.
## 7. Explique o conceito de superfície de revolução e o de sweeping), indicando de que forma um é um caso particular do outro.
Superfícies de Revolução são obtidas rotacionando uma curva plana em torno de um eixo. Já o Sweeping consiste em gerar uma superfície através do movimento de uma curva ou figura plano ao longo de um caminho. A Superfície de Revolução é considerada um caso particular de Sweeping por podermos considerar que o caminho é em torno de um eixo.
## 8. Explique o princípio da persistência da visão e como ele fundamenta a animação.
A persistência da visão é o fenômeno fisiológico que faz com que o cérebro retenha por frações de segundo a imagem captada pela retina. Ele fundamenta a animação pois permite que uma sequência rápida de imagens estáticas seja percebida como movimento contínuo.
## 9.  Explique as técnicas Straight Ahead e Pose-to-Pose, destacando em quais situações cada uma é mais indicada.
- Straight Ahead: Ideal para cenas que pedem espontaneidade e descontração, pois, nesse estilo, o animador tem que desenhar todos os quadros da animação, do quadro inicial e avançando cronologicamente. Isso permite que novas ideias sejam incorporadas conforme a sequência se desenvolve.
- Pose-to-Pose: Ideal quando a posição e o tempo são elementos importantes da cena, pois, nesse estilo, o animador primeiro define apenas quadros chave e depois desenha os intermediários. Vantagem de que o animador tem uma visão clara da estrutura geral do movimento antes de preencher os detalhes.
## 10. A animação por computador divide-se em duas grandes categorias. Explique a diferença entre Computer-Assisted Animation e Computer-Generated Animation.
- Computer-Assisted Animation: Nesse estilo, o animador se preocupa com os quadros-chave e o computador produz os quadros intermediários.
- Computer-Generated Animation: Nesse estilo, temos um grupo de técnicas que podem ser divididas em técnicas de baixo nível, onde o computador auxilia na especificação precisa do movimento, e técnicas de alto nível, onde o computador descreve o comportamento do personagem durante a animação.
## 11. O que é o canal alpha em uma imagem de 32 bits? Descreva e explique o que é, e como isso se conecta com a técnica de chroma key.
O canal alpha é a parte do pixel que é reservada para armazenar informações sobre a transparência. Em imagens de 32 bits, o canal alpha é um dos 4 canais e possui 8 bits para si. O canal alpha é importante para o chroma key pois após a remoção da cor de fundo definida como chave, um canal alpha é criado automaticamente, definindo quais áreas são transparentes e quais são opacas.
## 12. Cite os quatro tipos de sistemas de captura de movimento estudados e, para cada um, indique sua principal vantagem e sua principal desvantagem.
### Ótico
- Principal vantagem: Liberdade de movimento para o ator, uma vez que não há cabos ao redor do corpo. 
- Principal desvantagem: Possibilidade de oclusão, já que o próprio corpo do ator pode impedir a visibilidade das bolas para algumas câmeras. Esse problema pode ser mitigado aumentando o número de câmeras, mas é uma solução custosa.
### Mecânico
- Principal vantagem: Transforma os movimentos rotacionais em dados digitais em tempo real, não tendo o problema da obstrução de visão das câmeras.
- Principal desvantagem: Aparelhagem no corpo do ator pode ser pesada e acabar obstruindo os movimentos do mesmo.
### Magnético
- Principal vantagem: Não é suscetível a sobreposição de marcadores e não há problemas de oclusão.
- Principal desvantagem: Necessidade de vários cabos fixados ao corpo do ator, que também pode obstruir os movimentos. Além disso, objetos metálicos na área podem causar interferências nos dados magnéticos
### Acústico
- Principal vantagem: Mesmo do magnético, não suscetível a sobreposição de marcadores e não há problemas de oclusão
- Principal desvantagem: Mesmo do magnético na necessidade de cabos fixados ao corpo do ator.
## 13. Explique o que é o problema de visibilidade (hidden surface problem) em computação gráfica. Cite as quatro ramificações desse problema na pipeline gráfica e descreva brevemente cada uma.
O problema de visibilidade vem de determinar quais superfícies são visíveis a partir de um dado ponto de visibilidade já que diversos objetos se sobrepõem e nem todas suas faces podem ser vistas ao mesmo tempo.
### Ramificações
- Culling: Descartar objetos que não podem ser vistos de forma alguma
- Clipping: Recortar objetos para manter apenas as partes dentro do volume de visualização
- Desenho de partes visíveis: renderizar apenas o que é efetivamente visível
- Sombras: Superfícies não "vistas" pela luz ficam em sombra
## 14. Compare o Algoritmo do Pintor e o Algoritmo Reverso do Pintor
### Algoritmo do Pintor
- Renderiza todos os polígonos da cena em ordem do mais distante para o mais próximo.
- Vantagem: Não necessita de uma máscara auxiliar de pixels já pintados
- Desvantagem: Um mesmo pixel pode ser pintado múltiplas vezes(overdraw) quando o algoritmo for pintar os polígonos mas próximos
### Algoritmo Reverso do Pintor
- Inverte a lógica, pinta primeiro os mais próximos e depois os mais distantes. Faz uso de uma máscara para delimitar as porções que já foram pintadas.
- Vantagem: Cada pixel é pintado apenas uma vez, acabando com o overdraw
- Desvantagem: A máscara pode tornar um polígono simples em um polígono complexo, com componentes conexas e "buracos".
## 15. Descreva o funcionamento do Z-Buffer, explicando como ele é inicializado e qual teste é realizado para cada pixel durante a rasterização. Em seguida, explique o que é o artefato visual conhecido como Z-Fighting (Stitching) e cite duas formas de mitigá-lo.
O Z-Buffer é inicializado com o valor de cor da profundidade máxima. Durante a rasterização de cada polígono, para cada pixel, ele faz um teste de profundidade, se a profundidade do novo pixel for menor que o valor registrado no z-buffer, o pixel é pintado e o z-buffer é atualizado com o novo valor, caso contrário, o pixel é ignorado.
O Z-Fighting é o artefato visual que ocorre quando duas ou mais primitivas possuem o mesmo valor de profundida, ou valores muito próximos, que faz com que os pixels afetados sejam renderizados alternadamente com fragmentos de um polígono ou do outro, de forma aleatória. Uma solução é usar um Z-Buffer com um maior número de bits, o que aumentaria a precisão, e outra seria aplicar um offset de profundade entre as superfícies coplanares.
## 16. O Algoritmo de Warnock utiliza o conceito de coerência de área. Explique o princípio de funcionamento desse algoritmo, indicando as três condições em que ele resolve uma sub-região diretamente (sem subdivisão) e qual é o caso base da recursão.
O algoritmo de Warnock pinta uma região se ele satisfizer alguma das seguintes condições:
- Um polígono cobre a região totalmente e, em toda a região, é o mais próximo da câmera.
- Nenhum polígono intercepta a região(pinta-se a cor de fundo)
- Apenas um polígono intercepta a região(pinta-se o fundo e depois o polígono).
O caso base da recursão é quando a sub-região se reduz a um único pixel, nesse caso pinta-se a cor do polígono com menor profundidade no ponto.
## 17. Cite os quatro componentes fundamentais de uma fonte de luz em uma cena 3D e explique brevemente o que cada um representa. 
- Intensidade: Quantidade de luz emitida pela fonte
- Direção: Ângulo e orientação dos raios de luz emitido pela fonte
- Cor: Comprimento de onda da luz emitida pela fonte
- Tamanho: Área da fonte de luz, que influência a suavidade das sombras
## 18. Complete a tabela abaixo com as informações corretas
| Tipo de Luz    | Tipo de Emissão                                                                                                                                                                       | Uso Típico                                                                                                                           |
| -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| Spot Light     | Fonte de luz muito direta e direcional, emitida através de um cone, cujo ângulo de abertura determina a extensão da área efetivamente iluminada.                                      | Holofotes. Configuração de três pontos de iluminação.                                                                                |
| Luz Pontual    | Emite luz em todas as direções através de um único ponto.                                                                                                                             | Usado quando se deseja iluminar áreas com um gradiente suave em todas as direções, como lâmpada, vela ou tocha.                      |
| Luz Direcional | Imita a iluminação do sol. Seus raios são paralelos seguem uma direção única e se estendem até o infinito.                                                                            | Ideal para iluminar cidades, grandes espaços abertos e ambientes externos em geral.                                                  |
| Luz Ambiente   | Luz presente em toda a cena que não provém de nenhum objeto fonte específico. Ilumina todas as superfícies de maneira uniforme, independentemente de direção, distância ou obstrução. | Importante para o aspecto geral e o brilho de uma cena. Também utilizada para criar efeitos de iluminação estilizados e cartunescos. |
## 19. Explique por que iluminar um rosto apenas com luz vinda de todas as direções igualmente resulta em perda de profundidade. Em seguida, dê um exemplo de como a direção da luz pode mudar o humor de uma cena.
Pois se a luz viesse de todas as direções igualmente, o que seria visto seria apenas o contorno bidimensional da face, já que não haveria sombra que pudesse dar a profundidade aos detalhes tridimensionais. 
A direção da fonte de luz também influência no humor da cena por poder produzir diferentes efeitos dependendo de sua posição. Por exemplo, uma fonte de luz vinda de baixo pode causar um efeito dramático a cena.

## 20. O que é rendering no contexto da computação gráfica? Explique por que sintetizar uma imagem é diferente de simplesmente exibi-la digitalmente, e quais são os quatro elementos fundamentais que compõem uma cena sintetizada.
Rendering é o processo de converter dados de um modelo tridimensional em uma imagem realística. Sintetizar uma imagem é diferente de apenas exibi-la pois precisamos fazer com que a cena deixe de parecer um simples conjunto de formas geométricas e passe a se assemelhar com uma representação visual convincente do mundo real. Os quatro elementos que compõem uma cena são a geometria da cena, informações sobre os materiais e os objetos, funções de iluminação e a posição de observação.
## 21. O processo de realismo visual é composto por 7 fases. Descreva resumidamente o que ocorre em cada uma delas, na ordem correta.
### Fase 1: 
Construção do modelo, que consiste na construção do modelo 3D que irá conter as informações necessárias para o processo de renderização.
### Fase 2: 
Projeção e perspectiva, onde transformações lineares são aplicadas ao modelo para que ele tenha aparência tridimensional nos dispositivos de visualização, que são geralmente em 2D.
### Fase 3:
Eliminação de fases ocultas, onde polígonos e/ou faces escondidas do observador são retiradas de cena.
### Fase 4:
Recorte, onde é definido um volume de visualização e eliminado tudo que está fora desse volume.
### Fase 5:
Rasterização, Converte a representação tridimensional em pixels, onde ocorre a transição do domínio contínuo para o domínio discreto.
### Fase 6:
Determinação de superfícies visíveis, onde, diferente da fase 3, aqui é usado as coordenadas do dispositivo onde será visualizado, determinando quais superfícies são visíveis pixel a pixel.
### Fase 7:
Sombreamento e colorização, onde é colorido cada pixel individualmente, utilizando um esquema incremental ou interpolador de sombreamento.
## 22. Explique o que é o realismo por passadas e cite quatro tipos de passadas diferentes, descrevendo o que cada uma adiciona à imagem final.
O realismo por passadas é o processo incremental de construir uma cena realística, tanto o nível conceitual quanto no nível das técnicas e softwares disponíveis.
### Passada de Cores:
Momento em que se atribuem cores aos objetos. Inclui o modelo geométrico, a iluminação ambiente(uniforme e sem direção definida) e o mapa de cores(texturas difusas).
### Passada de Brilho:
Inclui a luminosidade direcional, o brilho e as ênfases da cena. Considera os pontos de luz intensa que aparecem quando a superfície reflete a fonte de luz diretamente na direção do observador.
### Passada de Iluminação:
Inclui os pontos de luz e suas interações com a cena. Mostra a influência de cada luz individualmente.
### Passada de Sombras:
Inclui as sombras projetadas pelos objetos, mostrando sua localização no solo e nos outros objetos da cena. Usa técnicas como Shadow Mapping e Shadow Volumes para gerar sombras em tempo real.
## 23. Explique a diferença entre a renderização fotorrealista tradicional e o NPR (Non-Photorealistic Rendering). O que é o Toon Shading e em quais contextos ele é especialmente útil?
A renderização fotorrealista é sobre o uso das técnicas como passadas e fases para buscar o realismo fotográfico, já os acabamentos não-fotográficos(NPR), se resume em buscar a clareza de comunicação, não em ser realista, como em design de produtos e ilustrações técnicas.
O Toon Shading é uma técnica que simula a aparência de desenhos animados, com sombreamento em faixas discretas de cor e contornos marcados ao redor dos objetos. É especialmente usado pela sua capacidade de comunicar emoções de forma clara e direta.
## 24. O que é hiper-realismo no contexto da computação gráfica? Explique por que muitas de suas técnicas não estão disponíveis nativamente nos motores de renderização padrão e em quais passadas do processo de realismo visual elas são geralmente aplicadas.
O hiper-realismo se resume a um conjunto de técnicas e efeitos que vão além da renderização padrão, com o objetivo de produzir imagens que se aproximem ou até superem a qualidade fotográfica. Essas técnicas não são disponíveis nativamente devido ao seu custo computacional, onde uma única cena pode levar horas para ser renderizada.
## 25. Explique o que são as imagens HDRI (High Dynamic Range Images) e qual problema elas resolvem na renderização de cenários. Em seguida, descreva o efeito de atenuação atmosférica e qual fenômeno físico ele simula.
O problema que é resolvido é a falta de interação entre objetos e o fundo da cena devido a ambos não serem modelados individualmente para não sobrecarregar desnecessariamente o software e o hardware, o que tornaria o processo lento e travado. O HDRI, solução desse problema, corrige esse problema ao incluir na imagem informações de intensidade que ultrapassam o intervalo convencional de 0.0 a 1.0(0 a 255), podendo chegar a 100.0 ou mais, preservando a gama de luminosidade real da cena capturada.
A atenuação atmosférica é o fenômeno em que objetos mais distantes do observador parecem progressivamente mais foscos, esbranquiçados e com menos contraste. Ele ocorre por causa de materiais presente na atmosfera, como poeira, vapor d'agua ou fumaça. Em computação gráfica, ela é frequentemente implementada através de técnicas como fog(neblina), haze(névoa) e aerial perspective(perspectiva aérea). 
## 26. Descreva cada um dos três efeitos abaixo, explicando o fenômeno físico real que cada um simula e como a computação gráfica o reproduz 
### Depth of Field(DoF):
Ao tirar uma foto ou gravar um vídeo de um objeto alvo é necessário ajustar a câmera e com esse ajuste, objetos que estão em outras profundidas aparecem borrados. A faixa de distâncias que permanece nítida é chamada de profundidade de campo. É controlada principalmente pela abertura do diafragma, a distância focal da lente e a distância entre a câmera e o objeto. 

O efeito de DoF simula esse comportamento óptico em 3D. Recurso útil para inteligibilidade visual em uma cena, direcionando a atenção do espectador para o elemento principal. Os pontos fora de foco produzem os chamados bokeh - círculos ou formas luminosas que aparecem nas áreas desfocadas, cuja forma depende do número de lâminas do diafragma da lente..
### Motion Blur
Ocorre quando fotografamos um objeto em movimento, observamos que ele aparece desfocado e embaçado em relação aos objetos estáticos. No processo físico, o desfoque por movimento ocorre em consequência do tempo de exposição do sensor (ou filme) à luz: durante o período em que o obturador permanece aberto, o objeto muda de posição, e essa mudança fica registrada como um "rastro" na imagem.

Na computação gráfica, os sistemas de renderização tentam simular esse efeito calculando a posição dos objetos nos quadros anteriores e posteriores misturando todas essas diferentes posições em um único quadro. Essencial para animações jogos que buscam realismo cinematográfico, pois sem ele, objetos em alta velocidade parecem "saltar" entre posições.
### Film Grain
Recria o efeito granulado característico das películas cinematográficas analógicas. Esse ruído é causado pelos cristais de haleto de prata presentes na emulsão do filme fotográfico: quanto maior a sensibilidade do filme, maiores e mais visíveis esses grãos.

Pouco utilizado pela maioria dos usuários de computação gráfica, o film grain é considerado um dos efeitos mais importantes para alcançar o fotorrealismo, pois elimina o visual "limpo demais" e artificialmente perfeito de imagens geradas por computador.
## 27. O efeito de Sub-Surface Light Scattering utiliza duas funções matemáticas distintas para descrever o comportamento da luz em materiais translúcidos. Explique a diferença entre BRDF e BSSRDF, e dê dois exemplos de materiais ou situações onde o Sub-Surface Light Scattering é aplicado.
O BRDF se diferencia do BSSRDF em como eles descrevem a forma como a luz entra e sai. No primeiro, a luz é refletida em um ponto da superfície e se assume que o raio de luz entra e sai do material no mesmo ponto, o que é adequado para materiais opacos. O segundo descreve esse movimento com mais precisão, de forma que a luz entra em um ponto e sai em outro, modelando o espalhamento interno, sendo necessário para materiais translúcidos como pele, mármore, cera e leite.

