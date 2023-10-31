from selenium import webdriver

navegador = webdriver.Chrome()

navegador.get('https://www.youtube.com/watch?v=y7OhuSGBt8o&t=0s')
like = navegador.find_element_by_xpath('//*[@id="segmented-like-button"]/ytd-toggle-button-renderer/yt-button-shape/button/yt-touch-feedback-shape/div/div[2]').click()