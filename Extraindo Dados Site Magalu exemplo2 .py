from selenium import webdriver as opcoesSelenium
from selenium.webdriver.common.by import By

import pyautogui as tempoEspera
import pyautogui as funcoesTeclado

navegador = opcoesSelenium.Chrome()

navegador.get("https://www.magazineluiza.com.br/")

#procura pelo campo ID, seu nome -id, e digita na barra de pesquisa o nome do produto
navegador.find_element(By.ID, "input-search").send_keys("geladeira")

tempoEspera.sleep(2)

funcoesTeclado.press("enter")

tempoEspera.sleep(10)

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
        #sc-kDvujY jDmBNY sc-hGglLj bQqJoc
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


print("Programa finalizado com sucesso!")