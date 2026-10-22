[[Tipos de Testes]]
## Automatizar
- Utilização de um software para automatizar tarefas presentes em um script de testes
	- Execução de casos de testes de um determinado componente
	- Dados do teste devem ser definidos para todas as situações possíveis(Espírito de porco)
## TDD
- Test Driven Development
- Desenvolve primeiro o teste e depois o código em si
- Garante que vai ter teste para o que eu estou desenvolvendo
## BDD(Behaviour Driven Development)
- Desenvolvimento baseado em comportamento
- Descrever o comportamento humano na utilização de um software
- Evolução do TDD, automatizar também comportamentos do software
- Surgiu pela dificuldade de explicar o que precisa ser testado
- Gherkin: especificamente para descrever comportamentos desejados de um software
- Como escrever BDD: Dado ... Quando ... E ... E ... Então ... .
- Métodos de testes são públicos para serem executados de fora do projeto
- Métodos auxiliares são privados para garantir acesso somente dentro da classe
- Métodos de testes retornam void para ficarem isolados, porém recebem parâmetros vindos exclusivamente do código Gherkin