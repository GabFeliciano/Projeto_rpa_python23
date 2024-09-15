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

rua = navegador.find_element(By.XPATH, '//*[@id="resultado-DNEC"]/tbody/tr/td[1]').text
bairro = navegador.find_element(By.XPATH, '//*[@id="resultado-DNEC"]/tbody/tr/td[2]').text
localidade = navegador.find_element(By.XPATH, '//*[@id="resultado-DNEC"]/tbody/tr/td[3]').text
cep = navegador.find_element(By.XPATH, '//*[@id="resultado-DNEC"]/tbody/tr/td[4]').text

print("Rua:",rua)
print("Bairro:",bairro)
print("Localidade/UF:",localidade)
print("CEP:",cep)

print("/*""Finalizado com sucesso!")
print("Tempo de execussão",time.process_time())

