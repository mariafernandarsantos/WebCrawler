from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import schedule

class WhatsappBot:
    def __init__(self):
        self.mensagem = "TESTANDO O BOT AI CARALHO" # mensagem enviada
        self.grupos = ["testezap, testezap 2"] # grupo onde vai enviar a mensagem
        options = webdriver.ChromeOptions() # consiguração do webdriver
        options.add_argument('lang=pt-br')
        self.driver = webdriver.Chrome(options=options)
    def EnviarMensagens(self): # função para enviar a mensagem
        self.driver.get('https://web.whatsapp.com/')
        time.sleep(30)
        for grupo in self.grupos:
            grupo = self.driver.find_element(by=By.XPATH, value=f"//span[@title='testezap']")   # XPATH do grupo
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
schedule.every().day.at("18:37").do(bot.EnviarMensagens)

while True:
    schedule.run_pending()
    time.sleep(1)