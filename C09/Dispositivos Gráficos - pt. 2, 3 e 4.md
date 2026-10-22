[[Dispositivos Gráficos - pt. 1]]
## Dispositivos de saída
### Impressoras
- Marcam a democratização da produção de documentos
- Surgiram para resolver limitações específicas: impacto mecânico ruidoso mas barato operacionalmente; jato de tinta oferecia qualidade fotográfica mas com custo por página alto; laser combinava velocidade com economia operacional mas investimento inicial significativo.
- Necessidade fundamental sempre foi **custo**
#### Impressora de Impacto - Matricial
- Primeira geração de impressão computadorizada
- Necessidade: computadores mainframe dos anos 1960-1980 geravam dados que precisavam ser materializados em papel para análise humana
- Muito ruidosa, custo operacional baixo
- Uso atual: notas fiscais, formulários múltiplas vias
#### Impressoras Térmicas
- Solução para o ruído
- Impressão desaparece em 2~5 anos
- Térmica direta:
	- Escurece papel térmico especial
	- Sem consumíveis, silenciosa
	- Desvantagem: desbota
	- Uso: recibos, tickets
- Transferência térmica:
	- Calor derrete tinta de ribbon para papel
	- Durável, resistente água/solventes
	- Uso: Etiquetas industriais, código de barras
- Sublimação:
	- Tinta sólida -> gás -> papel(sem fase líquida)
	- Tom contínuo(256 níveis), qualidade fotográfica perfeita
	- 4 passes(CMYO), 45~90s por foto
	- Uso: fotografia profissional, eventos
#### Jato de tinta(Inkjet)
+ Democratizou impressão fotográfica de qualidade
+ Necessidade:
	+ Computadores domésticos necessitavam de impressões domésticas
	+ Imprimir fotos de câmeras emergentes sem pagar laboratórios
+ Impressoras com vendidas com baixo lucro e cartuchos ficavam caros pra cacete
+ Térmica(HP, Canon):
	+ Bolha de vapor ejeta gota
	+ Resistor aquece 300°C em 2µs
	+ Gota: 1 - 5 picolitro(10 milhões x menor que chuva)
	+ Cabeça descartável com cartucho
+ Piezoelétrica:
	+ Cristal piezo deforma e ejeta gota
	+ Sem aquecimento, controle fino do tamanho da gota
	+ Cabeça permanente, aceita qualquer tipo de tinta
	+ Mais durável
+ Características gerais:
	+ Resolução: 300~600 DPI real
	+ Uso: Doméstico, fotografia, documentos coloridos
#### Laser:
* Democratização da produção de documentos de alta qualidade e volume
* Necessidade dos escritórios corporativos gerando volume massivo de documentos
* Investimento inicial alto mas justificado pro uso
* Princípio: Eltrofotografia(7 etapas)
	* Carregamento(corona wire)
	* Exposição(laser escreve no tambor fotossensível)
	* Revelação(toner adere a áreas descarregadas)
	* Transferência(toner vai para papel)
	* Fusão(calor 180~220°C funde toner)
	* Limpeza
	* Apagamento
* Características:
	* Velocidade alta
	* Custo por página baixo
	* Texto nítido, resistente à água
	* Uso: Escritórios, volume médio-alto
#### Plotters
- Necessidade especializada de imprimir documentos técnicos de grande formato
- Necessidade de imprimir algo impossível para canetas
- Qualidade justifica custo elevado
## Parte 3: Dispositivos de entrada
- Busca contínua por interfaces mais naturais e intuitivas entre humanos e computadores
### Dispositivos apontadores:
- Traduzir movimento espacial humano em coordenadas digitais para interfaces gráficas.
#### Mouse:
- Óptico: Sensor CMOS captura textura da superfície (1000-12000 fps)
- Laser: Infravermelho, funciona em vidro
- Trackball: Mouse invertido, esfera no topo
#### Touchpad:
- Capacitivo: Matriz de eletrodos detecta capacitância do dedo
- Multitouch: Gestos com 2-4 dedos
- Force Touch: Simula click mecânico via haptics
#### Stylus/Caneta digital:
- EMR (Wacom): Sem bateria, ressonância eletromagnética, 8192 níveis de pressão
- AES: Com bateria, funciona em tela capacitiva
- Apple Pencil: Capacitivo ativo, 9ms latência
#### Gamepad:
- Joysticks analógicos (potenciômetros ou Hall Effect)
- Triggers analógicos
- Giroscópio/Acelerômetro para motion controls
### Dispositivo de teclado:
- Não envia diretamente caracteres prontos, mas sim códigos de tecla, chamados de scancodes.
- Cada tecla pressionada e liberada produz um ou mais bytes que identificam exatamente qual tecla gerou o evento e qual foi a sua transição (pressão ou liberação).
### Scanners e Digitalizadores:
- Necessidade crítica de digitalizar o vasto corpus de documentos, fotos e desenhos físicos acumulados durante séculos de civilização analógica - transição para era digital exigia ponte para trazer conteúdo legado.
#### Scanner de Mesa:
- CCD: Sensor linear, óptica de redução, alta qualidade
- CIS: Sensor largo (1:1), fino, custo baixo
- Resolução: 300-1200 DPI óptico
#### Scanner 3D:
- Laser: Triangulação
- Structured Light: Padrões projetados
- ToF: Tempo de voo da luz
- Photogrammetry: Múltiplas fotos + software
### Câmeras Digitais:
- Eliminar fricção do filme: custo por foto (revelação), atraso (esperar revelação), irreversibilidade (foto ruim permanece ruim), e impossibilidade de compartilhamento instantâneo.
- Sensor:
	- CMOS domina (95%+): Baixo consumo, alta velocidade
	- Tamanhos: Full Frame > APS-C > Micro 4/3 > 1" > smartphone
