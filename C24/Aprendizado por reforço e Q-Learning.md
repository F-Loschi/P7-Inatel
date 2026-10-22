- Aprendizado por reforço
- Não aprende com dataset
- Tentativa e erro por penalidade e recompensa
- Paradigma voltado para tomada de decisão
- Agente é o algoritmo de aprendizado por reforço
- Adestramento de cachorro é um exemplo de aprendizado por reforço
## Q-Learning
- Model-free
- Não conhece as regras do ambiente
- O modelo é o conhecimento das regras do ambiente
- Aprende por experiência
- Começa "cego" e por tentativa e erro aprende
### Q
- Q vem de **qualidade**
- Representa o quão bom é uma ação que foi tomada
### Episódio
- Episódio é uma sequência completa de interações entre o agente e o ambiente, que começa num estado inicial e vai atualizando
- O treino é feito ao longo de muitos episódios
- Em cada episódio é usado o que se aprendeu nos anteriores
- O treinamento se encerra quando
	- Soma das recompensas obtidas para de subir e "estaciona" em um valor alto por muitos episódios seguidos
		- Agente já explorou o suficiente e encontrou o caminho ótimo
	- ou pela ausência de mudanças significativas
### Exploração vs. Explotação
- Exploração: Tentar ações aleatórias para descobrir novas recompensas
- Explotação: Escolher a melhor ação conhecida usando a tabela-Q atual
- Estratégia Epsilon-Greedy:
	- Com probabilidade epsilon, o agente explora
	- Com probabilidade 1-epsilon, o agente explota