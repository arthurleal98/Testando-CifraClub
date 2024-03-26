from behave import given, when, then

@given(u'que eu estou na página de pesquisa de cifras')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given que eu estou na página de pesquisa de cifras')


@when(u'eu preencher o campo de pesquisa com "Noite Feliz"')
def step_impl(context):
    raise NotImplementedError(u'STEP: When eu preencher o campo de pesquisa com "Noite Feliz"')


@when(u'eu clicar no botão de pesquisa')
def step_impl(context):
    raise NotImplementedError(u'STEP: When eu clicar no botão de pesquisa')


@then(u'eu devo ver a cifra de "Noite Feliz"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then eu devo ver a cifra de "Noite Feliz"')


@when(u'eu preencher o campo de pesquisa com "Cifra inexistente"')
def step_impl(context):
    raise NotImplementedError(u'STEP: When eu preencher o campo de pesquisa com "Cifra inexistente"')


@then(u'eu devo ver a mensagem "Nenhuma cifra encontrada"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then eu devo ver a mensagem "Nenhuma cifra encontrada"')


@when(u'eu preencher o campo de pesquisa com "123#$%456"')
def step_impl(context):
    raise NotImplementedError(u'STEP: When eu preencher o campo de pesquisa com "123#$%456"')


@then(u'eu devo ver a mensagem "Termo de pesquisa inválido"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then eu devo ver a mensagem "Termo de pesquisa inválido"')


@when(u'eu preencher o campo de pesquisa com ""')
def step_impl(context):
    raise NotImplementedError(u'STEP: When eu preencher o campo de pesquisa com ""')


@when(u'eu preencher o campo de pesquisa com "a"')
def step_impl(context):
    raise NotImplementedError(u'STEP: When eu preencher o campo de pesquisa com "a"')


@when(u'eu preencher o campo de pesquisa com "Is this the real life? Is this just fantasy?"')
def step_impl(context):
    raise NotImplementedError(u'STEP: When eu preencher o campo de pesquisa com "Is this the real life? Is this just fantasy?"')


@then(u'eu devo ver a cifra de "Bohemian Rhapsody"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then eu devo ver a cifra de "Bohemian Rhapsody"')