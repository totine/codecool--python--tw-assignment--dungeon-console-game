import sys
import os

os.system("printf '\033c'")
sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=30, cols=110))

def terrain(x, y):
    matrix = []
    for row in range(x):
        matrix.append([])
        for kolumn in range(y):
            if row == 0 or row == x-1 or kolumn == 0 or kolumn == y-1:
                matrix[row].append('x')
            else:
                matrix[row].append('.')
    return matrix


def display_terrain(matrix):
    for i in matrix:
        print(''.join(i).rjust(105, " "))


board = terrain(25,86)
board[5][1] = "@"
position_x = 1
position_y = 1


def player_position(matrix,pos1,pos2):
    x = [(index, row.index("@")) for index, row in enumerate(matrix) if "@" in row]
    x = x[0]
    matrix [pos1][pos2] = "@"
    matrix [x[0]][x[1]] = "."
    return matrix

board = player_position(board,position_x,position_y)


display_terrain(board)

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
    if x == "s":
        position_x = position_x + 1
    if x == "a":
        position_y = position_y - 1
    if x == "d":
        position_y = position_y + 1



    board = player_position(board,position_x,position_y)

    os.system("printf '\033c'")
    display_terrain(board)
