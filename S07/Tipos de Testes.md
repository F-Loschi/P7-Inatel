[[Introdução Qualidade de Software]]
## Testes Manuais:
- Definições sobre o que são testes manuais
## Testes Automatizados
- Definições e diferentes tipos de testes automatizados
- Escopo
- Tipos
## Cenário de teste
- Descrição de uma **ideia específica** a ser testada, sem detalhar os dados e etapas
- Ex.: Testar se o botão de mutar no Teams funciona corretamente
## Caso de teste
- Descrição de uma ação ou objetivo que o usuário pode encontrar durante a utilização do sistema
- Ex.: Se estiver mutado e fechar o Teams, o áudio deve continuar mutado para a próxima seção
- O botão de mutar deve ter seu comportamento isolado do botão da câmera
![[Pasted image 20260223222014.png]]

## Suíte de teste
- Conjunto de casos e cenários de teste
	- Executadas pela ferramenta de teste
	- O testador de software cria de acordo com sua necessidade
![[Pasted image 20260223220959.png]]
## Teste manual
- Bastante usado no teste exploratório e teste de usabilidade
## Teste automatizados
- Extremamente valorizada no desenvolvimento moderno de software
- Códigos que testam códigos
- Facilmente replicável
- Análises rápidas
- Garante funcionamento da aplicação

## Manual vs. Automatizado
- Depende do SUT
	- Games fazem muito uso de ambos
	- Demanda do mercado por testes automatizados está cada vez maior
### Vantagens de automação
![[Pasted image 20260223222055.png]]
## Tipos de testes automatizados
### Testes automatizados
- Os testes funcionais são escritos da perspectiva do usuário
- Confirmam que o sistema faz o que os usuários esperam
- Não importa com o comportamento interno, apenas a saída
- Exemplo: Ver se o botão de pesquisa faz a pesquisa
### Testes Fim a Fim
- Verifica o fluxo completo de um software está de acordo com o planejado
- Garantir que a informação passa de um fim ao outro
- Executado no ambiente real
### Não funcional
- Validam os requisitos não funcionais do sistema. Entre eles:
	- Desempenho
		- Tempo de resposta é aceitável
	- Usabilidade
		- Experiência do usuário
	- Segurança
		- Proteção contra ataques diversos
	- Disponibilidade
		- Verificar se fica disponível nos diversos ambientes
	- Manutenibilidade
		- Deve ser facilmente mantido
	- Recuperação
		- Recuperação é executada de maneira adequada
	- Carga
		- Grande volume de carga, dados ou usuários
		- Identificar problemas problemas de dimensionamento de link, infraestrutura, recursos ou implementação ineficiente
### Regressão
- Verificar se alguma alteração do software causa algum erro
