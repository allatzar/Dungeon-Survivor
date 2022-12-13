from PPlay.window import *
from PPlay.gameimage import *


janela = Window(1224,822)
mouse = Window.get_mouse()
teclado = keyboard.Keyboard()
player = []

'''def sort():
    for i in range(len(players)):
        for j in range(i, len(players)):
            if int(players[j][1]) > int(players[i][1]):
                temp = players[i][0]
                temp2 = players[i][1]
                players[i][0] = players[j][0]
                players[i][1] = players[j][1]
                players[j][0] = temp
                players[j][1] = temp2'''


def tela_ranking():
#    fundo = GameImage('fundo.png')
    with open('ranking.txt', 'r') as arquivo:
        l = arquivo.readlines()
        for linha in l:
            a = linha.rstrip('\n')
            player.append(a)
#    sort()
    while True:
#        fundo.draw()
        if (teclado.key_pressed("ESC")):
            break
        for i in range(len(player)):
            if i == 5:
                break
            janela.draw_text(player[i], janela.width/2-140, 80*(i+1), size=55, color=(255, 255, 255))

        janela.update()