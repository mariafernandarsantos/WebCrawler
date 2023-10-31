import requests
from bs4 import BeautifulSoup

# PARTE QUE O HILÁRIO PEDIU
def extrair_texto_main(link_main):
    response_texto_main = requests.get(link_main)
    if response_texto_main.status_code == 200:
        content_texto_main = response_texto_main.content
        texto_main = BeautifulSoup(content, 'html.parser')
        paragrafos_main = texto_main.find_all('p')
        for paragrafo_principal in paragrafos_main:
            print('\nTexto:', paragrafo_principal.get_text())

#PARTE QUE O HILÁRIO PEDIU

response = requests.get('https://www.uai.com.br/entretenimento/famosos/')
content = response.content
site = BeautifulSoup(content, 'html.parser' )

caixa_main = site.find_all('h2', class_= 'col-12 col-sm-10 standard-font color-black2 f21 bold ml-3-5')
url_link_main = site.find_all('article', class_ = 'noticia-chamada')
for i in range(len(caixa_main)):
    titulo_main = caixa_main[i].get_text()
    link_tag_main = url_link_main[i].find('a')
    if link_tag_main:
        link_main = link_tag_main['href']
        print('Link:', link_main)
        print('\nTítulo:', titulo_main)
        extrair_texto_main(link_main)
        

titulos = site.find_all('h3', class_ = 'mt-1 standard-font color-black2 f16 order-3')
links = site.find_all('article', class_ = 'noticia-pequena mb-4-5 d-flex d-sm-block')

for i in range(len(titulos)):
    titulo = titulos[i].get_text()
    link_tag = links[i].find('a')
    if link_tag:
        link = link_tag['href']
        print('\nLink:', link)
        print('\nTítulo:', titulo)