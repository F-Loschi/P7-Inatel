- Dividido em duas categorias: entrada e saída
## 1. Saída 
- Dispositivos ligados a visualização.
- Os dispositivos de saída foram sendo melhorados conforme o mercado pressionava por uma melhora, em vários sentidos, como qualidade, preço, tamanho, consumo de energia e portabilidade. 
### 1.1 Display
- Emite um raio de elétrons, o fosforo decaí quimicamente e forma uma imagem. Imagem não muito boa e imagens muito simples de formas geométricas.
- CRT(Tubo de Raios Catódicos) Vetorial: Funciona traçando linhas e curvas na tela.
- CRT Matricial: Faz um scan constante e repetitivo da tela inteira. A imagem surge pela modulação da intensidade do feixe enquanto ele varre a matriz de pontos. Formato matricial usa de bits para formar as imagens, com combinação de bits.
### 1.2 Plasma Display Panel
### 1.3 LCD(Liquid Crystal Display)
### 1.4 Led Display
- Basicamente o LCD mas com Led, o que é meio que uma fraude mercadológica mas economiza mais que o LCD
### 1.5 OLED(Organic Light-Emitting Diode)
### 1.6 AMOLED(Active Matrix OLED)
### 1.7 MicroLED
- Santo Graal de dispositivos de saída
### 1.8 E Ink
- Usado no kindle e dispositivos de leitura
- Demora muito pra atualizar, mas não há uma necessidade que seja rápido
---

|Tecnologia|Contraste|Resposta|Consumo|Burn-in|Status|
|---|---|---|---|---|---|
|**CRT**|Infinito|<1ms|Alto|Sim|Obsoleto|
|**Plasma**|15.000:1|Rápido|Alto|Sim|Obsoleto|
|**LCD**|1000:1|1-10ms|Baixo|Não|Dominante|
|**Mini-LED**|1M:1 (zonas)|1-10ms|Médio|Não|Premium|
|**OLED**|Infinito|0.1ms|Médio|Sim|Premium|
|**MicroLED**|Infinito|<0.001ms|Baixo|Não|Futuro|
|**E Ink**|15:1|300-1000ms|Mínimo|Não|E-readers|

---
### Pixels

Após analisarmos diversos modelos de telas, e se tratando da imagem que é formada pelos pixels de uma tela, podemos analisar melhor como isso funciona.

Pixel é a abreviação de Picture Element, é o menor ponto de uma imagem. 
-  Normalmente contém de 1 a 32 bits. 
- 1 bit para imagem branco e preto 8 bits para tons de cinza 
- 24 bits para imagens coloridas (16 milhões de cores) 32 bits para imagens coloridas com transparência.

|                    |                                |                    |
| ------------------ | ------------------------------ | ------------------ |
| **Bits Per Pixel** | **Number of Colors Available** | **Common Name(s)** |
| 1                  | 2                              | Monochrome         |
| 2                  | 4                              | CGA                |
| 4                  | 16                             | EGA                |
| 8                  | 256                            | VGA                |
| 16                 | 65536                          | XGA, High Color    |
| 24                 | 16777216                       | SVGA, True Color   |
| 32                 | 16777216 + Transparency        |                    |
| 48                 | 281 Trillion                   |                    |
A resolução de uma imagem é o número de pixels que ela contem.
Cada imagem, dependendo do seu tamanho e da quantidade de cores possíveis em cada pixel, pode necessitar de um espaço de armazenamento específico. Para analisarmos quanto espaço uma imagem ocupará, podemos nos apoiar nos bits por pixel e na quantidade de pixels dessa configuração, chegando assim à forma tradicional de identificarmos a quantidade de bytes que uma imagem pode ocupar em armazenamento.