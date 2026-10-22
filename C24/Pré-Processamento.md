[[Pré-Processamento]]
- Limpar a bagunça antes de alimentar um modelo
## Divisão do Dataset
- Generalizar bem para dados novos
- Não é correto usar o mesmo conjunto para treinar, validar e testar, pois a eficácia vai ser 100%, já que o modelo vai decorar os dados
### Conjunto de treinamento
- Modelo "aprende" os padrões
- Mais representativo, melhor
- Maior parte dos dados
### Conjunto de validação
- Melhor modelo e ajustar hiper parâmetros
- Treina com o treinamento e compara desempenho na validação para não ter vícios
- Ajustar hiperparâmetros
- Escolher arquiteturas
- Decidir quando parar
## Escalonamento de atributos
- Modelos não conhecem unidades, apenas números
- Modelos baseados em distância ou gradiente são sensíveis à escala dos atributos
- Escalonamento iguala a influência dos atributos no modelo
### Principais técnicas de escalonamento
#### Normalização(Min-Max Scaling): 
Transforma todos os valores numéricos para uma escala fixa, normalmente entre 0 e 1
- Quando usar:
	- Dados sem outliers
	- Algoritmos que não pressupõem nenhuma distribuição
#### Padronização:
Transforma os atributos para terem média 0 e desvio padrão 1, não impondo limites
- Vantagens: 
	- Torna os dados "comparáveis" em termos do número de desvios padrão da média
	- Robusto a outliers
- Quando usar: 
	- Quando temos uma gaussiana
#### Escalonamento Robusto:
Usa mediana e distância interquartil no escalonamento
- Vantagens:
	- Outliers tem influência mínima nos dados escalonados
	- Bom para outliers extremos
- Quando usar:
	- Outliers significativos
	- Distribuições assimétricas ou caudas longas
### Armadilhas
- O escalonador deve sempre ser ajustado no conjunto de treinamento
- **Conjuntos de validação e teste são transformados com valores encontrados com o conjunto e treinamento**
- Não se aplica à variável alvo, apenas atributos
- Não escalonar binários ou one-hot sem necessidade para não criar valores fracionários desnecessários
### Codificação de atributos categóricos
Modelos não entendem texto, precisamos converter em categorias
#### One-Hot Encoding
- Usado com atributos nominais e com baixa cardinalidade
- **Cria coluna binária para cada categoria distinta**
- Limitação: Gera alta dimensionalidade
#### Label Encoding
- Converte cada categoria para um número inteiro único, mas sem uma ordem
- Codificação de rótulo
- Limitação: pode introduzir uma ordem onde não existe
#### Target Encoding
Substitui cada categoria pela média do valor alvo correspondente
- Ideal para variáveis de alta cardinalidade
- Risco de overfitting quando uma categoria tem pouco exemplo
#### Binary Enconding
- Combina benefícios de One-Hot e Label
- Cada categoria recebe um número inteiro e depois ele é convertido para sua representação binária
- Desvantagem de algumas categorias compartilharem bits, modelos lineares podem achar que existe relação

## Engenharia de atributos
- Transformação ou criação de novos atributos que sejam mais úteis e informativos
- Ajuda o modelo a enxergar relações que não são óbvias
- Melhora a capacidade de predição do modelo
### Extração de atributos
- Transformar dados brutos em um conjunto menor de atributos significativos
#### PCA
Cria novos atributos que são combinações lineares das variáveis originais, sendo o 1° componente captura a maior variância possível e o 2 captura a maior variância restante, sem se correlacionar com o 1°
#### ICA
Novos atributos como combinações lineares, mas busca componentes estatisticamente independentes
#### BoW
Transforma texto em um vetor onde cada posição representa uma palavra do vocabulário e o valor é 0/1(presença) e contagem(quantas vezes aparece)
#### TF-IDF
Como o BoW, mas pondera palavras. Palavras **características** de um texto ganham mais peso que as comuns.
#### Word Embeddings: 
Representa palavras como vetores numéricos densos onde a geometria do espaço captura significado: palavras com sentidos parecidos ficam próximas
#### HOG:
Divide a imagem em pequenas regiões e calcula histograma de orientação das bordas(direções dos gradientes)
### Análise de componentes principais(PCA)
- Projeta dados de alta dimensão em um espaço de menor dimensão
- Funciona encontrando novas direções que capturam o máximo de variância dos dados e projetando os dados nessas direções para reduzir dimensionalidade com mínimo de perda de informação
- Encontra direções que descrevem como os dados estão espalhados
- Ordenadas por variância, da maior para menor
- Cada componente é uma combinação linear dos atributos originais
- **Apenas após separação dos conjuntos em treinamento, validação e teste**
## Seleção de atributos
Processo de selecionar um subconjunto de atributos que contribuem para melhoria do desempenho do modelo
- Reduz overfitting
- Reduz custo computacional
- Facilita interpretação
### Métodos de filtro
Seleciona atributos antes de treinar o modelo, usando critérios estatísticos
### Métodos de encapsulamento
- Desempenho do próprio modelo para avaliar subconjuntos de atributos.
- "Quais atributos fazem o meu modelo performar melhor de verdade"
- Suscetível a overfitting
### Métodos Embarcados
- Seleção durante o treinamento com algoritmos que possuem mecanismos que penalizam ou priorizam atributos