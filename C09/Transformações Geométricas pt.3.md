[[Transformações Geométricas pt.2]]
## Visualização planar de objetos tridimensionais 
 Permite ver 3D em 2D, como se estivesse vendo algo 3D de um ponto de vista
- Plano de projeção: superfície onde o objeto será projetado
- Raio de projeção: retas que passam pelos pontos do objeto e pelo centro de projeção
- Centro de projeção: ponto fixo de onde os raios de projeção partem. Se estiver no infinito: projeção paralela. Se finito: projeção perspectiva.
## Classificação das Projeções Geométricas
- Depende da relação entre o centro, o plano e as direções dos raios de projeção.
- Resumo simplificado: se os raios de projeção são paralelos → projeção paralela. Se convergem para um ponto → projeção perspectiva.
## Projeção paralela ortográfica
- Centro no infinito e linhas paralelas entre si.
- Na ortográfica, linhas são perpendicular ao plano de projeção
- Característica:
	- Preserva proporções e paralelismo entre arestas.
	- Não há efeito de perspectiva (objetos distantes não aparecem menores).
	- Muito usada em CAD, plantas baixas, vistas de engenharia.
- No YZ:
$$ \begin{bmatrix} 0 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 1 & 0 \\ T_x & 0 & 0 & 1 \end{bmatrix}$$
- No XZ:
$$\begin{bmatrix} 1 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & T_y & 0 & 1 \end{bmatrix}$$
- No XY:
$$\begin{bmatrix} 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & T_z & 1 \end{bmatrix}$$
## Projeção Paralela Oblíqua
- Linhas de projeção são inclinadas em relação ao plano de projeção em qualquer ângulo
$$ \begin{bmatrix} 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ l\cos\alpha & l\sin\alpha & 0 & 0 \\ 0 & 0 & 0 & 1 \end{bmatrix} $$
### Variantes:
- Cavaleira (l = 1, \alpha = 45°​): 
	- Preserva **todas** as medidas originais do objeto.
	- A profundidade (eixo z) é representada em escala 1:1.
	- Resultado: objeto parece “esticado” em profundidade.
- Gabinete (l = 0{,}5, \alpha = 45°):
	- Somente a **face paralela ao plano de projeção** permanece com seu tamanho original.
	- As demais arestas (em profundidade) ficam com **metade do tamanho**.
	- Resultado mais realista visualmente do que a projeção cavaleira.
## Projeção Perspectiva(Cônica)
- Representa a vista pelo olho humano
- Obtidas pela interseção dos raios projetores com o plano de projeção
- Características:
	- Objetos mais distantes aparecem **menores** (encurtamento perspectivo).
	- Linhas paralelas parecem convergir para um **ponto de fuga**.
	- Reproduz fielmente a percepção visual humana.
	- Usada em jogos 3D, cinema de animação, realidade virtual.
## Derivação
$$P_p = \left(x \cdot \frac{d}{z},\; y \cdot \frac{d}{z},\; d\right)$$
- $$\frac{d}{z}$$ é um fator de escala que varia com a profundidade. Pontos mais distantes são mais reduzidos.
## Matriz de Projeção Perspectiva Básica
- W = z/d
$$P_p = \begin{bmatrix} 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 0 & 1/d & 0 \end{bmatrix} \times \begin{bmatrix} x \\ y \\ z \\ 1 \end{bmatrix} = \begin{bmatrix} x \\ y \\ z \\ z/d \end{bmatrix}$$
### Por eixo
 $$\text{Perspectiva em X:}\quad \begin{bmatrix} 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 1/d & 0 & 0 & 0 \end{bmatrix} \qquad \text{Perspectiva em Y:}\quad \begin{bmatrix} 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 1/d & 0 & 0 \end{bmatrix} \qquad \text{Perspectiva em Z:}\quad \begin{bmatrix} 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 0 & 1/d & 0 \end{bmatrix}$$

## Projeção Perspectiva com Centro Arbitrário
- Aplica-se a mesma lógica da rotação em torno de um ponto arbitrário
1. Transladar para a origem
2. Aplicar a matriz de projeção perspectiva
3. Transladar de volta
- Resultado final:
$$P_p = \begin{bmatrix} x - x_0 + x_0 \cdot \dfrac{z - z_0}{d} \\[6pt] y - y_0 + y_0 \cdot \dfrac{z - z_0}{d} \\[6pt] z - z_0 + z_0 \cdot \dfrac{z - z_0}{d} \\[6pt] \dfrac{z - z_0}{d} \end{bmatrix} = \begin{bmatrix} \dfrac{x - x_0}{\frac{z - z_0}{d}} + x_0 \\[6pt] \dfrac{y - y_0}{\frac{z - z_0}{d}} + y_0 \\[6pt] d + z_0 \\[6pt] 1 \end{bmatrix}$$

## Comparação entre os tipos:
| Característica              | Paralela Ortográfica          | Paralela Oblíqua       | Perspectiva                |
| --------------------------- | ----------------------------- | ---------------------- | -------------------------- |
| Raios de projeção           | Paralelos e perpendiculares   | Paralelos e inclinados | Convergentes para um ponto |
| Centro de projeção          | No infinito                   | No infinito            | A distância finita         |
| Preserva ângulos?           | Apenas os paralelos ao plano  | Não totalmente         | Não                        |
| Preserva paralelismo?       | ✅ Sim                         | ✅ Sim                  | ❌ Não                      |
| Efeito de profundidade?     | ❌ Nenhum                      | ❌ Parcial              | ✅ Total                    |
| Semelhança com visão humana | Baixa                         | Média                  | Alta                       |
| Uso típico                  | CAD, plantas, vistas técnicas | Ilustrações técnicas   | Jogos, cinema, VR          |