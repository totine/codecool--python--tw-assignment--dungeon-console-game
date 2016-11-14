import sys
import os

os.system("printf '\033c'")
sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=30, cols=110))
PLAYER = "@"

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


plansza = tablica(25,86)
plansza[5][1] = "@"
position_x = 1
position_y = 1


def player_position(lista,pos1,pos2):
    x = [(index, row.index("@")) for index, row in enumerate(lista) if "@" in row]
    print(x)
    print(x[0][0])
    lista [pos1][pos2] = "@"
    lista [x[0][0]][x[0][1]] = "."
    return lista

plansza = player_position(plansza,position_x,position_y)


drukowanie_tablicy(plansza)

while 1:
    def getch():
        import sys, tty, termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

    x = getch()

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



    plansza = player_position(plansza,position_x,position_y)

    os.system("printf '\033c'")
    drukowanie_tablicy(plansza)
