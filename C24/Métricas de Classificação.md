## Matriz de confusão
- Mostra o quanto um classificador está se confundindo
- Contabiliza o número de classificações corretas e incorretas para cada uma das Q classes existentes
- Diagonal principal de C fornece o número de classificações corretas
- A q-ésima linha indica o total de exemplos que foram classificados como pertencentes a q-ésima classe, incluindo exemplos que pertencem e não pertencem à classe
- A q-ésima coluna indica o total de exemplos que realmente pertencem à q-ésima classe
- ![[Pasted image 20260409181216.png]]
- ![[Pasted image 20260409182427.png]]
## Acurácia
- Mede a proporção de exemplos classificados corretamente em relação ao total de exemplos avaliados
- Fornece uma indicação de quão bem o modelo está fazendo suas predições corretas em comparação com todas as previsões feitas
- Se Verdadeiro Positivo(TP) for muito grande devido a um desbalanço na base de dados, a acurácia vai tender a 1, mas o modelo é horrível devido a falta de dados
## Precisão
- Proporção de exemplos da classe positiva corretamente classificados em relação a todos os exemplos atribuídos à classe positiva
- Boa medida para determinar a qualidade do classificador quando os custos de falsos positivos são altos
## Recall
- Proporção de exemplos da classe positiva corretamente classificados
- Calcula quantos exemplos realmente positivos o classificador captura em relação a todos os exemplos positivos
- Boa medida para determinar a qualidade de um classificador quando os custos de falso negativos são altos
## F1-score
- Combina duas métricas em uma única
- Dá a mesma importância a precisão e para o recall
- Valores de F1 próximos de 1 indicam que o classificador obteve ótimos resultados tanto de precisão quanto de recall