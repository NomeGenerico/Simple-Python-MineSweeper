# -*- coding: utf-8 -*-

# This is my first Project, form calculators to this, no tutorials. Fell free to fork

# Ps: Sorry for this monstrosity

# Ps: Ps: Will try to implement list containing themselfs.
import Generator
import Render

tam = 0


def wincheck(renderboard, mineboard):
    i = 1
    j = 1
    win = True

    while i < len(renderboard) - 1:
        j = 1
        while j < len(renderboard) - 1:
            if mineboard[i][j] == 0:
                if renderboard[i][j] != 1:
                    win = False
            j = j+1
        i = i+1
    return win


def myinput():
    ended = False
    while ended == False:
        valid = False
        while valid == False:
            try:
                y, x = input("faça uma jogada: ").split()
                y, x = int(y), int(x)
                valid = True
                return x, y
            except:
                valid = False


def game():
    print("1 - Easy")
    print("2 - Medium")
    print("3 - Hard")
    print("4 - Custom")

    choice = int(input())

    if choice == 1:
        tam = 8
        dif = 10
    if choice == 2:
        tam = 16
        dif = 40
    if choice == 3:
        tam = 20
        dif = 99
    if choice == 4:
        notValid = True
        while(notValid):
            try: 
            	tam = int(input("Tamanho do tabuleiro: "))
            	dif = int(input("Numero de Minas: "))
            	print("Número de minas inválido")
            	if(dif < tam**2):
                	notValid = False
            except:
            	print("Digite Apenas Numeros")

    firstmove = True
    mineboard = Generator.GerarMinas(tam, dif)
    numboard = Generator.MineCounterBoard(mineboard, tam)
    renderboard = Render.DefRenderBoard(tam)
    Render.Numboard(numboard, renderboard, tam)
    ended = False

    while ended == False:
        x, y = myinput()
        Generator.firstmovecheck(mineboard, x, y, tam, firstmove)
        firstmove = False

        if mineboard[y][x] == -1:
            ended == True
            print("Você Perdeu")
            return
        renderboard = Render.updateRenderBoard(
            numboard, renderboard, x, y, tam)
        Render.Numboard(numboard, renderboard, tam)
        if wincheck(renderboard, mineboard):
            print("Você Ganhou")
            return


game()
