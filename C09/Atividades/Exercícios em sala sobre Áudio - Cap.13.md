Nome: Felipe Silva Loschi
Matrícula: GES - 601
## **Questão 1**

Um engenheiro precisa digitalizar um sinal de voz humana com frequência máxima de 4 kHz. Qual é a taxa de amostragem mínima necessária para evitar aliasing, segundo o Teorema de Nyquist-Shannon? Qual é o nome do fenômeno que ocorre caso essa taxa não seja respeitada, e por que ele é problemático?

**Resposta:** De acordo com o teorema, a taxa mínima é de 8kHz, que é o dobro da frequência máxima. Caso isso não ocorra, o que ocorrerá é o Aliasing, que é quando componentes de alta frequência do sinal aparecem como componentes de baixa frequência bi sinal digitalizado, fenômeno irreversível.

---

## **Questão 2**

Um sinal de áudio estéreo (2 canais) é digitalizado com frequência de amostragem de 44,1 kHz e profundidade de quantização de 16 bits por amostra.

a) Calcule a taxa de bits bruta (Rb) para um canal mono.

$$ f_{max} = \frac{f_{ams}}{2} = \frac{44,1}{2}=22,05kHz$$
$$ R_b \geq 2\text{ x }q \text{ x }f_{max}$$
$$R_b \geq 2 \text{ x } 16 \text{ x } 22,05$$
$$R_b \geq 705,6kbps\text{[mono]}$$
b) Calcule a taxa de bits total para o sinal estéreo.
$$R_b \geq 705,6 \text{ x }2$$
$$R_b \geq 1,4Mbps\text{[dois canais]}$$
c) Qual é a SNR aproximada proporcionada por essa profundidade de bits?
$$SNR \approx 6,02\text{ x }q+1,76$$
$$SNR \approx 98dB$$

---

## **Questão 3**

Explique a diferença entre os formatos de arquivo WAV, FLAC e MP3, classificando cada um como _sem compressão_, _lossless_ ou _lossy_. Para cada formato, indique uma situação de uso adequada e justifique sua escolha.
- **WAV:** Formato sem compressão, taxa típica de aproximadamente 1400kbps, qualidade original e uso típico para produção, edição e masterização. Mesmo ocupando muito espaço ainda preserva 100% da informação.
- **FLAC:** Lossless, comprime o arquivo em 50% mas sem nenhuma perda de informação, usando codificação entrópica. Reproduz bit a bit idêntico ao WAV original na decodificação. Usado por audiofilia e arquivamento.
- **MP3:** Lossy, descarta irreversivelmente informações perceptualmente irrelevantes. Oferece melhor relação qualidade/tamanho para distribuição. Normalmente usado por streaming, para download e para portabilidade.
---

## **Questão 4**

O codec AAC é frequentemente descrito como superior ao MP3 para a mesma taxa de bits. Cite **duas** diferenças técnicas entre eles que justificam essa afirmação, e indique em qual aplicação do cotidiano o AAC é o codec padrão adotado.

**Resposta:** O AAC usa a MDCT com janelas maiores (1024 vs. 576 pontos no MP3), o que confere maior resolução espectral para sinais estacionários resultando em menor ruído de quantização espectral. A alocação de bits é feita por coeficiente MDCT individual (muito mais granular que sub-bandas do MP3), e o modelo psicoacústico é mais sofisticado. O que significa que a mesma qualidade subjetiva percebida com ~30% menos bits em relação ao MP3.
