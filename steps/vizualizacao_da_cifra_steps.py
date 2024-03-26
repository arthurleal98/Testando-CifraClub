from behave import given, when, then

@given(u'que pesquiso por "Bohemian Rhapsody"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given que pesquiso por "Bohemian Rhapsody"')


@when(u'clico no botão de pesquisa')
def step_impl(context):
    raise NotImplementedError(u'STEP: When clico no botão de pesquisa')


@then(u'vejo a cifra da música "Bohemian Rhapsody"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then vejo a cifra da música "Bohemian Rhapsody"')


@then(u'vejo a cifra da música "Bohemian Rhapsody" do cantor/banda "Queen"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then vejo a cifra da música "Bohemian Rhapsody" do cantor/banda "Queen"')