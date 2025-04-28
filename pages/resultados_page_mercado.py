from .base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ResultadosPageMercadoLibre(BasePage):
    PRIMER_RESULTADO = (By.XPATH, '(//h2)[1]')

    def validar_resultado(self, texto_esperado):
        resultado = self.wait_for_element(self.PRIMER_RESULTADO)
        return texto_esperado.lower() in resultado.text.lower()

    def wait_for_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )
