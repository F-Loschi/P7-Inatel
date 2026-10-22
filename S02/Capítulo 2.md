[[Capítulo 1]]
## Orientado a documentos
- Possuem como filosofia conter todas as **informações importantes** sobre algo em um **único documento**, ao invés de quebrá-las em parte.
- Problema que gera redundância de dados
- Benefício é que gera uma disponibilidade maior de dados, não precisa fazer um JOIN
- Sacrifica espaço por disponibilidade e velocidade
- Guarda em formato JSON, com a característica de chave-valor
- Pode-se ainda ter listas embutidas dentro do documento
- O Esquema de um documento é flexível e auto descritivo. Não é necessário defini-lo antes de usá-lo, ou seja, seus campos podem variar de acordo com a necessidade.
- Isso gera **dados Semiestruturados**, pois, mesmo havendo uma estrutura, ela não é fixa
---
Exercício: criar um JSON sobre você
{'nome': 'Felipe Silva Loschi',
 'idade': 21,
  'parentesco': [{'nome':'Delmo Loschi', 'parentesco': 'pai' }, {'nome': 'Andrea Maria da Silva Loschi', 'parentesco': 'mãe}]
  }
- Outro jeito:
{'nome': 'Felipe Silva Loschi',
 'idade': 21,
 'tem_ps4':True,
  'parentesco': {'pais':['andrea, delmo],
			'avós': [adão, wanda, laurita, pedro],
			'primos' :[joão, miguel, monara, leonidas]}
  }
  
  ---
  
## Introdução ao MongoDB
  - Collections equivalem a tables em SQL
  - Dentro das collections se colocam documents(Convertido para binário, JSON -> BSON), que são equivalentes a linhas
  - Colunas dentro das linhas equivalem a campos
  - 