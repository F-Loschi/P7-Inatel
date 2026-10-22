Felipe Silva Loschi
GES - 601
## Cap. 7 - Multimídia e Hipermídia

### **Questão 01** – Defina "multimídia" com suas palavras. Em seguida, explique o que é multimídia "linear" e "não linear", apontando vantagens, desvantagens e exemplos de cada.
Multimídia pode ser definido como a combinação de mídias, sendo que a combinação deve ter pelo menos uma mídia estática e uma mídia dinâmica.
Multimídia linear é aquela em que que segue uma linha de acontecimento fixa e não muda até o final. A vantagem dela é o seguimento linear do raciocínio e é eficaz quando o publico consegue absorver bem o que está sendo passado. Sua desvantagem é a falta de interatividade, que pode levar a falta de interesse. Exemplos são slide, enredo de um filme, vídeo do YouTube, etc.
Multimídia não linear é aquela que não segue um roteiro fixo e podem acontecer diferentes coisas dependendo da interação do publico. Sua vantagem é a liberdade proporcionada ao telespectador, o que ajuda a prender a atenção da pessoa. A desvantagem é que pode vir a ser desorganizado se não for bem arquitetado e/ou utilizado. Exemplos são sites, menu de DVD, etc.

### **Questão 02** – Qual característica difere a hipermídia da multimídia convencional?
A característica que difere a hipermídia da multimídia convencional é o uso de hipertexto, o que significa que o usuário tem escolha sobre o caminho que toma a fim de recolher informação, podendo ignorar certos itens ou passar por cada pedaço de informação que está listado. O exemplo clássico é a World Wide Web.

---

## Cap. 8 - Dados Multimídia

### **Questão 03** – Quais os principais tipos de dados multimídia? Cite dois exemplos de cada.
- Vídeo: Filmes MP4, clipes AVI
- Imagem: JPEG, PNG
- Áudio: MP3, AAC
- Texto: HTML, PDF
- Animação: GIFs, Flash, CSS
- Gráficos 3D: Modelos OBJ, cenas em formato GLTF

### **Questão 04** – Como é realizada a composição de dados multimídia de diferentes tipos?
Ela é realizada de duas maneiras:
- Composição Espacial: Envolve a organização dos elementos de mídia no espaço visual, ou seja, a forma como estão dispostos na tela ou na área de exibição. Pode ser feita através de sobreposição, onde um elemento de mídia é colocado sobre o outro, ou em justaposição, quando múltiplas unidades de dados são ligadas ou posicionadas lado a lado em uma mesma área de exibição.
- Composição Temporal: Trata da organização dos elementos ao longo do tempo, ou seja, quando cada elemento começa, quanto tempo dura e como se relaciona com os demais. Especificado pelo instante ou pelo intervalo.

### **Questão 05** – Ao longo das últimas décadas, mídias de armazenamento e dispositivos de processamento de multimídia evoluíram significativamente. Em quais aspectos se deu essa evolução? Qual(is) fator(es) científico-tecnológico(s) contribuiu(iram) para isto?
Os aspectos em que se deram a maior evolução foram:
- Volume de armazenamento de dados: disquete para fitas magnéticas digitais para armazenamento óptico ao SSD
- Velocidade de processamento: processamento com núcleos e GPUs dedicadas
- Largura de banda: redes evoluíram do dial-up (56 kbps) para fibra óptica e 5G (Gbps), permitindo streaming de vídeo em alta qualidade.
- Compressão: algoritmos como MPEG, H.264 e H.265 reduziram drasticamente o tamanho dos arquivos sem perda perceptível de qualidade.
Os fatores científico-tecnológicos que contribuíram foram a Lei de Moore(aumento exponencial da densidade de transistores), os avanços em teoria da informação e codificação e o desenvolvimento da microeletrônica e dos semicondutores.

---

## Cap. 9 - Processamento de Imagens

