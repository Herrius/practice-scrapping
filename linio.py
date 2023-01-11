"""
OBJETIVO: 
    - Extraer informacion de ramen para.
    - Aprender a realizar extracciones verticales utilizando reglas
    - Aprender a utilizar MapCompose para realizar limpieza de datos
CREADO POR: LEONARDO KUFFO
ULTIMA VEZ EDITADO: 09 ENERO 2023
"""
from scrapy.item import Field
from scrapy.item import Item
from scrapy.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
from scrapy.loader.processors import MapCompose
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader


class News(Item):
    name = Field()
    price = Field()
    features = Field()


# CLASE CORE - Al querer hacer extraccion de multiples paginas, heredamos de CrawlSpider
class Linio(CrawlSpider):
    name = 'Linio'
    custom_settings = {
        'USER_AGENT': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
    }

    # Reduce el espectro de busqueda de URLs. No nos podemos salir de los dominios de esta lista
    allowed_domains = ['https://www.linio.com.pe/']

    # Url semilla a la cual se hara el primer requerimiento
    start_urls = ['https://www.linio.com.pe/search?scroll=&q=mouse']

    # Tiempo de espera entre cada requerimiento. Nos ayuda a proteger nuestra IP.
    download_delay = 2

    # Tupla de reglas para direccionar el movimiento de nuestro Crawler a traves de las paginas
    rules = (
        Rule( # Regla de movimiento VERTICAL hacia el detalle de los hoteles
            LinkExtractor(
                allow=r'/p/' # Si la URL contiene este patron, haz un requerimiento a esa URL
            ), follow=True, callback="parse_product"), # El callback es el nombre de la funcion que se va a llamar con la respuesta al requerimiento hacia estas URLs
    )

    # Funcion a utilizar con MapCompose para realizar limpieza de datos
    # def quitarDolar(self, texto):
    #     return texto.replace("$", "")

    # Callback de la regla
    def parse_product(self, response):
        sel = Selector(response)

        item = ItemLoader(News(), sel)
        item.add_xpath('name', '//span[@class="product-name"]/text()')
        item.add_xpath('price', '//div[@class="product-price"]//span[@class="price-main-md"]/text()')
        #,MapCompose(self.quitarDolar)
        # Utilizo Map Compose con funciones anonimas
        # PARA INVESTIGAR: Que son las funciones anonimas en Python?
        item.add_xpath('features', '//ul/li/text()')
        
        yield item.load_item()

# EJECUCION
# scrapy runspider 1_tripadvisor.py -o tripadvisor.csv