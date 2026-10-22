# Parte 1: Visibilidade
## Problema de Visibilidade
- Culling: descartar objetos que não podem ser vistos de forma alguma
- Clipping: Recortar objetos para manter apenas as partes dentro do volume de visualização
- Desenho de partes visíveis: Renderizar apenas o que é efetivamente visível, seja em modo aramado ou em superfícies preenchidas
- Sombras: visibilidade é tratada do ponto de vista das fontes de luz
## Algoritmos de visibilidade
- Eficiência de pixel: pintar apenas as superfícies visíveis, evitando repintar pixels desnecessariamente
- Tempo mínimo: renderizar a cena o mais rápido possível
- Coerência temporal: a cena é estática ou dinâmica? Objetos se movem em quadros?
- Qualidade visual: técnicas como antialiasing são necessárias?
- Software vs. hardware: o algoritmo pode ser acelerado por GPU?
## Complexidade do problema
- Número de Pixels: minimizar pixels pintados
- Número de objetos
- Classificação dos Algoritmos
	- Espaço do objeto
	- Espaço da imagem
## Algoritmo do Pintor
Depth priority. Conhecido como prioridade em Z, inspirado na técnica que um pintor real usa ao criar uma pintura a óleo.
### Características e limitações
- Ordenação em Z
- Limitações: Que ponto usar para determinar a ordem? Projeções que não se interceptam não precisam de ordem total.
- Vantagem: Não necessita de uma máscara auxiliar de pixels já pintados
- Desvantagem: um mesmo pixel pode ser pintado múltiplas vezes, desperdiçando processamento
## Pintor Reverso
Lógica inversa: polígonos são pintados de frente pra trás
### Características
- Vantagem principal: cada pixel é pintado somente uma vez- elimina completamento o overdraw
- Desvantagem: máscara pode se tornar um polígono genérico bastante complexo, com diversas componentes conexas e "buracos"
## Z-Buffer
Método no espaço da imagem - teste de profundida por pixel. Ao renderizar, as coisas, ele testa para ver qual forma está mais próxima, e será essa que será renderizada. Usado na maior parte dos jogos. 
### Vantagens
Simples e implementado em software, objetos desenhados em qualquer ordem. 
### Desvantagem
Problema é que é lento com muitos polígonos, possui erros de quantização e dificulta a transparência e técnicas de antialising.
## Z-Fighting(Stitching)
Problema visual que ocorre quando duas ou mais primitivas possuem valores de profundidade muito próximos(ou iguais) no z-buffer.
## A-Buffer
Evolução do z-buffer que resolve as principais limitações. Permite a implementação correta de transparência e de filtragem, armazenando informações mais ricas sobre cada pixel
# Parte 2: Iluminação
Iluminar tem a função de trazer para frente ou empurrar para trás as formas dos objetos visíveis do ponto de vista da câmera.
Iluminação confere emoção e caráter, além da ilusão de profundidade.
## Componentes e Propriedade
Formam a "qualidade da luz":
- Intensidade: Quantidade de energia luminosa emitida por uma fonte
- Direção: influência em como você vai perceber a profundida e forma dos objetos.
- Cor : depende da fonte emissora
	- Objeto branco: toda luz é refletida
	- Objeto preto: toda luz é absorvida e nada é refletido
	- Cor específica: absorve todos comprimentos de onda, exceto o seu.
	- Cores transmitem relações espaciais e temporais, além de transmitirem emoções.
	- ![[Pasted image 20260319142033.png]]
- Tamanho: Afeta sensação geral da cena
	- Fonte pequena: sombras nítidas = tensão
	- Fonte grande: sombras suaves = relaxamento
## Tipos de Luz
Diversos paradigmas bem estabelecidos, uso depende do cenário.
### Spot Light(Holofote)
Emitido através de um cone, cujo ângulo de abertura determina a extensão da área efetivamente iluminada. Dentro do cone há luz e fora não.
### Luz Pontual(Point Light)
Lâmpada incandescente, emite luz em todas as direções a partir de um único ponto. Objetos mais próximos recebem mais luz e os mais longe recebem menos.

