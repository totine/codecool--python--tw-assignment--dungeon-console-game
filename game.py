import sys
import os


os.system("printf '\033c'")
sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=30, cols=110))
position_x = 1
position_y = 1


def background(x, y):
    matrix = []
    for row in range(x):
        matrix.append([])
        for column in range(y):
            if row == 0 or row == x-1 or column == 0 or column == y-1:
                matrix[row].append('x')
            else:
                matrix[row].append('.')
    return matrix


def display_background(matrix):
    for i in matrix:
        print(''.join(i).rjust(105, " "))


def player_position(matrix, pos1, pos2):
    x = [(index, row.index("@")) for index, row in enumerate(matrix) if "@" in row]
    x = x[0]
    matrix[pos1][pos2] = "@"
    matrix[x[0]][x[1]] = "."
    return matrix


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
    if x == "s":
        position_x = position_x + 1
    if x == "a":
        position_y = position_y - 1
    if x == "d":
        position_y = position_y + 1


terrain = background(25, 86)
terrain[1][1] = "@"
display_background(terrain)


while 1:
    x = getch()
    user_input(x)
    terrain = player_position(terrain, position_x, position_y)
    os.system("printf '\033c'")
    display_background(terrain)