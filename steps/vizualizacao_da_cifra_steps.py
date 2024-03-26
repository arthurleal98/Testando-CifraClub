from behave import given, when, then
from pages.home_page import HomePage

@given(u'que eu estou na página inicial')
def step_impl(context):
    context.driver.get("https://www.cifraclub.com.br/")
    context.home_page = HomePage(context.driver)


@given(u'pesquiso por "Bohemian Rhapsody"')
def step_impl(context):
    context.home_page.pesquisar_cifra("Bohemian Rhapsody")


@when(u'clico na primeira opção de sugestao')
def step_impl(context):
    context.home_page.clicar_opcao_sugestao()


@then(u'vejo a cifra da música "Bohemian Rhapsody"')
def step_impl(context):
    assert "Bohemian Rhapsody" in context.driver.title

@then(u'vejo a cifra da música "Bohemian Rhapsody" da banda "Queen"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then vejo a cifra da música "Bohemian Rhapsody" da banda "Queen"')