Feature: Pesquisa de cifras
Scenario: Pesquisar cifras
Given que eu estou na página de pesquisa de cifras
When eu preencher o campo de pesquisa com "Noite Feliz"
And eu clicar no botão de pesquisa
Then eu devo ver a cifra de "Noite Feliz"

Scenario: Pesquisar cifras inexistentes
Given que eu estou na página de pesquisa de cifras
When eu preencher o campo de pesquisa com "Cifra inexistente"
And eu clicar no botão de pesquisa
Then eu devo ver a mensagem "Nenhuma cifra encontrada"

Scenario: Pesquisar cifras com termos inválidos
Given que eu estou na página de pesquisa de cifras
When eu preencher o campo de pesquisa com "123#$%456"
And eu clicar no botão de pesquisa
Then eu devo ver a mensagem "Termo de pesquisa inválido"


Scenario: Pesquisar cifras com termos vazios
Given que eu estou na página de pesquisa de cifras
When eu preencher o campo de pesquisa com ""
And eu clicar no botão de pesquisa
Then eu devo ver a mensagem "Termo de pesquisa inválido"

Scenario: Pesquisar cifras com termos muito curtos
Given que eu estou na página de pesquisa de cifras
When eu preencher o campo de pesquisa com "a"
And eu clicar no botão de pesquisa
Then eu devo ver a mensagem "Termo de pesquisa inválido"


Scenario: Pesquisar cifras com partes de musicas
Given que eu estou na página de pesquisa de cifras
When eu preencher o campo de pesquisa com "Is this the real life? Is this just fantasy?"	
And eu clicar no botão de pesquisa
Then eu devo ver a cifra de "Bohemian Rhapsody"
