"""
OBJETIVOS: 
    - Extraer los idiomas de la pagina principal de WIKIPEDIA
    - Aprender a utilizar requests para hacer requerimientos
    - Aprender a utilizar lxml para parsear el arbol HTML
CREADO POR: LEONARDO KUFFO
ULTIMA VEZ EDITADO: 12 ABRIL 2020
"""
import requests # pip install requests
from lxml import html # pip install lxml

def scrapping_text(url,xpath):
    # USER AGENT PARA PROTEGERNOS DE BANEOS
    headers = {
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.80 Chrome/71.0.3578.80 Safari/537.36",
    }
    # REQUERIMIENTO AL SERVIDOR
    respuesta = requests.get(url, headers=headers)
    # PARSEO DEL ARBOL HTML QUE RECIBO COMO RESPUESTA CON LXML
    parser = html.fromstring(respuesta.text)

    # EXTRACCION DE TODOS LOS IDIOMAS POR CLASE
    # titles = parser.find_class('featured-multi-sub-text')
    # for title in titles:
    #   print(title.text_content())

    # EXTRACCION DE TODOS LOS IDIOMAS POR XPATH
    titles = parser.xpath(f"{xpath}")
    for title in titles:
        print(title)

xpath='//h2/text()'
xpath_subtitle='//li[@class="infinite-post"]//a/text()'
xpath_wk="//h2/text()"
xpath_ann="//h3/a/text()"
# URL SEMILLA
url = 'https://ramenparados.com/'
url_categorias= "https://ramenparados.com/category/noticias/"
url_wk="https://wakaisekai.blogspot.com/"
url_ann="https://www.animenewsnetwork.com/"
scrapping_text(url_ann,xpath_wk)
