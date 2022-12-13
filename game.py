from PPlay.window import *
from PPlay.sprite import *
from PPlay.mouse import *
from PPlay.keyboard import *
from PPlay.gameimage import *
from PPlay.collision import *


janela = Window(1224,822)
mouse = Window.get_mouse()
teclado = keyboard.Keyboard()
point = [0]

def cria_matriz(matriz, moeda, fundo):
    for a in range(16):
        for b in range(16):
            if matriz[a][b] == 0:
                moeda = Sprite("moeda.png")
                moeda.set_position(212+b*50+16,11+a*50+16)
                matriz[a][b] = moeda
            elif matriz[a][b] == 1:
                fundo = Sprite("pt2.png")
                fundo.set_position(212+b*50,11+a*50)
                matriz[a][b] = fundo


def desenha_moedas(matriz):
    for a in range(16):
        for b in range(16):
            if matriz[a][b] != "VAZIO":
                matriz[a][b].draw()

def colisao(matriz, gue, ME):
    for a in range(16):
        for b in range(16):
            if matriz[a][b] != "VAZIO":
                if gue.collided(matriz[a][b]):
                    if ME[a][b] == 0:
                        matriz[a][b] = "VAZIO"
                        point[0] = point[0]+1
                        return 1
                    if ME[a][b] == 1:
                        return -1
    return 0


def jogo():
    matriz = [
    [0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0],
    [1,1,1,0,1,0,0,0,1,0,1,0,1,1,1,0],
    [0,0,0,0,1,1,1,0,0,0,0,0,0,1,0,0],
    [1,0,1,0,0,0,0,0,1,0,1,0,1,1,1,0],
    [1,0,1,1,0,1,1,0,1,0,1,0,1,1,1,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [1,1,1,0,1,1,1,1,1,0,1,1,0,1,1,1],
    [0,0,0,0,1,1,1,1,1,0,0,1,0,0,0,0],
    [1,1,1,0,1,1,1,1,1,0,1,1,0,1,1,1],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [1,0,1,0,1,1,1,0,1,1,0,1,1,1,1,0],
    [0,0,1,0,0,0,1,0,1,1,0,0,0,0,0,0],
    [1,0,1,1,1,0,1,0,1,1,0,1,1,0,1,1],
    [1,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0],
    [1,0,1,0,1,0,1,0,1,1,0,1,1,0,1,0],
    [0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0]
    ]

    ME = [
    [0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0],
    [1,1,1,0,1,0,0,0,1,0,1,0,1,1,1,0],
    [0,0,0,0,1,1,1,0,0,0,0,0,0,1,0,0],
    [1,0,1,0,0,0,0,0,1,0,1,0,1,1,1,0],
    [1,0,1,1,0,1,1,0,1,0,1,0,1,1,1,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [1,1,1,0,1,1,1,1,1,0,1,1,0,1,1,1],
    [0,0,0,0,1,1,1,1,1,0,0,1,0,0,0,0],
    [1,1,1,0,1,1,1,1,1,0,1,1,0,1,1,1],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [1,0,1,0,1,1,1,0,1,1,0,1,1,1,1,0],
    [0,0,1,0,0,0,1,0,1,1,0,0,0,0,0,0],
    [1,0,1,1,1,0,1,0,1,1,0,1,1,0,1,1],
    [1,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0],
    [1,0,1,0,1,0,1,0,1,1,0,1,1,0,1,0],
    [0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0]
    ]
    fundo = Sprite("pt2.png")

    demon = Sprite("demon1.png", 4)
    demon.x = janela.width/2 - demon.width/2
    demon.y = janela.height/2 - demon.height

    gue = Sprite("guerreiro1.png", 4)
    gue.x = 462
    gue.y = 461

    borda = Sprite("borda.png")
    borda.set_position(200, 0)

    cantoe = Sprite("canto.png")
    cantoe.set_position(0,0)

    cantod = Sprite("canto.png")
    cantod.set_position(janela.width-200,0)

    moeda = Sprite("moeda.png")

    dir = 0
    ndir = 0
    
    cria_matriz(matriz, moeda, fundo)
    while True:
        if gue.x >= (janela.width+gue.width/2)-200:
            gue.set_position(200-gue.width,janela.height/2-50)
        elif gue.x <= 200-gue.width:
            gue.set_position(janela.width-200,janela.height/2-50)
        adir = dir
        if(teclado.key_pressed("UP")):
            ndir = 1
        if (teclado.key_pressed("DOWN")):
            ndir = 2
        if (teclado.key_pressed("LEFT")):
            ndir = 3
        if (teclado.key_pressed("RIGHT")):
            ndir = 4

        dir = ndir
        if dir == 1 and gue.y > 11:
            gue.move_y(-1)
            if colisao(matriz, gue, ME) == -1:
                gue.move_y(1)
                dir = adir 
                if dir == 3:
                    gue.move_x(-1)
                    if colisao(matriz, gue, ME) == -1:
                        gue.move_x(1)
                if dir == 4:
                    gue.move_x(1)
                    if colisao(matriz, gue, ME) == -1:
                        gue.move_x(-1)

        elif dir == 2 and gue.y < janela.height-gue.height-11:
            gue.move_y(1)
            if colisao(matriz, gue, ME) == -1:
                gue.move_y(-1)
                dir = adir
                if dir == 3:
                    gue.move_x(-1)
                    if colisao(matriz, gue, ME) == -1:
                        gue.move_x(1)
                if dir == 4:
                    gue.move_x(1)
                    if colisao(matriz, gue, ME) == -1:
                        gue.move_x(-1)

        elif dir == 3 and (gue.x > 212 or gue.y == janela.height/2-50):
            gue.move_x(-1)
            if colisao(matriz, gue, ME) == -1:
                gue.move_x(1)
                dir = adir
                if dir == 1:
                    gue.move_y(-1)
                    if colisao(matriz, gue, ME) == -1:
                        gue.move_y(1)
                if dir == 2:
                    gue.move_y(1)
                    if colisao(matriz, gue, ME) == -1:
                        gue.move_y(-1)
                    
        elif dir == 4 and (gue.x < janela.width-gue.width-212 or gue.y == janela.height/2-50):
            gue.move_x(1)
            if colisao(matriz, gue, ME) == -1:
                gue.move_x(-1)
                dir = adir
                if dir == 1:
                    gue.move_y(-1)
                    if colisao(matriz, gue, ME) == -1:
                        gue.move_y(1)
                if dir == 2:
                    gue.move_y(1)
                    if colisao(matriz, gue, ME) == -1:
                        gue.move_y(-1)


        if (teclado.key_pressed("ESC")):
            break

        janela.set_background_color((0, 0, 0))
        demon.draw()
        desenha_moedas(matriz)
        borda.draw()
        gue.draw()
        cantoe.draw()
        cantod.draw()
        janela.draw_text(str(point[0]), 20, 20, size=48, font_name="Arial", bold=True, color=[255, 255, 255])
        janela.update()