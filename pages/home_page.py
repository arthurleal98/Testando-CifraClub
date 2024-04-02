from selenium.webdriver.common.by import By

class HomePage:
    def __init__(self, driver):
        self.DRIVER = driver
        self.URL = "https://www.cifraclub.com.br/"
        self.PESQUISA_FIELD = (By.ID, "js-h-search")
        self.BOTAO_PESQUISAR_BUTTON = (By.CSS_SELECTOR, "button.header-searchButton")
        self.TITULOS_RESULTADOS_PESQUISA = (By.CSS_SELECTOR, "div.gsc-thumbnail-inside")
        self.ELEMENTO_SUGESTAO = (By.CSS_SELECTOR, "#js-h-suggest > ul > li:nth-child(2)")
    def acessar_home_page(self):
        self.DRIVER.get(self.URL)

    def pesquisar_cifra(self, cifra):
        self.DRIVER.find_element(*self.PESQUISA_FIELD).send_keys(cifra)
        self.DRIVER.find_element(*self.BOTAO_PESQUISAR_BUTTON).click()

    def preencher_campo_pesquisa(self, cifra):
        self.DRIVER.find_element(*self.PESQUISA_FIELD).send_keys(cifra)

    def clicar_botao_pesquisar(self):
        self.DRIVER.find_element(*self.BOTAO_PESQUISAR_BUTTON).click()
    
    def clicar_opcao_pesquisa(self):
        self.DRIVER.find_element(*self.TITULOS_RESULTADOS_PESQUISA).click()

    def clicar_opcao_sugestao(self):
        self.DRIVER.find_element(*self.ELEMENTO_SUGESTAO).click()

    def clicar_na_primeira_musica(self):
        self.DRIVER.find_element(By.XPATH, "//span[@class='song-verified--ellipsis top-txt_primary__container']").click()