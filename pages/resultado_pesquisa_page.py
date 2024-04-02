
class ResultadoDePesquisa:
    def __init__(self, driver):
        self.driver = driver

    def obter_todos_os_resultados(self):
        return self.driver.find_elements(By.XPATH, "//div[@class='gsc-webResult gsc-result']")
    
    def verificar_se_a_pesquisa_retornou_resultados(self, pesquisa):
        for resultado in self.obter_todos_os_resultados():
            if resultado.text == pesquisa:
                return True
        return False
    
    def clicar_no_primeiro_resultado(self):
        self.obter_todos_os_resultados()[0].click()