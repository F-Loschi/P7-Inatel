[[Dispositivos Gráficos - pt. 2, 3 e 4]]
## Conceituação Inicial
Operações matemáticas que alteram características visuais e espaciais de objetos digitais baseados em:
- Posição: Localização no espaço
- Orientação: ângulo/ Direção
- Forma: Geometria do objeto
- Tamanho: Escala dimensional
## Classificação
### Euclidiana
- Preserva comprimento e ângulos
- Operações: translação, rotação e reflexão
- Altera pouco o objeto

### Afim
- Preserva paralelismo
- Operação: Escala(homoteia) e cisalhamento

### Projetiva
- Preserva linhas por linhas
- Operações: Projeção perspectiva(1° pessoa) e projeção paralela(jogos de cima)
- Altera bastante do objeto/cenário

## Coordenadas Homogêneas
- 2D cartesiano(x, y) -> Homogêneo 2D(x, y, 1)
- 3D cartesiano(x, y, z) -> Homogêneo 3D(x, y, z, 1)
	- A dimensão extra(w=1) é a base de funcionamento das GPUs modernas com operações entre matrizes


## Sistemas de Coordenadas
### Cartesiano 
- 2D e 3D: Uso geral, transformações matriciais
### Polares
2D: círculos e radares
### Cilíndricas
3D: Cilindros, tubos, hélices
### Esféricas
3D: Esferas, globos, simulações de câmera
## Sistemas de Referências
### Objeto(SRO)
Dimensões relativas ao centro do próprio objeto
### Universo(SRU)
Coordenadas do mundo real da aplicação(distância) em metros
### Normalizado(SRN)
Valores entre 0 e 1, independente de dispositivo - [0,1] x [1,0]
### Dispositivo
Unidade nativas do dispositivo de saída - pixels, DPI, etc.