### **Questão 06** – No contexto das técnicas de processamento de imagens, explique os conceitos de pré-processamento, segmentação e extração de características, destacando a contribuição de cada técnica para um sistema de classificação de imagens.
- Pré-processamento: Responsável por preparar a imagem para as etapas seguintes, corrigindo erros gerados no momento do registro da imagem e aprimorando sua qualidade. Pode também converter a imagem em uma forma mais adequada para o visualizador.
- Segmentação: Processo de subdivisão da imagem, de forma a isolar as regiões de interesse. Pode ser usado para separar o fundo do objeto ou segmentar objetos de interesse. Importante para as etapas seguintes por ser que isola o objeto de interesse.
- Extração de Características:  Transforma os dados brutos em um conjunto reduzido de atributos numéricos que conseguem descrever a imagem, ou objeto isolado, de forma compacta. Importante pois reduz a dimensionalidade de forma a deixar a comparação computacionalmente possível. 

---

## Cap. 10 - Operações no Domínio do Espaço

### **Questão 07** – Que operações aritméticas entre imagens podem causar underflow e/ou overflow? Como esta situação pode ser contornada? Explique.
As operações são adição, subtração e SHIFT. Para contornar esse problema, podemos usar algumas abordagens, como:
- Truncamento por saturação: valores acima de 255 são convertidos para 255 e valores negativos são convertidos para 0, intuitivo e preserva aparência; 
- Truncamento invertido: valores acima de 255 são convertido para 0 e valores negativos são convertidos para 255, útil para mostrar os pixels que passam; 
- Reescalonamento: ao invés de truncar, o algoritmo primeiro realiza a operação em um tipo de dado que suporte os valores que ultrapassem e depois esses valores sejam reescalonados para o intervalo de 0 a 255.

### **Questão 08** – Qual mudança na representação de imagens binárias deve ser realizada ao efetuar operações lógicas (em contrapartida com aritméticas) para que os operadores, tabelas-verdade e resultados façam sentido? Explique.
Como nas operações lógicas trabalhamos apenas com 0(False) e 1(True), os valores que estão em escala aritmética, de 0 a 255, devem ser convertidos para seus respectivos valores em binário para que a operação possa ser feita bit a bit.

### **Questão 09** – Que operações lógicas entre imagens podem causar underflow e/ou overflow? Como esta situação pode ser contornada? Explique.
Como operações lógicas fazem o uso de bits e as operações são feitas bit a bit, é impossível causar um underflow ou um overflow, uma vez que os resultados bit a bit sempre serão 0 ou 1. Caso a conversão do intervalo não seja previamente feita, a operação pode acabar não fazendo sentido, mas ainda estará dentro do intervalo.

---

## Cap. 11 - Operações no Domínio da Frequência

### **Questão 10** – Quais passos são necessários para realizar uma operação em imagens no domínio da frequência? Explique brevemente cada um.
- Transformada: Imagem é transformada para o domínio da frequência pela transformada discreta. Resultado é uma representação F(u,v) cujos coeficientes indicam quanto de cada frequência está presente na imagem. 
- Filtragem: A imagem transformada é multiplicada ponto a ponto pelo filtro H(u, v). O filtro determina o que passa(valores próximos a 1) e o que é bloqueado(valores próximos a 0) em cada frequência. 
- Transformada Inversa: A imagem resultante G(u, v) é submetida a uma transformada inversa, retornando ao domínio espacial como g(x', y'). A imagem final é o que vemos.

### **Questão 11** – O que representam componentes de baixa frequência? Que tipo de filtro os remove de uma imagem? Qual é o resultado esperado na imagem final?
Componentes de baixa frequência representam variações suaves de intensidade na imagem, ou seja, as informações globais de luminância e cor. 
O filtro que os remove é o filtro Passa-Alta.
O efeito esperado na imagem final são os detalhes finos da imagem mais enfatizados, como bordas, texturas e contornos. A imagem ficam com aparência semelhante a um desenho a lápis ou a um relevo gravado.

### **Questão 12** – O que representam componentes de alta frequência? Que tipo de filtro os remove de uma imagem? Qual é o resultado esperado na imagem final?
Componentes de alta frequência representam o oposto, logo, variações abruptas, como bordas e ruídos.
O filtro que os remove é o filtro Passa-Baixa.
O  efeito visual é uma imagem menos nítida, com perda dos detalhes finos. 

---

## Cap. 12 - Compressão de Imagens Parte 1

