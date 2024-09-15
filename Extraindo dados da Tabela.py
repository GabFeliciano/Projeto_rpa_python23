from selenium import webdriver as opcoesSelenium
from selenium.webdriver.common.by import By

navegador = opcoesSelenium.Chrome()

#abrindo site
navegador.get("https://rpachallengeocr.azurewebsites.net/")

extElemento = navegador.find_element(By.XPATH, '//*[@id="tableSandbox_wrapper"]')

linhas = extElemento.find_elements(By.TAG_NAME, 'tr')
colunas = extElemento.find_elements(By.TAG_NAME, 'td')

linha = 1

for linhaAtual in linhas:

    print(linhaAtual.text)
    linha += 1
