import requests
from bs4 import BeautifulSoup

def extrair_texto(link):
    response_texto = requests.get(link)
    if response_texto.status_code == 200:
        content_texto = response.content
        texto = BeautifulSoup(content, 'html.parser')
        paragrafos = texto.find_all('p')
        for paragrafo in paragrafos:
            print(paragrafo.get_text())


response = requests.get('https://www.giromarilia.com.br/secao/cidade/giro-marilia/4/41')
content = response.content
site = BeautifulSoup(content, 'html.parser' )

titulos = site.find_all('h4', class_='card-title')
links = site.find_all('div', class_ = 'card')

for i in range(len(titulos)):
    titulo = titulos[i].get_text()
    link_tag = links[i].find('a')
    if link_tag:
        link = link_tag['href']
        print(titulo)
        print()
        print(link)
        print()
        #extrair_texto(link)