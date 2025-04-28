from behave import given, when, then
from selenium import webdriver
from pages.home_page_mercado import HomePageMercadoLibre
from pages.resultados_page_mercado import ResultadosPageMercadoLibre

@given('el cliente accede a la página principal de MercadoLibre')
def step_given_homepage(context):
    context.driver = webdriver.Chrome()
    context.driver.get('https://www.mercadolibre.com.co')
    context.driver.maximize_window()
    context.home_page = HomePageMercadoLibre(context.driver)

@when('ingresa el término "iPhone 13" en la barra de búsqueda')
def step_when_search_product(context):
    context.home_page.buscar_producto("iPhone 13")
    context.results_page = ResultadosPageMercadoLibre(context.driver)

@then('se visualizan resultados relacionados con "iPhone"')
def step_then_verify_results(context):
    assert context.results_page.validar_resultado("iPhone"), "El texto 'iPhone' no se encontró en los resultados."
