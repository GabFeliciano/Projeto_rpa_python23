import pyautogui as posicaoMouse
import pyautogui as tempoEspera

#tempo de espera para que o computador possa pensar \ #print(posicaoMouse.position())
tempoEspera.sleep(2)

#descobrindo as coordenadas do mouse(x,y) para mover ate o botão iniciar
posicaoMouse.moveTo(x=25, y=747)

#tempo de espera para que o computador possa pensar
tempoEspera.sleep(1)
#posicao do mouse para o clique
posicaoMouse.click(25, 747)

tempoEspera.sleep(2)

posicaoMouse.typewrite('Google Chrome')

tempoEspera.sleep(2)
#clicando no app Google
posicaoMouse.press('enter')

tempoEspera.sleep(2)
#movendo o mouse para posição modo visitante
posicaoMouse.moveTo(x=243, y=640)

tempoEspera.sleep(3)

#print(posicaoMouse.position())
posicaoMouse.click(x=243, y=640)
tempoEspera.sleep(3)

posicaoMouse.typewrite('Dolar')
tempoEspera.sleep(2)

posicaoMouse.moveTo(x=204, y=87)
#print(posicaoMouse.position())
posicaoMouse.click(x=204, y=87)
