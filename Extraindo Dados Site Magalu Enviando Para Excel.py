from selenium import webdriver as opcoesSelenium
from selenium.webdriver.common.by import By

import pyautogui as tempoEspera
import pyautogui as funcoesTeclado

import pandas as pd

navegador = opcoesSelenium.Chrome()

navegador.get("https://www.magazineluiza.com.br/")

#procura pelo campo ID, seu nome -id, e digita na barra de pesquisa o nome do produto
navegador.find_element(By.ID, "input-search").send_keys("geladeira")

tempoEspera.sleep(2)

funcoesTeclado.press("enter")

tempoEspera.sleep(10)

listaDataFrame = []

listaProdutos = navegador.find_elements(By.CLASS_NAME, "fwviCj")


for item in listaProdutos:

    nomeProduto = ""
    precoProduto = ""
    urlProduto = ""

    if nomeProduto == "":
        #sc-hFVsQR hQYVAI
        try:
            nomeProduto = item.find_element(By.CLASS_NAME, "sc-hFVsQR").text
        except Exception:
            pass

    elif nomeProduto == "":

        try:
            nomeProduto = item.find_element(By.CLASS_NAME, "hQYVAI").text
        except Exception:
            pass
    #------------------------------precoProduto-----------------------------------------

    if precoProduto == "":
        # sc-hLBbgP blWoJz sc-gGfaQS dhvIhC     $sc-kDvujY jDmBNY sc-hGglLj bQqJoc

        try:
            precoProduto = item.find_element(By.CLASS_NAME, "bQqJoc ").text
        except Exception:
            pass
    elif precoProduto == "":
        try:
            precoProduto = item.find_element(By.CLASS_NAME, "sc-hGglLj ").text
        except Exception:
            pass

    elif precoProduto == "":
        try:
            precoProduto = item.find_element(By.CLASS_NAME, "sc-kDvujY").text
        except Exception:
            pass
    elif precoProduto == "":
        try:
            precoProduto = item.find_element(By.CLASS_NAME, "jDmBNY ").text
        except Exception:
            pass
    else:
        precoProduto = '0'
    #------------------------------urlProduto--------------------------------------------

    if urlProduto == "":
        try:
            urlProduto = item.find_element(By.TAG_NAME, "a ").get_attribute("href")
        except Exception:
            pass

    else:
        urlProduto = "-"


    print(nomeProduto,"-", precoProduto)
    print(urlProduto)
    dadosLinha = nomeProduto + ";" + precoProduto + ";" + urlProduto

    # Populando o DataFrame com as informações
    listaDataFrame.append(dadosLinha)

arquivoExcel = pd.ExcelWriter('dadosMagalu.xlsx', engine='xlsxwriter')
arquivoExcel.save()

dataFrame = pd.DataFrame(listaDataFrame, columns=['Descrição;Preço;Url'])

# Prepara o arquivo do Excel usando xlsxwriter como mecanismo
arquivoExcel = pd.ExcelWriter('dadosMagalu.xlsx', engine='xlsxwriter')

dataFrame.to_excel(arquivoExcel, sheet_name='Dados', index=False)

# Salva as informações no arquivo de Excel
arquivoExcel.save()

print("Programa finalizado com sucesso!")