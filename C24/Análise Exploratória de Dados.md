[[Machine Learning]]
Etapas:
1. Definição do Problema
	- Importante saber de forma clara e bem definido o objetivo
	- **Como o problema será abordado, qual abordagem será utilizada e qual medida de desempenho será considerada**
2. Coleta de dados
	- Atender requisitos de volume e qualidade dos dados coletados
	- Dados de maior qualidade e representatividade
	- Análise dos dados visando verificar o tipo dos dados coletados e seu significado para o problema a ser abordado
	- **Separar em conjunto de treinamento e teste**
3. Preparação dos dados
	- Etapa responsável por transformar os dados brutos em um conjunto adequado para modelagem
		- EDA(Análise Exploratória dos Dados): Compreender os dados, analisando tudo possível. Orienta decisões importantes sobre quais transformações e ajustes serão necessários
		- Pré-processamento de Dados: Efetivamente tratados e transformados, incluindo limpeza, tratamento de valores faltantes, normalização ou padronização, etc etc.
	- Garantir dados consistentes, bem compreendidos e adequadamente estruturados, possibilitando um treinamento mais eficiente e resultados mais confiáveis
4. Escolha de um modelo
5. Treinamento
6. Avaliação
7. Ajuste de hiperparâmetro
8. Predição

## EDA
- Etapa antes da construção e treinamento
- Primeiro passo
- Transforma dados crus em conhecimento visual e estatístico
### Por que realizar?
- Garantir que não está aprendendo com lixo
## Inspeção Visual e Estatística
### Estatística
- Foco é o rigor
- Validar variabilidade
- Identificar tendências centrais
- Detectar discrepâncias
### Inspeção Visual
- Detectar padrões
- Identificar a distribuição
- Encontrar agrupamentos
- Confirmar correlações
### Por que utilizar as duas
- Conjuntos de dados com as mesmas estatísticas mas com comportamentos totalmente diferentes
## Tipos de dados
Precisa-se entender a taxonomia
- Variáveis qualitativas:
	- Nominal: não existe uma ordem entre elas
	- Ordinal: existe um hierarquia ou ordem lógica
- Variáveis quantitativas:
	- Discretas
	- Contínua
## Limpeza dos dados
Problemas que podemos encontrar:
- Valores irrelevantes
- Duplicatas
- Valores faltantes
- Tipos inconsistentes
- Outliers
### Removendo valores irrelevantes
- Colunas irrelevantes atrapalham a análise e os modelos, sem trazer informações úteis
- Melhora a qualidade do modelo
- Reduz risco de overfitting
- Acelera processamento
- Facilita interpretação dos dados
- Evita erros e inconsistências
- Ajuda na privacidade e governança
### Tratando valores faltantes
- Remover linhas ou colunas faltantes
- Preencher o dado faltante com estatísticas como média, moda e mediana
- Substituição:
	- Média:
		- Sensível a outliers
		- Usada com variáveis numéricas
	- Mediana:
		- Insensível a outiliers
		- Usada com variáveis numéricas
	- Moda:
		- Insensível a outliers
		- Usada com variáveis numéricas e categóricas
- Ao invés de chutar um valor fixo, o preenchimento inteligente tenta estimar o valor faltante usando padrões presente nos dados
- KNNImputer(K-Nearest Neighbors Imputer)
	- Procura as K linhas mais parecidas com a faltante e preenche usando a média
- IterativeImputer
	- Escolhe uma coluna com valores faltantes
	- Treina um modelo de regressão para prever Peso usando outras colunas como entrada
	- Preenche valores faltantes dessa coluna com as previsões do modelo
	- Repete isso para outras colunas, em ciclos, refinando as estimativas
## Outliers
- Valores muito fora do padrão que podem distorcer os seus dados e causar ruído
- Não pode ser simplesmente simplesmente removido, pois podem ser informações verídicas raras dos seus dados
- Distorcem estatísticas, prejudicam visualização, impactam modelos de ML, geram modelos enviesados e de pior desempenho
- Zuckemberg e Bill Gates são outliers nos dados de quem larga Harvard


**Correlação não significa causalidade!!!**
