from PPlay.window import *
from PPlay.sprite import *
from PPlay.mouse import *
from PPlay.keyboard import *
from PPlay.gameimage import *
from game import jogo
from ranking import tela_ranking

janela = Window(1224,822)
mouse = Window.get_mouse()
teclado = keyboard.Keyboard()
velx = 200

logo = Sprite("lg.png")
logo.x = janela.width/2 - logo.width/2
logo.y = 100

fundo = GameImage("fundo.png")
fundo.set_position(200,0)

start = Sprite("strt.png")
start.x = janela.width/2 - start.width/2
start.y = janela.height/1.53

startred = Sprite("strtred.png")
startred.x = janela.width/2 - startred.width/2
startred.y = janela.height/1.53

rank = Sprite("rank.png")
rank.x = janela.width/2 - rank.width/2
rank.y = janela.height/1.38

rankred = Sprite("rankred.png")
rankred.x = janela.width/2 - rankred.width/2
rankred.y = janela.height/1.38

opt = Sprite("opt.png")
opt.x = janela.width/2 - opt.width/2
opt.y = janela.height/1.25

optred = Sprite("optred.png")
optred.x = janela.width/2 - optred.width/2
optred.y = janela.height/1.25

qt = Sprite("quit.png")
qt.x = janela.width/2 - qt.width/2.3
qt.y = janela.height/1.15

qtred = Sprite("quitred.png")
qtred.x = janela.width/2 - qtred.width/2.3
qtred.y = janela.height/1.15

while True:
    janela.set_background_color((0, 0, 0))
    fundo.draw()

    if (mouse.is_over_object(start)):
        start.hide()
        startred.draw()
        if (mouse.is_button_pressed(1)):
            jogo()
    else:
        start.unhide()

    if (mouse.is_over_object(opt)):
        opt.hide()
        optred.draw()
        if (mouse.is_button_pressed(1)):
            break
    else:
        opt.unhide()

    if (mouse.is_over_object(rank)):
        rank.hide()
        rankred.draw()
        if (mouse.is_button_pressed(1)):
            tela_ranking()
    else:
        rank.unhide()

    if (mouse.is_over_object(qt)):
        qt.hide()
        qtred.draw()
        if (mouse.is_button_pressed(1)):
            break
    else:
        qt.unhide()

    logo.draw()
    start.draw()
    rank.draw()
    qt.draw()
    opt.draw()
    janela.update()