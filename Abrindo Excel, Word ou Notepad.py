import pyautogui as escolhaOpcao

opcao = escolhaOpcao.confirm('Clique no Botão desejado!',
        buttons=['Excel', 'Word', 'Notepad'])

if opcao == "Excel":
    escolhaOpcao.hotkey('Win', 'r')

    escolhaOpcao.sleep(2)

    escolhaOpcao.typewrite('Excel')

    escolhaOpcao.sleep(1)

    escolhaOpcao.press('enter')

    escolhaOpcao.sleep(3)

    escolhaOpcao.moveTo(x=307, y=212)                                         #print(escolhaOpcao.position())

    escolhaOpcao.sleep(2)

    escolhaOpcao.click(x=307, y=212)

    escolhaOpcao.sleep(2)

    escolhaOpcao.typewrite('Escolhi o Excel e estou escrevendo aqui!')

    escolhaOpcao.sleep(3)

    fechandoAba = escolhaOpcao.getActiveWindow()

    fechandoAba.close()

    escolhaOpcao.sleep(1)

    escolhaOpcao.press('tab')

    escolhaOpcao.sleep(2)

    escolhaOpcao.press('enter')

    print("Você escolheu a opção Excel.")


elif opcao == "Word":
    escolhaOpcao.hotkey('Win', 'r')

    escolhaOpcao.sleep(2)

    escolhaOpcao.typewrite('WinWord')

    escolhaOpcao.press('enter')

    escolhaOpcao.sleep(3)

    escolhaOpcao.moveTo(x=448, y=345)

    escolhaOpcao.sleep(2)

    escolhaOpcao.click(x=448, y=345)

    escolhaOpcao.sleep(2)

    escolhaOpcao.typewrite('Ola Gabriel, parabens por conseguir mais um objetivo em RPA com Python e pyautogui.')

    escolhaOpcao.sleep(3)

    fechandoJanela = escolhaOpcao.getActiveWindow()

    fechandoJanela.close()

    escolhaOpcao.sleep(2)

    escolhaOpcao.press('tab')

    escolhaOpcao.sleep(2)

    escolhaOpcao.press('enter')

    print("Você escolheu a opção Word.")

else:
    escolhaOpcao.hotkey('Win','r')

    escolhaOpcao.sleep(2)

    escolhaOpcao.typewrite('Notepad')

    escolhaOpcao.press('enter')

    escolhaOpcao.sleep(1)

    escolhaOpcao.typewrite('Ola Gabriel, parabens por conseguir mais um objetivo com Python e pyautogui.')

    escolhaOpcao.sleep(3)

    fechandoAba = escolhaOpcao.getActiveWindow()

    fechandoAba.close()

    escolhaOpcao.sleep(2)

    escolhaOpcao.press('tab')

    escolhaOpcao.sleep(2)

    escolhaOpcao.press('enter')

    print("Voçê escolheu a opção Notepad.")
