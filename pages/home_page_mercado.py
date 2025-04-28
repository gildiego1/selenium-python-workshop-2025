from .base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HomePageMercadoLibre(BasePage):
    CAMPO_BUSQUEDA = (By.NAME, 'as_word')

    def buscar_producto(self, nombre_producto):
        campo = self.wait_for_element(self.CAMPO_BUSQUEDA)
        campo.clear()
        campo.send_keys(nombre_producto)
        campo.submit()

    def wait_for_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )
