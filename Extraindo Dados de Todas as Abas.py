from selenium import webdriver as opcoesSelenium
from selenium.webdriver.common.by import By

import pyautogui as tempoDeEspera

navegador = opcoesSelenium.Chrome()

#abrindo site
navegador.get("https://rpachallengeocr.azurewebsites.net/")

linha = 1

i = 1

while i <= 3:

    extElemento = navegador.find_element(By.XPATH, '//*[@id="tableSandbox_wrapper"]')

    linhas = extElemento.find_elements(By.TAG_NAME, 'tr')
    colunas = extElemento.find_elements(By.TAG_NAME, 'td')

    for linhaAtual in linhas:
        print(linhaAtual.text)
        linha += 1

    i += 1

    tempoDeEspera.sleep(3)

    navegador.find_element(By.XPATH, '//*[@id="tableSandbox_next"]').click()

    tempoDeEspera.sleep(1)

else:
    print("Parabens, Dados extraidos com sucesso!!")