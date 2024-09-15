from selenium import webdriver as opcoesSelenium
from selenium.webdriver.common.by import By

import pandas as pd

navegador = opcoesSelenium.Chrome()

#abrindo site
navegador.get("https://rpachallengeocr.azurewebsites.net/")

#extraindo elementos do site
extElemento = navegador.find_element(By.XPATH, '//*[@id="tableSandbox_wrapper"]')

#acessando as linhas e colunas da tabela
linhas = extElemento.find_elements(By.TAG_NAME, 'tr')
colunas = extElemento.find_elements(By.TAG_NAME, 'td')

dataFramelistas = []

linha = 1

for linhaAtual in linhas:

    print(linhaAtual.text)
    dataFramelistas.append(linhaAtual.text)
    linha += 1

arquivoExcel = pd.ExcelWriter('dadosDoSite.xlsx', engine='xlsxwriter')
arquivoExcel.save()

dataFrame = pd.DataFrame(dataFramelistas, columns=['Dados'])

arquivoExcel = pd.ExcelWriter('dadosDoSite.xlsx', engine='xlsxwriter')

dataFrame.to_excel(arquivoExcel, sheet_name = 'Sheet1', index = True)

arquivoExcel.save()
