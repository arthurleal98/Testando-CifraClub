Feature: Ações na cifra
Scenario: Verificar se o botão de "Videoaula" funciona corretamente
Given que o usuário está na página de cifras
When o usuário clica no botão "Videoaula"
Then o usuário é redirecionado para a página de videoaula


Scenario: Verificar se o botão de "Auto rolagem" funciona corretamente
Given que o usuário está na página de cifras
When o usuário clica no botão "Auto rolagem"
Then a cifra é rolada automaticamente

Scenario: Verificar se o botão de aumentar texto funciona corretamente
Given que o usuário está na página de cifras
When o usuário clica no botão "Aumentar texto"
Then o texto da cifra é aumentado



Scenario: Verificar se o botão de diminuir texto funciona corretamente
Given que o usuário está na página de cifras
When o usuário clica no botão "Diminuir texto"
Then o texto da cifra é diminuído

Scenario: Verificar se o botão de aumentar "Tom" funciona corretamente
Given que o usuário está na página de cifras
When o usuário clica no botão "Aumentar tom"
Then o tom da cifra é aumentado

Scenario: Verificar se o botão de diminuir "Tom" funciona corretamente
Given que o usuário está na página de cifras
When o usuário clica no botão "Diminuir tom"
Then o tom da cifra é diminuído

Scenario: Verificar se o botão "Acordes" exibe os acordes da cifra atual
Given que o usuário está na página de cifras
When o usuário clica no botão "Acordes"
Then os acordes da cifra são exibidos

Scenario: Verificar se ao clicar no botão "Afinação" aparece as opções de afinação
Given que o usuário está na página de cifras
When o usuário clica no botão "Afinação"
Then as opções de afinação são exibidas

Scenario: Verificar se as opções do botão "Exibir" funcionam corretamente
Given que o usuário está na página de cifras
When o usuário clica no botão "Exibir"
Then as opções de exibição são exibidas
