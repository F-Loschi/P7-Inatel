### Capítulo 7 - Multimídia e Hipermídia

**Questão 1 (Fechada).** Assinale a alternativa que melhor distingue multimídia linear de multimídia não-linear:

a) A multimídia linear é interativa e a não-linear é passiva.

b) Na multimídia linear o conteúdo segue uma ordem predefinida e a plateia é passiva; na não-linear o usuário interage e escolhe seu próprio caminho.

c) Ambas exigem a participação ativa do usuário para avançar no conteúdo.

d) A multimídia não-linear dispensa o uso de computador.

e) A multimídia linear não combina mídias estáticas e dinâmicas.

**Resposta:** B

**Questão 2 (Aberta).** Diferencie hipertexto e hipermídia. Dê um exemplo de cada e explique por que a World Wide Web é considerada um exemplo de multimídia não-linear.
**Resposta:** Hipermídia é a mistura de mistura de hipertexto com hipermídia, como a WWW, já o hipertexto é uma escrita

---

### Capítulo 8 - Dados Multimídia

**Questão 3 (Fechada).** Sobre imagens vetoriais e matriciais (raster), assinale a alternativa correta:

a) Imagens vetoriais são formadas por uma matriz de pixels e perdem qualidade ao serem ampliadas.

b) Imagens matriciais são descritas por primitivas geométricas e podem ser escaladas sem perda.

c) Imagens vetoriais são descritas por primitivas geométricas (pontos, linhas, curvas) e podem ser escaladas sem perda de qualidade; as matriciais dependem da resolução.

d) Os formatos JPEG e PNG são exemplos típicos de imagens vetoriais.

e) Não há diferença prática entre os dois tipos ao redimensionar a imagem.

**Resposta:** C

**Questão 4 (Aberta).** Explique a diferença entre composição espacial e composição temporal de dados multimídia. Cite a hierarquia de unidades de um vídeo, da menor para a maior.
**Resposta:** Composição espacial é sobre como o elemento está disposto espacialmente na composição na imagem, sobrepondo ou não outros elementos. A composição temporal é sobre quando começa, quando termina, se é intervalo ou instante. Quadro -> tomada -> cena -> sequência

---

### Capítulo 9 - Processamento de Imagens

**Questão 5 (Fechada).** Assinale a alternativa correta sobre o pipeline e as técnicas de processamento de imagens:

a) O aprimoramento de imagem (enhancement) adiciona informação nova que não existia na cena original.

b) O pipeline clássico compreende pré-processamento, segmentação, extração de características e classificação.

c) O filtro de média preserva as bordas melhor do que o filtro de mediana.

d) A segmentação é sempre a primeira etapa, executada antes do pré-processamento.

e) O histograma de uma imagem indica a posição espacial de cada pixel.

**Resposta:** B

**Questão 6 (Aberta).** O que é a equalização de histograma e qual é o seu objetivo? Explique também por que se diz que o aprimoramento de imagem não cria informação nova.
**Resposta:** A equalização propõe a ideia de redistribuir os valores de mesma faixa para que haja aproximadamente o mesmo valor de pixels por nível no histograma. O aprimoramento de imagem não cria informação, ele apenas aprimora o que já existe, como sumir com ruído

---

### Capítulo 10 - Operações no Domínio do Espaço

**Questão 7 (Fechada).** Relacione cada operação com sua aplicação típica e assinale a alternativa com a associação totalmente correta:

a) Subtração: mascaramento de uma região de interesse.

b) AND: detecção de movimento entre dois quadros consecutivos.

c) NOT: obtenção do negativo da imagem (255 menos o valor do pixel).

d) Blending: união de formas de duas imagens binárias.

e) XOR: aumento uniforme de brilho somando uma constante.

**Resposta:** C 

**Questão 8 (Aberta).** A operação de blending é dada por Q = X · P1 + (1 - X) · P2, com 0 <= X <= 1. Explique por que ela evita o problema de overflow, ao contrário da soma simples de duas imagens.
**Resposta:** Evita overflow porque a soma de P1 com P2 nunca irá ultrapassar 255 devido ao fator de peso

---

### Capítulo 11 - Operações no Domínio da Frequência

**Questão 9 (Fechada).** Sobre a filtragem no domínio da frequência, assinale a alternativa correta:

a) Um filtro passa-baixa realça bordas e detalhes finos da imagem.

b) Um filtro passa-alta produz suavização (blur) da imagem.

c) Em imagens naturais, a energia tende a se concentrar nas altas frequências, longe do centro do espectro.

d) Um filtro passa-baixa preserva as baixas frequências e atenua as altas, suavizando a imagem.

e) A filtragem na frequência dispensa a transformada inversa para retornar ao domínio do espaço.
**Resposta:** D

