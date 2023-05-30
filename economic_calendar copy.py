import requests
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}


# URL de la página web
url = "https://nfs.faireconomy.media"

# Realizar una solicitud HTTP a la página web
response = requests.get(url, headers=headers)

# Analizar el contenido de la página con BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")

# Lista de divisas que queremos filtrar
divisas = ["USD", "CHF", "EUR", "AUD", "JPY", "GBP", "CAD", "NZD"]

# Lista para almacenar las noticias filtradas
noticias_filtradas = []

# Buscar todas las noticias (esto puede variar dependiendo de la estructura de la página web)
# Por ejemplo, supongamos que cada noticia está en un div con la clase "news-item"
for news_item in soup.find_all("div", class_="news-item"):
    # Comprobar si la noticia menciona alguna de las divisas deseadas
    for divisa in divisas:
        if divisa in news_item.text:
            # Si la noticia menciona una divisa deseada, añadirla a la lista
            noticias_filtradas.append(news_item.text)

# Imprimir las noticias filtradas
for noticia in noticias_filtradas:
    print(noticia)
