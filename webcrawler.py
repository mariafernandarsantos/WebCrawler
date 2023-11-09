import time
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
import pyperclip
import spacy

# PROCURAR A INFORMAÇÃO NO CHROME
url = "https://www.uol.com.br/"

option = Options()
option.headless = True
driver = webdriver.Firefox()
driver.get(url)
time.sleep(3)

apertar = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[4]/section[2]/div/div/div[1]/div/div[1]/div/div/div/div/div[1]/div/div[1]/article/a/figure")
apertar.click()

elemento_texto = driver.find_element(By.XPATH, "/html/body/div[1]/main/article/div[1]/div[2]/div/div/div[2]/p[1]")
texto = elemento_texto.text
pyperclip.copy(texto)
driver.quit()

print(texto)