### Área de Luz
Raios de luz emitidos dentro de um limite físico Emitida a partir de uma área, não de um ponto, diferente de spot light e luzes pontuais. Perfeito para recriar janelas.
![[Pasted image 20260319143201.png]]
### Luz Direcional
Imita a iluminação do sol. Raios paralelo, seguem em uma única direção e se estendem ao infinito. Ideal para iluminar cidades, grandes espaços abertos e ambientes externos em geral.
![[Pasted image 20260319143454.png]]
### Materiais Emissivos
Emitem luz em toda superfície. Propriedade do material. Ressaltar a iluminação não-uniforme e uma cena.
![[Pasted image 20260319143630.png]]
### Luz Ambiente
Presente em toda a cena que não provém de nenhum objeto fonte específico. Contribui para aspecto geral e brilho da cena. Cria efeitos de iluminação estilizados e cartunescos.
# Parte 3: Renderização
## Introdução
- Síntese de imagens diferente do processamento de imagens
- Trata de geometria, materiais, iluminação, observador
- Conversão de dados em imagem
## Fases do Processo de Realismo Visual
### Modelagem
- Construção de modelo com todas as informações necessárias
### Projeção
- Aplicação de transformações lineares ao modelo para gerar aparências tridimensionais
### Backface Culling
- Eliminação de faces ocultas com base na posição relativa entre os objetos e o observador
### Clipping
- Descarte de das partes da cena fora do campo de visão do observador - como o que está atrás de paredes ou além do alcance visual - mesmo que esses elementos estejam descritos nos dados da cena
### Rasterização
- Converte a representação tridimensional em pixels para o dispositivo de exibição
### Remoção de superfícies ocultas
- Continuação da fase 3, porém operando em coordenadas do dispositivo(após a rasterização):
	- Técnicas: hidden-surface removal, visible-surface determination, occlusion culling
	- Diferença da parte 3: enquanto a fase 3 elimina faces inteiras usando coordenadas 3D, essa fase atua em coordenadas 2D da tela
### Sombreamento
- Coloração individual de cada pixel considerando todos os fatores de realismo da cena:
	- Iluminação: intensidade e direção das luzes em relação aos objetos
	- Superfícies: transparência, brilho, reflexão e textura
	- Sombras: projeção entre objetos e nas superfícies de apoio
## Realismo por passadas
Renderização por passadas é o padrão da computação gráfica: cada atributo da cena e renderizado separadamente, economizando memória e permitindo modificações pontuais sem refazer todo o processo.
### Diffuse Pass
### Highlight Pass/ Specular Pass(2a passada) 
Adição de luminosidade direcional e brilhos
### Reflection Pass(3a passada)
Adição de reflexos às superfícies da cena
### Light Pass(4a passada)
Renderização individual das fontes de luz e seus efeitos
### Shadow Pass(5a passada)
Renderização das sombras projetadas pelos objetos no solo e sobre outros elementos da cena
### FX Pass(6a passada)
Renderização separada dos efeitos especiais da cena
### Depth Pass(7a passada)
Adição artificial de profundidade à cena
## Acabamentos não fotográficos
Renderização estilizada como alternativa ao realismo fotográfico
- NPR aplicado - Toon shading: simplificação visual para destacar apenas o que é relevante
# Parte 4: Hiper-Realismo
Métodos avançados que elevam o realismo além do render padrão. 
## Atuam na parte da iluminação:
## HDRI
Imagens de fundo com informação de iluminação real:
- Problema: cenários distantes não são modelados par não sobrecarregar o sistema
- Solução: captura intensidade de luz reais que efetivamente iluminam a cena
- Pode eliminar a necessidade de iluminação extra 
## Atenuação Atmosférica(fog)
Simulação do efeito da atmosfera sobre objetos distantes(poeira, vapor, fumaça);
- Objetos mais distantes aparecem mais foscos
## Area Light + Soft Shadow
Simulação de fontes de luz com área, não pontual
- Luz emitida por uma superfície extensa(lâmpadas fluorescentes) gera sombras suaves que se dispersam com a distancia
- Sombreamento mais realista e convincente
- Simula o efeito de radiosidade e iluminação global sem o alto custo computacional
## Ambient Occlusion
Simulação do escurecimento natural de cantos, frestas e superfícies próximas - onde a luz ambiente tem dificuldade de chegar
- Quanto mais bloqueado o hemisfério acima de um ponto, menos luz ambiente chega até ele
- Atua no pós processamento - opera sobre o depth buffer, após a rasterização
## Sub-Surface Scattering
Simulação da translucidez de materiais
- A luz penetra e se dispersa dentro do material antes de sair, criando o efeito de  translúcido.
### BRDF
Assume que a luz entra e sai do material no mesmo ponto
### BSSRDF
Descreve com maior precisão o trajeto da luz dentro do material, capturando onde ela entre e onde ela sai
## Atuam no Pós-Processamento:
## Depth of Field(DoF)
Simulação do efeito de foco de câmera em cenas 3D
- Base Física: ao focar em um objeto, o fundo embaça
## Motion Blur
Simulação do desfoque causado por objetos em movimento
- Base física: desfoque ocorre pelo tempo de exposição do filme à luz durante o movimento
- Implementação: calcula posições do objeto ...
## Film Grain
Simulação do granulado característico de filmes fotográficos
- Efeito: adiciona ruído
## Lens Flare
Simula artefatos luminosos causados pela refração da luz nas lentes da câmera
## Glow
Adiciona aura luminosa ao redor