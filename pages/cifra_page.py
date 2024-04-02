
from selenium.webdriver.common.by import By
class CifraPage:
    def __init__(self, driver):
        self.DRIVER = driver
        self.AUTO_ROLAGEM_CONTROL = (By.ID, "c-roll")
        self.AUTO_ROLAGEM_BUTTON = (By.ID, "side-rolagem")
        self.AUMENTAR_TEXTO_BUTTON = (By.ID, "side-font-more")
        self.TEXTO_CIFRA = (By.XPATH, "//pre[@div='cifra_cnt g-fix cifra-mono']")
        self.DIMINUIR_TEXTO_BUTTON = (By.ID, "side-font-less")
        self.AUMENTAR_TOM_BUTTON = (By.ID, "side-tom-more")
        self.DIMINUIR_TOM_BUTTON = (By.ID, "side-tom-less")
        self.TOM_ATUAL = (By.ID, "cifra_tom")
        self.ACORDES_BUTTON = (By.ID, "side-acordes")
        self.ACORDES = (By.ID, "c-acordes")
        self.AFINACAO_BUTTON = (By.ID, "side-afinacao")
        self.AFINACAO = (By.ID, "tuner-modal-wrapper")
        self.EXIBIR_BUTTON = (By.ID, "side-exibir")
        self.EXIBIR = (By.ID, "c-exibir")
    
    def verificar_se_o_botao_exibir_e_exibido(self):
        return self.DRIVER.find_element(*self.EXIBIR).is_displayed()
    def clicar_exibir(self):
        self.DRIVER.find_element(*self.EXIBIR_BUTTON).click()

    def clicar_afinacao(self):
        self.DRIVER.find_element(*self.AFINACAO_BUTTON).click()

    def verificar_se_a_afinacao_e_exibida(self):
        return self.DRIVER.find_element(*self.AFINACAO).is_displayed()

    def clicar_acordes(self):
        self.DRIVER.find_element(*self.ACORDES_BUTTON).click()

    def verificar_se_os_acordes_sao_exibidos(self):
        return self.DRIVER.find_element(*self.ACORDES).is_displayed()
    def clicar_aumentar_tom(self):
        self.DRIVER.find_element(*self.AUMENTAR_TOM_BUTTON).click()

    def clicar_diminuir_tom(self):
        self.DRIVER.find_element(*self.DIMINUIR_TOM_BUTTON).click()

    def obter_tom_atual(self):
        return self.DRIVER.find_element(*self.TOM_ATUAL).text
    def verificar_se_o_tom_mudou(self):
        tom_original = self.obter_tom_atual()
        self.DRIVER.find_element(*self.AUMENTAR_TOM_BUTTON).click()
        tom_atual = self.obter_tom_atual()
        return tom_atual != tom_original

    def clicar_aumentar_texto(self):
        self.DRIVER.find_element(*self.AUMENTAR_TEXTO_BUTTON).click()

    def clicar_diminuir_texto(self):
        self.DRIVER.find_element(*self.DIMINUIR_TEXTO_BUTTON).click()

    def verificar_se_o_texto_aumentou(self):
        tamanho_original = self.DRIVER.find_element(*self.TEXTO_CIFRA).value_of_css_property("font-size")
        self.DRIVER.find_element(*self.AUMENTAR_TEXTO_BUTTON).click()
        tamanho_atual = self.DRIVER.find_element(*self.TEXTO_CIFRA).value_of_css_property("font-size")
        return tamanho_atual > tamanho_original
    
    def verificar_se_o_texto_diminuiu(self):
        tamanho_original = self.DRIVER.find_element(*self.TEXTO_CIFRA).value_of_css_property("font-size")
        self.DRIVER.find_element(*self.DIMINUIR_TEXTO_BUTTON).click()
        tamanho_atual = self.DRIVER.find_element(*self.TEXTO_CIFRA).value_of_css_property("font-size")
        return tamanho_atual < tamanho_original
    def clicar_auto_rolagem(self):
        self.DRIVER.find_element(*self.AUTO_ROLAGEM_BUTTON).click()

    def verificar_se_a_cifra_rolou(self):
        return self.DRIVER.find_element(*self.AUTO_ROLAGEM_CONTROL).is_displayed()
    
