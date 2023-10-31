import pyautogui
import time

# Espera um tempo para você alternar para a janela do WhatsApp Desktop
time.sleep(5)

# Link de convite do grupo do WhatsApp
group_link = "testezap"  # Substitua pelo link do grupo real

# Mensagem que você deseja enviar
message = "https://marilianoticia.com.br/cestas-natalinas-para-servidores-municipais-devem-custar-r-54-milhoes-aos-cofres-publicos/"

# Hora do envio (formato 24 horas)
hour = 20  # Hora
minute = 39  # Minuto

# Função para enviar a mensagem para o grupo
def send_whatsapp_message_to_group():
    # Abre o grupo usando o link de convite
    pyautogui.hotkey('alt', 'tab')  # Abre uma nova janela
    time.sleep(2)
    pyautogui.hotkey('ctrl', 'f')  # Abre uma nova janela
    time.sleep(2)
    pyautogui.write(group_link)
    time.sleep(1)
    pyautogui.hotkey('Down')  # Abre uma nova janela
    time.sleep(2)
    pyautogui.press('enter')
    time.sleep(5)  # Aguarde a abertura do grupo

    # Digita a mensagem e a envia
    pyautogui.write(message)
    time.sleep(1)
    pyautogui.press('enter')

# Execute a função para enviar a mensagem para o grupo
send_whatsapp_message_to_group()