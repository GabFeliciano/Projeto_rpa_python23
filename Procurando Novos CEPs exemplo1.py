import time

from selenium import webdriver as opcoesSelenium
from selenium.webdriver.common.by import By

import pyautogui as tempoEspera

navegador = opcoesSelenium.Chrome()
navegador.get("https://buscacepinter.correios.com.br/app/endereco/index.php")

tempoEspera.sleep(2)

dictEndereco = {
    "CEP 1":"05876100",
    "CEP 2":"05876249",
    "CEP 3":"05876269"
}

navegador.find_element(By.ID, "endereco").send_keys("05869240")
tempoEspera.sleep(5)

navegador.find_element(By.NAME, "btn_pesquisar").click()

tempoEspera.sleep(10)

#for para percorrer os elementos e trazer os resultados
for contador in dictEndereco.values():

    tempoEspera.sleep(6)

    navegador.find_element(By.ID, 'btn_nbusca').click()

    tempoEspera.sleep(6)

    navegador.find_element(By.NAME, "endereco").send_keys(contador)

    tempoEspera.sleep(6)

    navegador.find_element(By.NAME, "btn_pesquisar").click()

    tempoEspera.sleep(6)

    # variavel et recebe navegador para pegar o XPATH para procurar os elementos do resultado da pesquisa cep
    elementoTabela = navegador.find_element(By.XPATH, '//*[@id="resultado-DNEC"]')

    #endereço vazio para não repetir a cada nova busca
    endereco = ""
    for linhaTab in elementoTabela.find_elements(By.TAG_NAME, 'tr'):

        for colunaTab in linhaTab.find_elements(By.TAG_NAME, 'td'):

            endereco = endereco + ";" + colunaTab.text


print(endereco)

print("Finalizado com sucesso!")
print("Tempo de execussão",time.process_time())
