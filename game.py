import sys
import os
import random


WINDOW_ROWS = 30
WINDOW_COLS = 110
RJUST_SIZE = 105
MOB_TYPES = ["A", "B", "C", "D", "E", "F"]

os.system("printf '\033c'")
sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=WINDOW_ROWS, cols=WINDOW_COLS))


def background(x, y):
    matrix = []
    for row in range(x):
        matrix.append([])
        for column in range(y):
            if row == 0 or row == x-1 or column == 0 or column == y-1:
                matrix[row].append('#')
            else:
                matrix[row].append('.')
    return matrix


def display_background(matrix):
    for i in matrix:
        print(''.join(i).rjust(RJUST_SIZE, " "))


"""def random_barriers(game_matrix, max_size=15):
    barrier_size_x = random.randint(1,max_size)
    barrier_size_y = random.randint(1,max_size)
    barrier_start_x = random.randint(1,len(game_matrix)-barrier_size_x)
    barrier_start_y = random.randint(1,len(game_matrix[0])-barrier_size_y)
    for i in range(barrier_start_x,barrier_start_x+barrier_size_x):
        for j in range(barrier_start_y,barrier_start_y+barrier_size_y):
            game_matrix[i][j] = "#"
    return game_matrix"""



def mobs_positions(game_matrix, mob_list):
    mob_pos_x = random.randint(1,24)
    mob_pos_y = random.randint(1,84)
    mob_type = random.choice(mob_list)
    if game_matrix[mob_pos_x][mob_pos_y] != "#":
        game_matrix[mob_pos_x][mob_pos_y] = mob_type
    return game_matrix


def player_position(matrix, pos1, pos2):
    old_player_pos = [(index, row.index("@")) for index, row in enumerate(matrix) if "@" in row]
    old_player_pos = old_player_pos[0]
    old_pos1 = old_player_pos[0]
    old_pos2 = old_player_pos[1]
    new_pos1 = old_pos1 + pos1
    new_pos2 = old_pos2 + pos2

    if matrix[new_pos1][new_pos2] == "#":
        return matrix
    else:
        matrix[new_pos1][new_pos2] = "@"
        matrix[old_pos1][old_pos2] = "."
    return matrix


#background roll
"""   if new_pos2 == 83:
        for i in range(1,len(matrix)):
            for j in range(1,len(matrix[0])-2):
                matrix[i][j] = matrix[i][j+1]
        return matrix"""



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
    if x not in ("wsad"):
        return 0, 0
    else:
        if x == "w":
            position_x = -1
            position_y = 0
        elif x == "s":
            position_x = 1
            position_y = 0
        elif x == "a":
            position_x = 0
            position_y = -1

        elif x == "d":
            position_x = 0
            position_y = 1


    return position_x, position_y

terrain = background(25, 86)
terrain[1][1] = "@"
for i in range(10):
    terrain = mobs_positions(terrain, MOB_TYPES)
"""for i in range(10):
    terrain = random_barriers(terrain)"""
display_background(terrain)

while 1:
    x = getch()
    if x == 'p':
        sys.exit()
    while x not in "wsad":
        x = getch()
    position = user_input(x)
    terrain = player_position(terrain, position[0], position[1])
    os.system("printf '\033c'")
    display_background(terrain)