### **Questão 13** – Explique um formato/técnica de compressão de imagens sem perdas.
Na codificação de Huffman, ao invés de gastar 8 bits para representar cada símbolo, como faz o ASCII, usa-se um número variável de bits, sequências curtas para símbolos frequentes e sequências longas para símbolos raros, o que é chamado de codificação entrópica.
#### Como funciona:
1. Conta-se a frequência de cada símbolo na entrada (quantas vezes cada pixel/cor/letra aparece).
2. Constrói-se uma árvore binária combinando, a cada passo, os dois símbolos de menor frequência em um nó pai, até restar um único nó raiz.
3. Atribuem-se códigos: a cada aresta da árvore associa-se um bit (0 ou 1). O código de um símbolo é a sequência de bits do caminho da raiz até a folha correspondente.
O resultado é um conjunto de códigos com a propriedade do prefixo livre: nenhum código é prefixo de outro, garantindo decodificação unívoca.

### **Questão 14** – Explique um formato/técnica de compressão de imagens com perdas.
O JPEG(Joint Photographic Experts Group) funciona seguindo os seguintes passos:
1. Obtenção do espectro bidimensional via DCT 2D: cada bloco de 8×8 pixels é transformado em uma matriz 8×8 de coeficientes de frequência.
2. Truncamento dos componentes do espectro: os coeficientes são divididos por uma tabela de quantização, e em seguida arredondados. Coeficientes pequenos (alta frequência, pouca energia) viram zero. **É aqui que ocorre a perda**.
3. Codificação entrópica: os coeficientes resultantes (com muitos zeros) são percorridos em ordem zig-zag e comprimidos com RLE + Huffman.

---

## Cap. 12 - Compressão de Imagens Parte 2

### **Questão 15** – Como os quadros de uma sequência de vídeo são subdivididos?
- I-frames: quadros completos, comprimidos de forma independente.
- P-frames: contêm apenas as diferenças em relação ao I-frame ou P-frame anterior.
- B-frames: preditos a partir de frames anteriores e posteriores, oferecendo maior compressão.
A sequência de frames entre dois I-frames é chamada de GOP (Group of Pictures).

### **Questão 16** – Para qual espaço de cor uma imagem em RGB deve ser alterada antes da etapa de subamostragem de cor? O que significam cada componente deste espaço?
O que deve ser alterado antes da etapa de subamostragem de cor é transformar do espaço RGB para YCrCb. Nesse espaço, as componentes são:
- Y (Luminância): Representa o brilho da imagem. É a componente mais importante perceptualmente.
- Cb (Chroma Blue): Diferença entre o azul e a luminância. Representa informação de cor "fria".
- Cr (Chroma Red): Diferença entre o vermelho e a luminância. Representa informação de cor "quente".

### **Questão 17** – Qual o propósito de realizar a subamostragem de cor em um quadro de vídeo? Em qual aspecto da visão humana este procedimento se baseia?
A subamostragem de cor baseia-se na ideia de que o sistema visual humano é mais sensível a variações de luminância do que variações de crominância, assim, é possível destacar parte dos canais de crominância(Cb e Cr), mantendo a resolução integral da luminância(Y), sem que o observador perceba.
### **Questão 18** – Explique a diferença entre os formatos 4:4:4, 4:2:2 e 4:2:0.
|Formato|Descrição|Redução de dados|Uso típico|
|---|---|---|---|
|**4:4:4**|Sem subamostragem — cada pixel tem Y, Cb e Cr completos|0% (sem redução)|Pós-produção, cinema RAW|
|**4:2:2**|Cb e Cr amostrados horizontalmente na metade|~33% de redução|Broadcast, câmeras profissionais|
|**4:2:0**|Cb e Cr amostrados na metade horizontal E vertical|~50% de redução|JPEG padrão, H.264, streaming|

