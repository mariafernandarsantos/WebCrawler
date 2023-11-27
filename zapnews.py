from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import schedule
import requests
from bs4 import BeautifulSoup


# Função para obter notícias do site
def obter_noticias():
    response = requests.get('https://www.giromarilia.com.br/secao/cidade/giro-marilia/4/41')
    content = response.content
    site = BeautifulSoup(content, 'html.parser')
    
    titulos = site.find_all('h4', class_='card-title')
    links = site.find_all('div', class_='card')
    
    noticias = []
    for i in range(len(titulos)):
        titulo = titulos[i].get_text().upper()
        link_tag = links[i].find('a')
        if link_tag:
            link = link_tag['href']
            noticia = titulo + '    ' + link
            noticias.append(noticia)
    return noticias

# Função para carregar notícias já enviadas a partir do arquivo
def carregar_noticias_enviadas():
    try:
        with open('noticias_enviadas.txt', 'r') as arquivo:
            noticias_enviadas = arquivo.read().splitlines()
        return noticias_enviadas
    except FileNotFoundError:
        return []

# Função para salvar notícias enviadas no arquivo
def salvar_noticias_enviadas(noticias):
    with open('noticias_enviadas.txt', 'a') as arquivo:
        for noticia in noticias:
            arquivo.write(noticia + '\n')

# Classe WhatsappBot
class WhatsappBot:
    def __init__(self):
        self.grupos = ["testezap"]
        options = webdriver.ChromeOptions()
        options.add_argument('lang=pt-br')
        self.driver = webdriver.Chrome(options=options)

    def enviar_mensagens(self):
        self.driver.get('https://web.whatsapp.com/')
        time.sleep(30)

        noticias = obter_noticias()
        noticias_enviadas = carregar_noticias_enviadas()

        for grupo in self.grupos:
            grupo = self.driver.find_element(by=By.XPATH, value="//span[@title='testezap']")
                                             
            time.sleep(3)
            grupo.click()

            chat_box = self.driver.find_element(by=By.XPATH, value='//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]')
                                                
            time.sleep(3)

            for noticia in noticias:
                if noticia not in noticias_enviadas:
                    chat_box.click()
                    chat_box.send_keys(noticia)

                    botao_enviar = self.driver.find_element(by=By.XPATH, value='//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button/span')
                                                             
                    time.sleep(3)
                    botao_enviar.click()

                    time.sleep(5)
                    noticias_enviadas.append(noticia)

        # Salvar apenas as notícias novas enviadas
        noticias_novas_enviadas = [noticia for noticia in noticias_enviadas if noticia in noticias]
        salvar_noticias_enviadas(noticias_novas_enviadas)

# Criar uma instância do WhatsappBot
bot = WhatsappBot()

# Agendar a execução do bot para um horário específico
schedule.every().day.at("13:00").do(bot.enviar_mensagens)

while True:
    schedule.run_pending()
    time.sleep(1)