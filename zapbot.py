from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import schedule
import requests
from bs4 import BeautifulSoup

# WEBCRAWLER
response = requests.get('https://www.giromarilia.com.br/secao/cidade/giro-marilia/4/41')
content = response.content
site = BeautifulSoup(content, 'html.parser' )

titulos = site.find_all('h4', class_='card-title')
links = site.find_all('div', class_ = 'card')
mensagem_enviada = []
for i in range(len(titulos)):
    titulo = titulos[i].get_text()
    link_tag = links[i].find('a')
    if link_tag:
        link = link_tag['href']

# BOT
class WhatsappBot:
    def __init__(self):
        self.mensagem = link # mensagem enviada
        self.grupos = ["testezap"] # grupo onde vai enviar a mensagem
        options = webdriver.ChromeOptions() # consiguração do webdriver
        options.add_argument('lang=pt-br')
        self.driver = webdriver.Chrome(options=options)
    def EnviarMensagens(self): # função para enviar a mensagem
        self.driver.get('https://web.whatsapp.com/')
        time.sleep(30)
        for grupo in self.grupos:
            grupo = self.driver.find_element(by=By.XPATH, value='//*[@id="pane-side"]/div/div/div/div[1]/div/div/div/div[2]/div[1]/div[1]/span')   # XPATH do grupo
            time.sleep(3)
            grupo.click() # clica no grupo
            
            chat_box = self.driver.find_element(by=By.XPATH, value='//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]')   # XPATH do chat
            time.sleep(3)
            chat_box.click()
            chat_box.send_keys(self.mensagem) # clica no chat
            
            botao_enviar = self.driver.find_element(by=By.XPATH, value='//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button/span')  # XPATH do botão enviar
            time.sleep(3)
            botao_enviar.click() # clica no botão enviar
            time.sleep(5)
bot = WhatsappBot()

# Agende a execução do bot para um horário específico (por exemplo, todos os dias às 10:00 da manhã)
schedule.every().day.at("16:46").do(bot.EnviarMensagens)

while True:
    schedule.run_pending()
    time.sleep(1)