### **Questão 19** – A ideia geral da Transformada Discreta do Cosseno (DCT) consiste em representar os dados da imagem como uma combinação (isto é, uma soma ponderada) de ondas cossenoidais. Explique as etapas deste processo, desde a extração dos pixels da imagem até a obtenção dos coeficientes da DCT.
- Passo 0 - Input Block: Divisão da imagem em blocos de 8x8.
- Passo 1 - Shifted Block(Centralização): Subtrai-se 128 de todos os valores, centralizando o sinal em torno de zero para que que a DCT funcione com valores simétricos.
- Passo 2 - Aplicação da DCT: decompõe-se os blocos em 64 coeficientes que representam as frequências espaciais crescentes. O coeficiente DC de cada posição representa a média do bloco e os coeficientes AC representam as variações.
- Passo 3 - Obtenção dos coeficientes: gera-se a matriz 8x8 de coeficientes da DCT, com energia concentrada nos coeficientes de baixa frequência.

### **Questão 20** – Como é feita a remoção das componentes de alta frequência de uma imagem? Explique.
A remoção é feita através do processo de quantização, sendo a única etapa de perda irreversível do JPEG. Divide-se cada coeficiente DCT pelo valor correspondente em uma Tabela de Quantização, arredondando o resultando para o inteiro mais próximo. As componentes altas são removidas pois o arredondamento joga o valor dessas casas para 0, descartando-as.

### **Questão 21** – Qual a vantagem trazida pela travessia em zig-zag para algoritmos de codificação, utilizados nas etapas finais do JPEG?
Após a quantização, a maior parte dos coeficientes de alta frequência é zero e, quando ordenados pela travessia em zig-zag, é possível agrupar os zeros no final da sequência. Com isso, cria-se longas sequências de zeros, o que torna mais eficiente de ser codificado por RLE, aumentando a taxa de compressão na etapa de codificação por entropia.

### **Questão 22** – Como é possível ajustar a qualidade de uma imagem ao comprimi-la?
A qualidade do JPEG pode ser ajustada multiplicando ou dividindo os valores da tabela de quantização:
- Qualidade alta: Multiplica-se por um fator que torne os divisores menores, assim, mais coeficientes sobrevivem e maior é a fidelidade do arquivo.
- Qualidade baixa: Multiplica-se por um fator que torne os divisores maiores, assim, mais coeficientes são zerados e menor é a fidelidade do arquivo.

### **Questão 23** – É possível recuperar os dados descartados pelo processo de quantização? Justifique.
Não. A quantização é a única etapa da pipeline do JPEG que possui perda de informações de forma irreversível. A quantização arredonda os valores, assim, não é possível conseguir os valores originais.

### **Questão 24** – Explique os passos necessários para descomprimir uma imagem JPEG, enfatizando a necessidade de persistir as tabelas de quantização no arquivo final (além dos dados da imagem).
O processo é realizado na ordem inversa:
1. Decodificação de Huffman + RLE: O fluxo de bits é decodificado, recuperando a matriz 8x8 quantizada de coeficientes.
2. Reordenação: reconverte a sequência zig-zag de volta à matriz 8×8.
3. Dequantização: Cada coeficiente é multiplicado pelo valor correspondente na tabela de quantização, que foi salva no arquivo, logo, é aqui que a importância de salvar a tabela se mostra, pois é preciso dela para o processo inverso: $$F'(u,v) = Q(u,v) \times T_Q(u,v)​$$
4. DCT inversa(IDCT): reconstrói-se os valores de pixel do bloco 8x8, o que transforma os coeficientes de volta ao domínio do espaço.
5. Deslocamento e recombinação: desfaz o deslocamento de nível e reagrupa os blocos para reconstruir a imagem completa.
Os valores obtidos são aproximações dos coeficientes DCT originais e a informação que foi perdida não pode ser recuperada.

---

## Cap. 13 - Visão Geral sobre Áudio

### **Questão 25** – Qual o papel da amostragem, no contexto de digitalização de áudio?
Amostragem é o processo de capturar o valor da amplitude do sinal analógico em instantes regulares e igualmente espaçados. Cada captura é chamada de amostras e o intervalo de período de amostragem. A amostragem é o primeiro passo para a digitalização.

### **Questão 26** – O que define o Teorema da Amostragem de Nyquist-Shannon? Explique.
O Teorema de Amostragem diz que para reconstruir um sinal analógico sem aliasing, a taxa de amostragem deve ao, no mínimo, o dobro da frequência máxima do sinal. Em fórmula:
$$f_s \geq 2 .f_{max}$$

