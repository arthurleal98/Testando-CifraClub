from behave import given, when, then
from pages.home_page import HomePage

@given(u'que eu estou na página de pesquisa de cifras')
def step_impl(context):
    context.home_page = HomePage(context.driver)
    context.home_page.acessar_home_page()

@when(u'eu preencher o campo de pesquisa com "Noite Feliz"')
def step_impl(context):
    context.home_page.preencher_campo_pesquisa("Noite Feliz")


@when(u'eu clicar no botão de pesquisa')
def step_impl(context):
    context.home_page.clicar_botao_pesquisar()


@then(u'eu devo ver a cifra de "Noite Feliz"')
def step_impl(context):
    assert context.home_page.cifra_existe("Noite Feliz") == True

@when(u'eu preencher o campo de pesquisa com "Cifra inexistente"')
def step_impl(context):
    context.home_page.preencher_campo_pesquisa("Cifra inexistente")

@then(u'eu devo ver a mensagem "Nenhuma cifra encontrada"')
def step_impl(context):
    assert context.home_page.cifra_existe("Cifra inexistente") == True

@when(u'eu preencher o campo de pesquisa com "123#$%456"')
def step_impl(context):
    context.home_page.preencer_campo_pesquisa("123#$%456")

@then(u'eu devo ver a mensagem "Termo de pesquisa inválido"')
def step_impl(context):
    assert context.home_page.cifra_existe("123#$%456") == False

@when(u'eu preencher o campo de pesquisa com ""')
def step_impl(context):
    context.home_page.preencher_campo_pesquisa("")

@when(u'eu preencher o campo de pesquisa com "a"')
def step_impl(context):
    context.home_page.pesquisar_cifra("a")

@when(u'eu preencher o campo de pesquisa com "Is this the real life? Is this just fantasy?"')
def step_impl(context):
    context.home_page.preencher_campo_pesquisa("Is this the real life? Is this just fantasy?")

@then(u'eu devo ver a cifra de "Bohemian Rhapsody"')
def step_impl(context):
    assert context.home_page.cifra_existe("Bohemian Rhapsody") == True