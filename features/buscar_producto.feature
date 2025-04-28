Feature: Realizar búsqueda de productos en MercadoLibre
    Scenario: Buscar un iPhone 13 y validar los resultados
        Given el cliente accede a la página principal de MercadoLibre
        When ingresa el término "iPhone 13" en la barra de búsqueda
        Then se visualizan resultados relacionados con "iPhone"
