import pyautogui as posicaoMouse
import pyautogui as tempoEspera

#tempo de espera para que o computador possa pensar \ #print(posicaoMouse.position())
tempoEspera.sleep(2)

#descobrindo as coordenadas do mouse(x,y) para mover ate o botão iniciar
posicaoMouse.moveTo(x=25, y=747)

#tempo de espera para que o computador possa pensar
tempoEspera.sleep(2)
#posicao do mouse para o clique
posicaoMouse.click(25, 747)

#tempo de espera para que o computador possa pensar
tempoEspera.sleep(2)
#escrevendo Calculadora na barra de pesquisa
posicaoMouse.typewrite('Calculadora')

tempoEspera.sleep(2)

#print(posicaoMouse.position())

#clicando no programa da calculadora
posicaoMouse.click(x=84, y=304)