**Questão 10 (Aberta).** Enuncie o teorema da convolução e explique sua utilidade prática na filtragem de imagens. Cite também a vantagem da FFT em relação ao cálculo direto da DFT.
**Resposta:** A convolução é a mudança de espectro e sua utilidade é devido ao cálculo ser mais fácil em diferentes espectros. A FFT tem a vantagem de ser uma transformada mais rápida em relação a DFT.

---

### Capítulo 12 - Compressão de Imagens

**Questão 11 (Fechada).** Sobre a compressão JPEG (baseline, com perdas), assinale a alternativa correta:

a) A perda de informação ocorre na etapa da DCT, e não na quantização.

b) A sequência simplificada é: DCT em blocos, depois quantização e, por fim, codificação entrópica (RLE e Huffman); a perda ocorre na quantização.

c) O JPEG não utiliza nenhuma forma de codificação de entropia.

d) A DCT é aplicada à imagem inteira de uma só vez, sem divisão em blocos.

e) A quantização é totalmente reversível e não causa perda de qualidade.
**Resposta:** B

**Questão 12 (Aberta).** Diferencie compressão com perdas e sem perdas. Cite ao menos um formato de cada tipo e uma situação de uso em que a compressão sem perdas é preferível.
**Resposta:** Compressão com perdas significa que ao comprimir é perdido informação que não é relevante ou notável ao espectador, enquanto a sem perdas é o contrário, o arquivo inteiro é comprimido.

---

### Capítulo 13 - Visão Geral sobre Áudio

**Questão 13 (Fechada).** Sobre a digitalização de áudio, assinale a alternativa correta:

a) Amostragem é a discretização da amplitude, e quantização é a discretização no tempo.

b) Pelo teorema de Nyquist, a taxa de amostragem deve ser pelo menos o dobro da maior frequência presente no sinal.

c) Aumentar o número de bits por amostra reduz a relação sinal-ruído (SNR).

d) O número de níveis de quantização independe do número de bits por amostra.

e) Para qualidade de CD, utiliza-se taxa de amostragem de 8 kHz.

**Questão 14 (Aberta).** Explique o que é o efeito de mascaramento da audição e como codecs perceptuais (por exemplo, MP3 e AAC) o utilizam para reduzir a taxa de dados sem perda perceptível de qualidade.

---

### Capítulo 14 - Visão Geral sobre Vídeo Analógico

**Questão 15 (Fechada).** Sobre os sistemas de TV analógica e a varredura, assinale a alternativa correta:

a) O sistema NTSC utiliza 625 linhas e taxa de atualização de 50 Hz.

b) Na varredura progressiva, o quadro é dividido em dois campos exibidos alternadamente.

c) A taxa de campos por segundo, no entrelaçado, é o dobro da taxa de quadros por segundo.

d) O sistema SECAM transmite as informações de cor por modulação QAM, simultaneamente.

e) As siglas 1080i e 1080p referem-se, respectivamente, às varreduras progressiva e entrelaçada.

**Resposta:** C

**Questão 16 (Aberta).** Explique o que é a varredura entrelaçada, por que ela foi adotada na TV analógica e qual artefato visual pode surgir em cenas de movimento rápido.

---

### Capítulo 15 - Sistema de TV Digital

**Questão 17 (Fechada).** Sobre o Sistema de TV Digital e a compressão MPEG-2, assinale a alternativa correta:

a) Os quadros I (Intra) dependem dos quadros vizinhos para serem decodificados.

b) Os quadros B (bidirecionais) utilizam informação dos quadros anterior e posterior, enquanto os quadros I são independentes e os P se baseiam no quadro anterior.

c) A compensação de movimento sempre transmite o quadro inteiro, sem economia de dados.

d) A largura de banda de cada canal foi ampliada de 6 MHz para 12 MHz na transição para o digital.

e) O multiplexador (MUX) tem a função de modular a portadora de rádio.

**Resposta:** B

**Questão 18 (Aberta).** Descreva a relação de simetria entre o transmissor e o receptor de TV digital, citando ao menos três pares de operações inversas. Explique também a função do multiplexador (MUX) e do transport stream.

---

### Questões de síntese (conteúdo combinado)

**Questão 19 (Fechada).** Sobre a Transformada Discreta de Cosseno (DCT) usada na compressão de imagens, assinale a alternativa correta:

a) A DCT converte o bloco do domínio da frequência de volta para o domínio do espaço.

b) Após a DCT, a energia do bloco tende a se concentrar em poucos coeficientes de baixa frequência, o que favorece a compressão.

c) A DCT é uma operação com perdas por si só, independentemente da quantização.

d) Os coeficientes resultantes da DCT são percorridos em ordem aleatória antes da codificação.

e) A DCT só pode ser aplicada a imagens binárias.

**Questão 20 (Aberta).** Compare a filtragem no domínio do espaço (convolução com máscara) e no domínio da frequência (multiplicação pela função de transferência). Em que situações cada abordagem costuma ser mais vantajosa?

---