from behave import given, when, then
from pages.home_page import HomePage
from pages.cifra_page import CifraPage
@given(u'que o usuário está na página de cifras')
def step_impl(context):
    context.home_page = HomePage(context.driver)
    context.home_page.clicar_na_primeira_musica()


@when(u'o usuário clica no botão "Videoaula"')
def step_impl(context):
    pass

@then(u'o usuário é redirecionado para a página de videoaula')
def step_impl(context):
    pass

@when(u'o usuário clica no botão "Auto rolagem"')
def step_impl(context):
    context.cifra_page = CifraPage(context.driver)
    context.cifra_page.clicar_auto_rolagem()

@then(u'a cifra é rolada automaticamente')
def step_impl(context):
    context.cifra_page = CifraPage(context.driver)
    assert context.cifra_page.verificar_se_a_cifra_rolou() == True

@when(u'o usuário clica no botão "Aumentar texto"')
def step_impl(context):
    context.cifra_page = CifraPage(context.driver)
    context.cifra_page.clicar_aumentar_texto()
    
@then(u'o texto da cifra é aumentado')
def step_impl(context):
    context.cifra_page = CifraPage(context.driver)
    assert context.cifra_page.verificar_se_o_texto_aumentou() == True

@when(u'o usuário clica no botão "Diminuir texto"')
def step_impl(context):
    context.cifra_page = CifraPage(context.driver)
    context.cifra_page.clicar_diminuir_texto()

@then(u'o texto da cifra é diminuído')
def step_impl(context):
    context.cifra_page = CifraPage(context.driver)
    assert context.cifra_page.verificar_se_o_texto_diminuiu() == True

@when(u'o usuário clica no botão "Aumentar tom"')
def step_impl(context):
    context.cifra_page = CifraPage(context.driver)
    context.cifra_page.clicar_aumentar_tom()

@then(u'o tom da cifra é aumentado')
def step_impl(context):
    context.cifra_page = CifraPage(context.driver)
    assert context.cifra_page.verificar_se_o_tom_mudou() == True

@when(u'o usuário clica no botão "Diminuir tom"')
def step_impl(context):
    context.cifra_page = CifraPage(context.driver)
    context.cifra_page.clicar_diminuir_tom()

@then(u'o tom da cifra é diminuído')
def step_impl(context):
    context.cifra_page = CifraPage(context.driver)
    assert context.cifra_page.verificar_se_o_tom_mudou() == True

@when(u'o usuário clica no botão "Acordes"')
def step_impl(context):
    context.cifra_page = CifraPage(context.driver)
    context.cifra_page.clicar_acordes()

@then(u'os acordes da cifra são exibidos')
def step_impl(context):
    context.cifra_page = CifraPage(context.driver)
    assert context.cifra_page.verificar_se_os_acordes_sao_exibidos() == True

@when(u'o usuário clica no botão "Afinação"')
def step_impl(context):
    context.cifra_page = CifraPage(context.driver)
    context.cifra_page.clicar_afinacao()

@then(u'as opções de afinação são exibidas')
def step_impl(context):
    context.cifra_page = CifraPage(context.driver)
    assert context.cifra_page.verificar_se_a_afinacao_e_exibida() == True
@when(u'o usuário clica no botão "Exibir"')
def step_impl(context):
    context.cifra_page = CifraPage(context.driver)
    context.cifra_page.clicar_exibir()

@then(u'as opções de exibição são exibidas')
def step_impl(context):
    context.cifra_page = CifraPage(context.driver)
    assert context.cifra_page.verificar_se_o_botao_exibir_e_exibido() == True
