- Aprendizado não supervisionado, não tenho rótulos, apenas atributos.
- Tenta agrupar dados por semelhança
- Enxergar padrões mesmo não conhecendo as classes
- Procura por grupos de exemplos semelhantes
- Relações não explícitas entre dados
- Redução de complexidade
- Detecção de anomalias
## Como representar
- Várias formas
- Mais simples e utilizada é centroides com K-Means
- Centroide é o ponto central de um cluster
	- Representa a média
- Centroide pode ser usado como:
	- Centros para iniciar redes neurais Baysianas ou de funções de base radial
	- Estimativa de valores de atributos ausentes
	- Forma de comprimir dados usando apenas o centroide mais próximo
	- Usar para definir o que é normal e o que está fora do normal
- Centroide utiliza valores numéricos, então usamos apenas para esse mesmo tipo de atributos. Existem outras técnicas para atributos categóricos.
- Uma amostra pertence unicamente a um cluster
- Clusters não se sobrepõe
## A qual cluster um exemplo pertence
- Uma amostra *x* possui um distância ao centroide, dada pela distância Euclidiana
- Calcula-se a distância entre os centroides e a amostra e a amostra pertencerá ao cluster com a menor distância ao centroide
## K-Means
- O "k" é um hiperparâmetro que define o número de clusters
1. O centroide é inicialmente definido de forma aleatória
2. Dado os centroides definido, agrupa-se as amostras nos cluster
3. Com as amostras definidas, calcula-se a média e o centroide muda de posição para essa média
4. Com o novo centroide, refaz-se os passos 2 e 3 até atingir os critérios de parada, que pode ser número de iterações e menor distância possível das amostras para o centroide
## Método do cotovelo
- Busca o ponto onde a melhoria do aumento de clusters começa a diminuir significativamente
- Aumentar o número de clusters sempre traz uma melhora, mas chega em um ponto em que o ganho é marginal
- O ponto é o cotovelo da curva