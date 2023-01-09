import requests
from bs4 import BeautifulSoup

# Hacer una solicitud a la página web
headers = {
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.80 Chrome/71.0.3578.80 Safari/537.36",
}
url_reddit='https://www.reddit.com/r/StableDiffusion/'
url_ramen='https://ramenparados.com/category/articulos-y-resenas/resenas/'
response = requests.get(url_ramen,headers=headers)
# Parsear el contenido de la respuesta con lxml
soup = BeautifulSoup(response.text, 'html.parser')

# Buscar un elemento con una clase específica
question_title=soup.find_all(class_='widget-full-list-text')
# Imprimir el contenido del elemento
for title in question_title:
     text=title.text
     text=text.replace('\r','').strip()
     print(text)
     print()
