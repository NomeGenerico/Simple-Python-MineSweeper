import random


def Gerar0Board(tam):
    board = []
    x = []
    i = 0
    j = 0
    while i < (tam + 2):
        x.append(0)
        i = i + 1
    while j < (tam + 2):
        j = j+1
        board.append(x[:])
    return board


def GerarMinas(tam, dif):
    mineboard = Gerar0Board(tam)
    i = 0
    while i < dif:
        x = random.randint(1, (tam))
        y = random.randint(1, (tam))
        if mineboard[y][x] != -1:
            mineboard[y][x] = -1
            i = i + 1
    return mineboard


def MinecounterSquare(board, x, y):
    i = -1
    j = -1
    runningtotal = 0
    while i < 2:
        while j < 2:
            runningtotal = board[y + i][x + j] + runningtotal
            j = j + 1
        i = i + 1
        j = - 1
    return (runningtotal * -1) + board[y][x]

# Might be useful for "rendering" the board


def MineCounterBoard(mineboard, tam):
    y = 1
    x = 1
    board = Gerar0Board(tam)
    while y < tam + 1:
        while x < tam + 1:
            board[y][x] = MinecounterSquare(mineboard, x, y)
            x = x + 1
        y = y + 1
        x = 1
    return board


def firstmovecheck(mineboard, x, y, tam, firstmove):
    if firstmove:
        Sx, Sy = x, y
        if mineboard[y][x] == -1:
            i = 0
            while i < 1:
                x = random.randint(1, (tam))
                y = random.randint(1, (tam))
                if mineboard[y][x] != -1:
                    mineboard[y][x] = -1
                    i = i + 1
        mineboard[Sy][Sx] = 0