- Smartphones:
	- Múltiplas câmeras (wide, ultra-wide, telephoto)
	- Computational photography (HDR, Night Mode, Portrait)
	- ISP processa em tempo real
### Sensores de Movimento:
- A necessidade que impulsionou miniaturização foi airbag automotivo (anos 1980-1990) - detectar desaceleração súbita de colisão requer acelerômetro confiável e barato o suficiente para colocar em todos carros.
- A necessidade fundamental é "context awareness" - dispositivos que sabem sua orientação, movimento, localização relativa podem adaptar comportamento apropriadamente, criando interfaces mais intuitivas e aplicações impossíveis com sensores ausentes.
#### IMU(Inertial Measurement Unit):
- Acelerômetro 3-axis: Mede aceleração linear
- Giroscópio 3-axis: Mede velocidade angular (rotação)
- Magnetômetro 3-axis: Detecta campo magnético (bússola)
- Sensor fusion: Combina dados para orientação 3D precisa

**Aplicações:** VR, drones, smartphones, robótica
### Sensores Biométricos
- Necessidade fundamental de autenticação conveniente e segura em era onde senhas tornaram-se insustentáveis
#### Impressão digital:
- Capacitivo: Array de capacitores (mais comum)
- Óptico: Luz refletida pelo prisma
- Ultrassônico: Ondas sonoras (3D, funciona molhado)
#### Reconhecimento facial:
- 2D: Câmera RGB (inseguro, foto engana)
- 3D Structured Light: 30.000 pontos IR (Apple Face ID)
- ToF: Depth map em tempo real
#### Iris Scanner:
- NIR camera captura textura da íris
- 240 degrees of freedom (mais seguro que digital)
### Interfaces Gestuais
- Busca por "next paradigm" além touch - controlar computadores com movimentos naturais do corpo, eliminando necessidade de tocar dispositivos físicos.
- **Leap Motion:** Rastreamento de mão (10 dedos, 200+ FPS)
- **Kinect:** Depth sensing para skeleton tracking (descontinuado)
- **RealSense:** Família de sensores depth (Intel)
## Dispositivos de processamento
- Responsáveis por transformar dados em representações visuais.
### GPU(Unidade de processamento gráfico)
- Ela executa operações matemáticas intensivas em paralelo para renderizar imagens, aplicar transformações geométricas, processar shaders e manipular texturas. Diferente da CPU, a GPU possui milhares de núcleos otimizados para cálculos matriciais e operações vetoriais simultâneas.
#### Características principais dos dispositivos de processamento:
- **Paralelismo massivo** — processam milhões de pixels e vértices simultaneamente
- **Pipeline gráfico dedicado** — executam estágios como transformação de vértices, rasterização e fragment shading
- **Memória especializada (VRAM)** — armazenam texturas, frame buffers e dados geométricos com alta largura de banda
- **Aceleração por hardware** — implementam operações gráficas comuns diretamente em circuitos dedicados
### Diferenças entre arquitetura simplificada e com GPU
|**Característica**|**Arquitetura Simplificada (Sem GPU)**|**Arquitetura com Processador Gráfico (GPU)**|
|---|---|---|
|**Responsável pelos Gráficos**|**CPU** (faz tudo: lógica e imagem).|**GPU** (especializada em renderização).|
|**Tipo de Processamento**|**Sequencial**: Uma tarefa após a outra.|**Paralelo**: Milhares de tarefas simultâneas.|
|**Núcleos de Processamento**|Poucos núcleos, mas muito poderosos.|Milhares de núcleos pequenos e eficientes.|
|**Memória (RAM)**|Compartilhada na **RAM principal** (gera competição).|**VRAM dedicada** (exclusiva e de alta velocidade).|
|**Papel do Controlador**|**Passivo**: Apenas lê e converte o sinal.|**Ativo**: Executa o pipeline gráfico completo.|
|**Desempenho (FPS)**|Baixo (gargalo no processamento).|Alto (fluidez e alta taxa de quadros).|
|**Carga do Sistema**|CPU fica sobrecarregada.|CPU fica livre para lógica e controle.|