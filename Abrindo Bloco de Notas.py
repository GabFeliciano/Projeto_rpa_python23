import pyautogui as abreArquivos

abreArquivos.sleep(1)
#hotkey pressiona tecla ou mais de uma / Win + r para pesquisa rapida
abreArquivos.hotkey('Win','r')

abreArquivos.sleep(2)
abreArquivos.typewrite('notepad')

abreArquivos.sleep(1)
abreArquivos.press('enter')

abreArquivos.sleep(2)

#mensagem exibida no notepad
abreArquivos.typewrite('Abri o Bloco de notas com o pyautogui do Python e estou programando esse '
                       'robozinho aqui rs!!')
abreArquivos.sleep(3)

#movendo o mouse para x (fechar a janela)
#abreArquivos.moveTo(x=1022, y=32)
#print(abreArquivos.position())

abreArquivos.sleep(1)

#outra maneira de fechar a janela criando uma var e com o metodo .getActiveWindow()
fechandoArquivo = abreArquivos.getActiveWindow()
abreArquivos.sleep(2)

fechandoArquivo.close()

#executando click de fechamento de janela(X)
#abreArquivos.click(x=1022, y=32)

abreArquivos.sleep(2)

#tab para trocar de botão SIM para NÂO SALVAR
abreArquivos.press('tab')

abreArquivos.sleep(2)

#pressionando não salvar
abreArquivos.press('enter')

print("Automação concluida com sucesso!!")