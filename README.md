# Plano de testes para o site Cifra Club

## Objetivo
O objetivo deste plano é verificar e validar algumas funcionalidades presentes no site, testando principalmente se estão funcionais para os usuários.

## Ferramentas utilizadas
* **Python 3.12**
* **Behave**
* **Selenium**
* **Visual Studio Code**
* **Chrome Browser**


## Funcionalidades a serem testadas

1) **Pesquisa de cifra**:
    * Verificar se a lista de cifras condiz com o pesquisado.
    * Validar as sugestões de pesquisa quando estiver procurando uma cifra.

2) **Vizualização da cifra**:
    * Verificar se a cifra corresponde ao que foi pesquisado.
    * Verificar se a cifra é realmente do cantor/banda informado.

3) **Ações na cifra**:
    * Verificar se o botão de "Videoaula" funciona corretamente.
    * Verificar se o botão de "Auto rolagem" funciona corretamente.
    * Verificar se o botão de aumentar e diminuir texto funciona corretamente.
    * Verificar se o botão de "Tom" funciona corretamente.
    * Verificar se o botão "Acordes" exibe os acordes da cifra atual.
    * Verificar se ao clicar no botão "Afinação" aparece as opções de afinação.
    * Verificar se as opções do botão "Exibir" funcionam corretamente.


## Cenários de teste

## Estrutura do projeto
```bash
├── features
│   └── sample.feature
├── steps
│   └── sample_steps.py
├── pages
│   └── sample_page.py
├── environment.py
└── behave.ini
```
## Padrão de escrita
* Os nomes de classes devem seguir a notação CamelCase (MinhaClasse)
* Os nomes de variáveis devem ser em snake_case e totalmente em minúsculas (primeiro_nome)
* Os nomes de funções devem ser em snake_case e totalmente em minúsculas (quick_sort())
* As constantes devem ser em snake_case e totalmente em maiúsculas (PI = 3.14159)
* Os módulos devem ter nomes curtos, em snake_case e totalmente em minúsculas (numpy)
* Aspas simples e aspas duplas são tratadas da mesma forma (escolha uma e seja consistente)


## Ambiente de testes

*  Sistema Operacional: Windows 11
* Navegador: Chrome
* Resolução de tela: 1920x1080

## Reponsáveis pelos testes

* **Nome**: Arthur Leal
* **Email**: arthurleal1@hotmail.com

## Criterios de Aceitação

* Todos os cenários devem ser executados sem erros.
* Os testes de interface de usuários devem estar forma que nao atrapalhe o uso do software.
* Os resultados devem ser documentados e revisados pelos membros da equipe.
