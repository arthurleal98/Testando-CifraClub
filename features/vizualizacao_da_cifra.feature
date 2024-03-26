Feature: Vizualização da cifra

Scenario: Verificar se a cifra corresponde ao que foi pesquisado
Given que eu estou na página inicial
And pesquiso por "Bohemian Rhapsody"
When clico no botão de pesquisa 
Then vejo a cifra da música "Bohemian Rhapsody"


Scenario: Verificar se a cifra é realmente do cantor/banda informado
Given que eu estou na página inicial
And pesquiso por "Bohemian Rhapsody"
When clico no botão de pesquisa 
Then vejo a cifra da música "Bohemian Rhapsody" da banda "Queen"