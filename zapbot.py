from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class WhastappBot:
    def __init__(self):
        self.mensagem = " Teste do bot ok TESTANDO O BOT APENAS é teste, segura o link https://www.ofuxico.com.br/reality-show/a-fazenda/a-fazenda-15-ofendi-todo-mundo-diz-simioni-sobre-trajetoria"
        self.grupos = ["testezap"]
        options = webdriver.ChromeOptions()
        options.add_argument('lang=pt-br')
        self.driver = webdriver.Chrome(options=options)

    def EnviarMensagens(self):
        # <span dir="auto" title="testezap" aria-label="" class="ggj6brxn gfz4du6o r7fjleex g0rxnol2 lhj4utae le5p0ye3 l7jjieqr _11JPr" style="min-height: 0px;">testezap</span>
        # <div tabindex="-1" class="_3Uu1_">
        # <span data-icon="send" class="">
        self.driver.get('https://web.whatsapp.com')
        time.sleep(30)
        for grupo in self.grupos:
            grupo = self.driver.find_element(by=By.XPATH, value = "//span[@title='testezap']")
            time.sleep(3)
            grupo.click()
            chat_box= self.driver.find_element(by=By.XPATH, value = "//div[@class='_3Uu1_']")
            time.sleep(3)
            chat_box.click()
            chat_box.send_keys(self.mensagem)
            botao_enviar = self.driver.find_element(by=By.XPATH, value =  "//span[@data-icon='send']D")
            time.sleep(3)
            botao_enviar.click()
            time.sleep(5)

bot = WhastappBot()
bot.EnviarMensagens()