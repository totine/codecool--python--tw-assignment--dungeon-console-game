import sys
import os


os.system("printf '\033c'")
sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=30, cols=110))
PLAYER = "@"
position_x = 1
position_y = 1


def tablica(x, y):
    lista = []
    for rzad in range(x):
        lista.append([])
        for kolumn in range(y):
            if rzad == 0 or rzad == x-1 or kolumn == 0 or kolumn == y-1:
                lista[rzad].append('x')
            else:
                lista[rzad].append('.')
    return lista


def drukowanie_tablicy(lista):
    for i in lista:
        print(''.join(i).rjust(105, " "))


def player_position(lista, pos1, pos2):
    x = [(index, row.index("@")) for index, row in enumerate(lista) if "@" in row]
    lista[pos1][pos2] = "@"
    lista[x[0][0]][x[0][1]] = "."
    return lista


def getch():
    import sys
    import tty
    import termios
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch


def user_input(x):
    global position_x, position_y
    if x == "w":
        position_x = position_x - 1
        position_y = position_y
    if x == "s":
        position_x = position_x + 1
        position_y = position_y
    if x == "a":
        position_x = position_x
        position_y = position_y - 1
    if x == "d":
        position_x = position_x
        position_y = position_y + 1


plansza = tablica(25, 86)
plansza[1][1] = "@"
drukowanie_tablicy(plansza)


while 1:
    x = getch()
    user_input(x)
    plansza = player_position(plansza, position_x, position_y)
    os.system("printf '\033c'")
    drukowanie_tablicy(plansza)
