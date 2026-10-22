[[Introdução]]
- Entender o objetivo
- Entender as variáveis
- Entender técnicas
## O que é:
- Várias definições
- Subcampo de IA
- Algoritmos que aprendem padrões e fazem inferência
- "Matemática com marketing"
- Álgebra linear, probabilidade e estatística
- Programação tradicional: regras + dados -> computador -> resultados
	- Você dá as **regras** e os **dados**
	- Computador **gera o resultado**
- Machine learning: resultados + dados -> computador -> regras
	- **Dá os dados e os resultados**
	- **Descobre as regras**
	- A máquina cria suas próprias regras baseado nos dados
## Objetivo:
- Generalizar 
## Paradigmas:
- Aprendizado Supervisionado
	- Dispõe de um conjunto de dados rotulados(entrada x, saída y)
	- Objetivo é construir uma função y=f(x){modelo} para prever o rótulo de uma **nova** amostra x(não previamente observada) da mesma distribuição
	- "Ensina pra uma criança sobre alguns gatos e depois tenta ver se ela consegue identificar um outro gato que você não mostrou"
	- Tarefas:
		- Classificação: a variável de saída é discreta
		- Regressão: a variável de saída é contínua
- Aprendizado Não Supervisionado
	- Autodidata
	- Entrega um monte de informação e deixa ele se virar
	- Conjunto de dados não rotulados
	- Objetivo é descobrir propriedades da estrutura do conjunto de dados
	- Tarefas:
		- Clustering: descobrir grupos de exemplos(dados) similares
			- Exemplos: "Quem viu, ouviu ou comprou isso, também viu, ouviu ou comprou aquilo"
		- Redução de Dimensionalidade: encontrar uma representação mais simples dos dados para agilizar algoritmos ou permitir visualização
			- Exemplos: Comprimir uma imagem mantendo a qualidade
			- Remover informações inúteis
		- Detecção de anomalias: identificar casos que fogem do padrão esperado
		- Modelos Generativos: gerar novos exemplos, tipicamente com características específicas
	- Maldição de dimensionalidade: maior o número de entradas, maior o número de dimensões. Chega a um ponto explosivo
- Aprendizado Por reforço
	- Não existe nenhum tipo de dado para treinamento, sejam rotulados ou não
	- Máquina aprende por tentativa e erro
	- Usado na robótica
	- Não há dado, apenas o ambiente
	- Tentativa e erro onde o agente aprende através de recompensas
	- Objetivo: maximizar a recompensa e evitar punições
---
- Exercício:
	A. supervisionado: classificação
	B. reforço
	C. não supervisionado: clustering
	D. não supervisionado: detecção de anomalias
- --