### **Questão 27** – Como é possível reduzir o erro de quantização ao discretizar um sinal de áudio?
Para reduzir o ruído de quantização é necessário aumentar o número de bits por amostras. Quanto mais bits por amostra, menor o ruído de quantização.
Outra técnica seria usar compressão logarítmica, a qual concentra mais níveis nas amplitudes baixas, onde o ouvido é mais sensível, reduzindo o erro perceptivo.
Outra técnica é o Dithering, que adiciona ruído de baixa amplitude antes da quantização para distribuir o erro de forma aleatória, o que evita padrões audíveis.

### **Questão 28** – Qual é a taxa mínima de bits necessária para representar uma fonte de áudio analógica de 20 Hz a 20 kHz quantizada com 128 níveis de amplitude?
- Pelo teorema de Nyquist:
$$ f_{s} = 2 \times20.000 = 40.000$$
- Bits por amostra:
$$ log_2(128) = 7 \text{ bits/amostra}$$
- Taxa de bits:
$$ \text{Bit rate} = f_s\times\text{bits/amostra} = 40.000\times7 = 280.000bps = 280kbps $$


---

## Cap. 14 - Visão Geral sobre Vídeo Analógico

### **Questão 29** – Em vídeo analógico, qual o propósito dos sinais de sincronismo?
O propósito dos sinais de sincronismo em vídeo analógico é para que o monitor saiba onde e quando desenhar cada linha, além de quando começar e parar de produzir cada linha. A ideia é garantir que o feixe de elétrons da câmera e o feixe do monitor estejam sempre coordenados, varrendo a mesma posição no mesmo instante.

### **Questão 30** – Quais são as características (ou seja, forma de onda, frequência e amplitude) dos pulsos de sincronismo horizontal e vertical?
- Pulso de sincronismo horizontal: Ocorre ao final de cada linha, tem forma de onda retangular, é um pulso negativo, tem frequência de aproximadamente 15,734kHz e sua amplitude leva o sinal abaixo do nível de preto.
- Pulso de sincronismo horizontal: Ocorre ao final de cada quadro, tem maior duração que o horizontal e frequência de 60Hz ou 50 Hz. Sinaliza o retorno do feixe ao topo da tela.

### **Questão 31** – Quais as diferenças entre os processos de varredura progressiva e entrelaçada?
- Progressiva: As linhas são desenhadas de forma progressiva, o que significa que uma é desenhada após a outra, de cima para baixo, de forma natural. Cada quadro é desenhado inteiramente antes de iniciar o próximo. A taxa de exibição típica é de 25 ou 30 quadros/s. Usado tipicamente em monitores, DVDs progressivos, Blu-ray e grande parte dos conteúdos digitais modernos.
- Entrelaçada: Quadro é dividido em dois campos: campo ímpar, que é transmitido primeiro e um campo par, que é transmitido em seguida. A taxa de campos por segundo é o dobro da taxa de quadros por segundo, o que dá a impressão de fluidez.

### **Questão 32** – Como é possível transmitir vídeo colorido usando um único cabo?
Para transmitir vídeo colorido com um único cabo, o sinal de cor é modulado em uma subportadora de frequência específica sobreposta ao sinal de luminância. O sinal composta combina luminância, crominância modulada e pulsos de sincronismo. O receptor demodula a subportadora para separar luminância e crominância e reconstruir as componentes da cor.

### **Questão 33** – A quais propriedades da cor as características do sinal correspondem?
A crominância possui características que correspondem as seguintes propriedades:
- Amplitude da subportadora -> saturação
- Fase da subportadora -> matiz
- Luminância -> brilho

### **Questão 34** – Para que serve o sinal conhecido como color burst?
Para que o monitor consiga interpretar corretamente as fases e, portanto, as cores, ele precisa de uma referência. O color burst é adicionado ao início de cada linha de vídeo, logo após o sinal de sincronismo horizontal, mas ainda durante o intervalo de blanking horizontal. Ele é usado como referência para dar ao monitor um ponto de partida para a matiz e a saturação. O color burst é enviado com 180 graus de fase para servir de referência neutra.