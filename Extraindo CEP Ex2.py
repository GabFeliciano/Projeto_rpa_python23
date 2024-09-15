import time

from selenium import webdriver as opcoesSelenium
from selenium.webdriver.common.by import By

import pyautogui as tempoEspera

navegador = opcoesSelenium.Chrome()
navegador.get("https://buscacepinter.correios.com.br/app/endereco/index.php")
tempoEspera.sleep(4)

navegador.find_element(By.ID, "endereco").send_keys("05869240")
tempoEspera.sleep(4)

navegador.find_element(By.NAME, "btn_pesquisar").click()

tempoEspera.sleep(3)
#variavel et recebe navegador para pegar o XPATH para procurar os elementos do resultado da pesquisa cep
elementoTabela = navegador.find_element(By.XPATH, '//*[@id="resultado-DNEC"]')

#for para percorrer os elementos e trazer os resultados
for linhaTab in elementoTabela.find_elements(By.TAG_NAME, 'tr'):
    endereco = ""
    for colunaTab in linhaTab.find_elements(By.TAG_NAME, 'td'):
        endereco = endereco + ";" + colunaTab.text

print(endereco)

print("Finalizado com sucesso!")
print("Tempo de execussão",time.process_time())
