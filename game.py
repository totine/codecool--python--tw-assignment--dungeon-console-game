from collections import Counter
import csv
import sys
import os
import random
import tty
import termios
import time

global attributes
attributes = {"strenght" : 2, "agility" : 2, "speed" : 2, "power" : 2, "endurance" : 2, "mana" : 2}
TERRX = 86
TERRY = 25
WINDOW_ROWS = 30
WINDOW_COLS = 110
RJUST_SIZE = 105
MOB_TYPES = [u"\U0001F577", u"\U0001F6B9", u"\U0001F43A",u"\U0001F40D",u"\U0001F41B"]
inv = {}
items = [('head', u"\u26D1"), ('chest', u"\U0001F458"), ('legs', u"\U0001F462"),
         ('right hand', '†'), ('left hand', u"\u26E8"), ("hp potion", u"\u2764"),
         ('mana potion', u"\u262F"), ('gold', u"\U0001F4B0")]
equiped = [('head', "nothing"), ('chest', "nothing"), ('legs', "nothing"),
           ('right hand', "nothing"), ('left hand', "nothing"),
           ("hp potion", "nothing"), ('mana potion', "nothing")]
head = [("helmet", 3), ("cap", 0.5)]
chest = [("mail", 6), ("robe", 2)]
legs = [("graves", 2), ("boots", 0.5)]
right_hand = [("sword", 1.5), ("wand", 0.2)]
left_hand = [("shield", 3), ("spell book", 1)]
os.system("printf '\033c'")
sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=WINDOW_ROWS, cols=WINDOW_COLS))


def equip(inv, items, equiped, stats):
    choice = input("Name the thing you want to equip: ")
    if choice == 'helmet' or choice == 'cap':
        value = 'head'
        stats["endurance"] += 1
    elif choice == 'mail' or choice == 'robe':
        value = 'chest'
        stats["endurance"] += 1
    elif choice == 'graves' or choice == 'boots':
        value = 'legs'
        stats["endurance"] += 1
    elif choice == 'sword' or choice == 'wand':
        value = 'right hand'
    elif choice == 'shield' or choice == 'spell book':
        value = 'left hand'
    keys = list(inv.keys())
    values = [seq[0] for seq in head] + [seq[0] for seq in chest] + [seq[0] for seq in legs] + [seq[0] for seq in head] + [seq[0] for seq in right_hand] + [seq[0] for seq in left_hand]
    if choice in keys and choice in values:
        if inv[choice] > 1:
            inv[choice] = inv[choice] - 1
            for idx, itm in enumerate(equiped):
                if itm[0] == value:
                    equiped[idx] = (value, choice)
            print("%s equiped" % choice)
            time.sleep(1)
            stats = print_table(inv, equiped, items, left_column, stats)
        else:
            del inv[choice]
            for idx, itm in enumerate(equiped):
                if itm[0] == value:
                    equiped[idx] = (value, choice)
            print("%s equiped" % choice)
            time.sleep(1)
            stats = print_table(inv, equiped, items, left_column, stats)
    else:
        stats = print_table(inv, equiped, items, left_column, stats)
    return stats


def drop(inv, items,stats):
    choice = input("Name the thing you want to drop: ")
    keys = list(inv.keys())
    values = [seq[0] for seq in head] + [seq[0] for seq in chest] + [seq[0] for seq in legs] + [seq[0] for seq in head] + [seq[0] for seq in right_hand] + [seq[0] for seq in left_hand]
    if choice in keys and choice in values:
        if inv[choice] > 1:
            inv[choice] = inv[choice] - 1
            print_table(inv, equiped, items, left_column, stats)
        else:
            del inv[choice]
            print_table(inv, equiped, items, left_column, stats)
    else:
        print_table(inv, equiped, items, left_column, stats)


def add_to_inventory(inventory, recivedloot):
    """adds loot to inventory"""
    a = Counter(recivedloot)
    b = Counter(inventory)
    inventory = a + b
    return inventory


def item_random(picked_loot, inventory):
    global inv
    print(picked_loot)
    if picked_loot == u"\u26D1":
        picked_loot = [random.choice([seq[0] for seq in head])]
        inv = add_to_inventory(inventory, picked_loot)
    elif picked_loot == u"\U0001F458":
        picked_loot = [random.choice([seq[0] for seq in chest])]
        inv = add_to_inventory(inventory, picked_loot)
    elif picked_loot == u"\U0001F462":
        picked_loot = [random.choice([seq[0] for seq in legs])]
        inv = add_to_inventory(inventory, picked_loot)
    elif picked_loot == '†':
        picked_loot = [random.choice([seq[0] for seq in right_hand])]
        inv = add_to_inventory(inventory, picked_loot)
    elif picked_loot == u"\u26E8":
        picked_loot = [random.choice([seq[0] for seq in left_hand])]
        inv = add_to_inventory(inventory, picked_loot)
    elif picked_loot == u"\u2764":
        picked_loot = ["hp potion"]
        inv = add_to_inventory(inventory, picked_loot)
    elif picked_loot == u"\u262F":
        picked_loot = ["mana potion"]
        inv = add_to_inventory(inventory, picked_loot)
    elif picked_loot == u"\U0001F4B0":
        picked_loot = ["gold"]
        inv = add_to_inventory(inventory, picked_loot)


def print_table(inventory, equiped, items, left_column, stats):
    """displays inventory in arranged manner, used once"""
    os.system("printf '\033c'")
    if inventory:
        longest_item = len(max(inventory, key=len)) + 1
        if longest_item < len("item name") + 1:
            longest_item = len("item name") + 1
    print("\n\t\t\t\t\t" * 5 + "Inventory: ")
    if len(inventory) > 0:
        sorted_tuples = sorted(inventory.items(), key=lambda x: -x[1])
        print("\t" * 5 + "{0:>7} {1:>{width}}".format("count", "item name", width=longest_item))
        print("\t" * 5 + "-" * ((longest_item) + 18))
        nazwy = [seq[0] for seq in head] + [seq[0] for seq in chest] + [seq[0] for seq in legs] + [seq[0] for seq in right_hand] + [seq[0] for seq in left_hand]
        wagi = [seq[1] for seq in head] + [seq[1] for seq in chest] + [seq[1] for seq in legs] + [seq[1] for seq in right_hand] + [seq[1] for seq in left_hand]
        suma_wag = []
        suma_nazw = []
        suma_liczb = []
        for z in nazwy:
            x = nazwy.index(z)
            if z in inv:
                k = wagi[x] * inv[z]
                suma_wag.append(k)
                suma_nazw.append(z)
                suma_liczb.append(inv[z])
        suma = sum(suma_wag)
        for i in range(len(suma_liczb)):
            print("\t" * 5 + "{0:>7} {1:>{width}} {2:>7}".format(suma_liczb[i], suma_nazw[i], float(suma_wag[i]),
                                                                 width=longest_item))
        if 'hp potion' in inv:
            print("\t" * 5 + "{0:>7} {1:>{width}} {2:>7}".format(inv['hp potion'], "hp potion", "0.0",
                                                                 width=longest_item))
        if 'mana potion' in inv:
            print("\t" * 5 + "{0:>7} {1:>{width}} {2:>7}".format(inv['mana potion'], "mana potion", "0.0",
                                                                 width=longest_item))
        if 'gold' in inv:
            print("\t" * 5 + "{0:>7} {1:>{width}} {2:>7}".format(inv['gold'], "gold", "0.0", width=longest_item))
        print("\t" * 5 + "-" * ((longest_item) + 18))
        print("\t" * 5 + "Total number of items:", sum(inventory.values()))
        print("\t" * 5 + "Total weight: %.1f" % suma)
        print("\t" * 5 + "Equiped items: \n")
        iterator = 0
        for i in equiped:
            if iterator < 3:
                print("\t" * 5 + i[0] + '\t\t' + i[1])
                iterator += 1
            elif iterator < 5:
                print("\t" * 5 + i[0] + '\t' + i[1])
                iterator += 1
        decision = input("\n\nDo you want to equip something or drop it? (e/d): ")
        if decision == 'e':
            equip(inventory, items, equiped,stats)
            return stats
        elif decision == 'd':
            drop(inventory, items,stats)
        else:
            os.system("printf '\033c'")
            return stats
            display_background(terrain,left_column)
    else:
        print("\n\t\t\t\t\tYou have nothing in your inventory. \n")
        print("\t" * 5 + "Equiped items: \n")
        iterator = 0
        for i in equiped:
            if iterator < 3:
                print("\t" * 5 + i[0] + '\t\t' + i[1])
                iterator += 1
            elif iterator < 5:
                print("\t" * 5 + i[0] + '\t' + i[1])
                iterator += 1
    return stats


def character_creator():


    def rand_creator():
        os.system("printf '\033c'")
        for i in range(2):
            d = random.choice(list(attributes.keys()))
            attributes[d] += 1
    def creator(attributes):
        print("Create you character. Choose first of two abilities You'd like to expand (or q to go back):\n ")

        for i in attributes:
            print(i, attributes.get(i))

        st_input = str(input("\nWrite a first character of ability you'd like to modify, \nq to get back to main menu or anything else to start over."))
        os.system("printf '\033c'")
        if st_input == "st":
            attributes["strenght"] += 1
        elif st_input == "ag":
            attributes["agility"] += 1
        elif st_input == "sp":
            attributes["speed"] += 1
        elif st_input == "po":
            attributes["power"] += 1
        elif st_input == "en":
            attributes["endurance"] += 1
        elif st_input == "ma":
            attributes["mana"] += 1
        elif st_input == "q":
            main_menu()
        else:
            character_creator()
        os.system("printf '\033c'")
        print("")
        for i in attributes:
            print(i, attributes.get(i))

        st_input = str(input("Now, choose second ability (or anything else, If you'd like to start over): "))
        if st_input == "st":
            attributes["strenght"] += 1
        elif st_input == "ag":
            attributes["agility"] += 1
        elif st_input == "sp":
            attributes["speed"] += 1
        elif st_input == "po":
            attributes["power"] += 1
        elif st_input == "en":
            attributes["endurance"] += 1
        elif st_input == "ma":
            attributes["mana"] += 1
        elif st_input == "q":
            main_menu()
        else:
            os.system("printf '\033c'")
            character_creator()

    print("{:^105}".format("1. Create new character\n"))
    print("{:^105}".format("2. Pick random character\n"))
    print("{:^105}".format("3. Go back"))
    char_method = getch()
    if char_method == "3":
        os.system("printf '\033c'")
        main_menu()
    elif char_method == "2":
        rand_creator()
    elif char_method == "1":
        os.system("printf '\033c'")
        creator(attributes)
    else:
        os.system("printf '\033c'")
        character_creator()

    char_class = ""

    if attributes["strenght"] == 4:
        char_class = "Barbarian"
    elif attributes["agility"] == 4:
        char_class = "Rogue"
    elif attributes["power"] == 4:
        char_class = "Warlock"
    elif attributes["speed"] == 4:
        char_class = "Fencer"
    elif attributes["endurance"] == 4:
        char_class = "Knight"
    elif attributes["mana"] == 4:
        char_class = "Sorcerer"
    elif attributes["power"] == 3 and attributes["speed"] == 3:
        char_class = "Mystic"
    elif attributes["speed"] == 3 and attributes["endurance"] == 3:
        char_class = "Gladiator"
    elif attributes["speed"] == 3 and attributes["mana"] == 3:
        char_class = "Druid"
    elif attributes["power"] == 3 and attributes["endurance"] == 3:
        char_class = "Arcanist"
    elif attributes["mana"] == 3 and attributes["power"] == 3:
        char_class = "Wizard"
    elif attributes["strenght"] == 3 and attributes["agility"] == 3:
        char_class = "Thug"
    elif attributes["speed"] == 3 and attributes["strenght"] == 3:
        char_class = "Sellsword"
    elif attributes["power"] == 3 and attributes["strenght"] == 3:
        char_class = "Templar"
    elif attributes["endurance"] == 3 and attributes["strenght"] == 3:
        char_class = "Battle Mage"
    elif attributes["speed"] == 3 and attributes["agility"] == 3:
        char_class = "Assasin"
    elif attributes["power"] == 3 and attributes["agility"] == 3:
        char_class = "Shaman"
    elif attributes["endurance"] == 3 and attributes["agility"] == 3:
        char_class = "Fighter"
    elif attributes["mana"] == 3 and attributes["agility"] == 3:
        char_class = "Magician"

    name = input("Pick your's character name: ")

    attributes["Name"] = name
    attributes["Class"] = char_class
    os.system("printf '\033c'")

    print("Your character is %s the %s" % (attributes["Name"], attributes["Class"]))

    for i in attributes:
        if attributes[i] == attributes["Name"]:
            continue
        if attributes[i] == attributes["Class"]:
            continue
        print(i, attributes.get(i))

    print("")
    print("Press any key to proceed or r to try again.")
    fin_choice = getch()
    if fin_choice == "r":
        os.system("printf '\033c'")
        character_creator()
    else:
        pass
    attributes.update({'hp': int(10* attributes['endurance']), 'mp': int(10*attributes['mana']), 'exp': 0})
    return attributes


def main_menu():
    title = ["______                                    _ ",
     "|  _  \                                  | |",
      "| | | |_   _ _ __   __ _  ___  ___  _ __ | |",
    "| | | | | | | '_ \ / _` |/ _ \/ _ \| '_ \| |",
     "| |/ /| |_| | | | | (_| |  __/ (_) | | | |_|",
      " ___/  \__,_|_| |_|\__, |\___|\___/|_| |_(_)",
    "                    __/ |                   ",
     "                   |___/                    "]
    for line in title:
        print("{:>75}".format(line))
    m_l = [("" * 2), "1.Start Game", "2.Help", "3.Quit"]
    for n in m_l:
        print("{:^105}".format(n))

    choice = getch()

    if choice == "1":
        os.system("printf '\033c'")
        character_creator()
    elif choice == "2":
        os.system("printf '\033c'")
        help_l = [("" * 10), "HELP", "Use WSAD for moving your character.", "That's all for now.", ""]
        for i in help_l:
            print("{:^105}".format(i))
        ib = input("{:^105}".format("Press ENTER to go back"))
        if ib == False:
            os.system("printf '\033c'")
            main_menu()
        else:
            os.system("printf '\033c'")
            main_menu()
    elif choice == "3":
        sys.exit()


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


def display_background(matrix,right_column_text):
    #for i in matrix:
    length_list_1 = [len(str(item[0])) for item in right_column_text]
    length_list_2 = [len(str(item[1])) for item in right_column_text]

    max_size_1 = max(length_list_1) + 2
    max_size_2 = max(length_list_2) + 2
    #    print(''.join(i).rjust(RJUST_SIZE, " "))
    for i in range(0,len(matrix)):
        if i < len(right_column_text):
            print(right_column_text[i][0].ljust(max_size_1 , " "), str(right_column_text[i][1]).ljust(max_size_2 , " "), end="")
            print(''.join(matrix[i]))
        else:
            print(''.join(matrix[i]).rjust(max_size_1 + max_size_2 + len(matrix[0]) + 1, " "))



def level_creating(game_matrix):
    stalactite = random.randint(2,6)
    stalagmite = random.randint(2,6)
    for i in range(2,len(game_matrix[0])):
        stalactite = stalactite + random.randint(-1,1)
        stalagmite = stalagmite + random.randint(-1,1)
        if stalactite > 7 or stalactite < 2:
            stalactite = random.randint(2,4)
        if stalagmite > 7 or stalagmite < 2:
            stalagmite = random.randint(2,4)
        for j in range(1,stalactite):
            game_matrix[j][i] = "#"
        for k in range(1,stalagmite):
            game_matrix[-k][i] = "#"
    return game_matrix


def mobs_positions(game_matrix, mob_list, TERRY, TERRX):
    mob_pos_x = random.randint(1, TERRY-1)
    mob_pos_y = random.randint(1, TERRX -1)
    mob_type = random.choice(mob_list)
    if game_matrix[mob_pos_x][mob_pos_y] != "#":
        game_matrix[mob_pos_x][mob_pos_y] = mob_type
    return game_matrix


def items2_positions(game_matrix, mob_list, items):
    item2_pos_x = random.randint(1, 24)
    item2_pos_y = random.randint(1, 84)
    itemss = [seq[1] for seq in items]
    item2_type = random.choice(itemss)
    if game_matrix[item2_pos_x][item2_pos_y] != "#" and game_matrix[item2_pos_x][item2_pos_y] not in mob_list:
        game_matrix[item2_pos_x][item2_pos_y] = item2_type
    return game_matrix


def battle(matrix, new_pos1, new_pos2, mobhp, inv):

    choice = getch()

    if choice == '1':
        roll = (random.randint(1,10)) + attributes["strenght"]
        mobhp -= roll
        print('Your hit dealt ', str(roll), ' damage')
        if mobhp < 1:
            print('You won!')
            attributes['exp'] += 5
            matrix[new_pos1][new_pos2] = "."
            time.sleep(1)
            return matrix
        else:
            roll = (random.randint(1, 6)) + 3
            attributes['hp'] -= roll
            print('You lost ', str(roll), " health points. You have ", repr(attributes['hp']), " left.")
            if attributes['hp'] < 1:
                print('Game over',u"\U0001F595")
                time.sleep(1)
                sys.exit()
            else:
                battle(matrix, new_pos1, new_pos2, mobhp,inv)
    elif choice == '2':
        roll = (random.randint(1, 6))
        mobhp -= roll
        print('Your hit dealt ', str(roll), ' damage')
        if mobhp < 1:
            print('You won!')
            attributes['exp'] += 5
            time.sleep(1)
            matrix[new_pos1][new_pos2] = "."
            return matrix
        else:
            roll2 = (random.randint(1, 20)) + attributes["agility"]
            if roll2 > 15:
                print('Your agility allowed a second hit!')
                roll = (random.randint(1, 6)) + int(attributes["agility"]/2)
                mobhp -= roll
                print('Your hit dealt ', str(roll), ' damage')
                if mobhp < 1:
                    print('You won!')
                    attributes['exp'] += 5
                    time.sleep(1)
                    matrix[new_pos1][new_pos2] = "."
                    return matrix
                else:
                    roll = (random.randint(1, 6)) + 3
                    attributes['hp'] -= roll
                    print('You lost ', str(roll), " health points. You have ", repr(attributes['hp']), " left.")
                    if attributes['hp'] < 1:
                        print('Game over',u"\U0001F595")
                        time.sleep(1)
                        sys.exit()
                    else:
                        battle(matrix, new_pos1, new_pos2, mobhp,inv)
    elif choice == '3':
        if attributes['mp']> 5:
            roll = (random.randint(1, 15)) + attributes['power']
            attributes['mp'] -=5
            mobhp -= roll
            print('Your spell dealt ', str(roll), ' damage. You have ', repr(attributes['mp']), " mana left.")
            if mobhp < 1:
                print('You won!')
                attributes['exp'] += 5
                time.sleep(1)
                matrix[new_pos1][new_pos2] = "."
                return matrix
            else:
                roll = (random.randint(1, 6)) + 3
                attributes['hp'] -= roll
                print('You lost ', str(roll), " health points. You have ", repr(attributes['hp']), " left.")
                if attributes['hp'] < 1:
                    print('Game over',u"\U0001F595")
                    time.sleep(1)
                    sys.exit()
                else:
                    battle(matrix, new_pos1, new_pos2, mobhp,inv)
        else:
            print('You do not have enough mana!')
            battle(matrix, new_pos1, new_pos2, mobhp,inv)
    elif choice == '4':
        print('Would you like to use\n1. Health potion or\n2. Mana potion?')
        x = getch()
        if x == "1":
            if 'hp potion' in inv:
                attributes['hp'] += 5
                print('You regained 5 Health points. You have ', repr(attributes['hp']), " left.")
                if inv["hp potion"] > 1:
                    inv["hp potion"] = inv["hp potion"] - 1
                    battle(matrix, new_pos1, new_pos2, mobhp, inv)
                else:
                    del inv["hp potion"]
                    battle(matrix, new_pos1, new_pos2, mobhp, inv)
            else:
                print('You have no Health potions left!')
        if x == "2":
            if 'mana potion' in inv:
                attributes['mp'] += 5
                print('You regained 5 Mana points. You have ', repr(attributes['mp']), " left.")
                if inv["mana potion"] > 1 or inv["mana potion" != "nothing"]:
                    inv["mana potion"] = inv["mana potion"] - 1
                    battle(matrix, new_pos1, new_pos2, mobhp, inv)
                else:
                    del inv["mana potion"]
                    battle(matrix, new_pos1, new_pos2, mobhp, inv)
            else:
                print('You have no Health potions left!')
                battle(matrix, new_pos1, new_pos2, mobhp, inv)
        else:
             battle(matrix, new_pos1, new_pos2, mobhp,inv)
    elif choice == '5':
        roll = (random.randint(1, 6)) + attributes['speed']
        if roll > 4:
            print('You managed to escape!')
            attributes['exp'] -= 5
            time.sleep(1)
            return matrix
        else:
            roll = (random.randint(1, 6)) + 3
            attributes['hp'] -= roll
            print('You regained 5 Health points. You have ', repr(attributes['hp']), " left.")
            if attributes['hp'] < 1:
                print('Game over',u"\U0001F595")
                time.sleep(1)
                sys.exit()
            else:
                battle(matrix, new_pos1, new_pos2, mobhp,inv)
    else:
        battle(matrix, new_pos1, new_pos2, mobhp,inv)
    #battle(matrix, new_pos1, new_pos2, mobhp, inv)
            
def talk():
    input('Hola! ')
    x = input('No habla ingles! ')
    while x:
        x = input('No habla ingles! ')


def encounter(matrix, new_pos1, new_pos2):
    mobhp = 20
    if matrix[new_pos1][new_pos2] == u"\U0001F6B9":
        print('You have encountered an NPC ')
        choice = input('What would you like to do? ').lower()
        if choice == 'fight':
            print('1. Strong attack\n2. Quick attack\n3. Spell\n4. Use item\n5. Run ')
            battle(matrix, new_pos1, new_pos2,mobhp,inv)
        elif choice == 'talk':
            talk()
    else:
        print('You were attacked by a feroucious beast! ')
        print('1. Strong attack\n2. Quick attack\n3. Spell\n4. Use item\n5. Run ')
        battle(matrix, new_pos1, new_pos2,mobhp, inv)
    return matrix

def pick_up(matrix, new_pos1, new_pos2, inventory, items):
    #global inv
    old_player_pos = [(index, row.index("@")) for index, row in enumerate(matrix) if "@" in row]
    old_player_pos = old_player_pos[0]
    old_pos1 = old_player_pos[0]
    old_pos2 = old_player_pos[1]
    itemsss = [seq[1] for seq in items]
    if matrix[new_pos1][new_pos2] in itemsss:
        picked_loot = matrix[new_pos1][new_pos2]

        #inv = add_to_inventory(inventory, picked_loot)
        matrix[new_pos1][new_pos2] = "@"
        matrix[old_pos1][old_pos2] = "."
        item_random(picked_loot, inventory)
        return matrix


def new_column(matrix):
    old_stalactite = 0
    for i in range(1,14):
        if matrix[i][83] == "#":
            old_stalactite += 1
    stalactite = old_stalactite + random.choice([-1,0,1,1,1,2,3,4,3,3,4])
    old_stalagmite = 0
    for i in range(len(matrix)-8,len(matrix)-1):
        if matrix[i][83] == "#":
            old_stalagmite += 1
    stalagmite = old_stalagmite + random.choice([-1,0,1,1,1,2,3,4,3,3,4])
    if stalactite + stalagmite > 20:
        stalactite = stalactite - 2
        stalagmite = stalagmite - 2

    for j in range(1,stalactite):
                matrix[j][84] = "#"
    for k in range(0,stalagmite):
        matrix[-k][84] = "#"

    last_column_list = []
    for i in range(1,len(matrix)-1):
        last_column_list.append(matrix[i][84])

    return last_column_list


def player_position(matrix, pos1, pos2, MOB_TYPES, inventory, items, equiped):
    old_player_pos = [(index, row.index("@")) for index, row in enumerate(matrix) if "@" in row]
    old_player_pos = old_player_pos[0]
    old_pos1 = old_player_pos[0]
    old_pos2 = old_player_pos[1]
    new_pos1 = old_pos1 + pos1
    new_pos2 = old_pos2 + pos2
    itemsss = [seq[1] for seq in items]
    if matrix[new_pos1][new_pos2] == "#":
        return matrix
    elif matrix[new_pos1][new_pos2] in MOB_TYPES:
        encounter(matrix, new_pos1, new_pos2)
        return matrix
    elif matrix[new_pos1][new_pos2] in itemsss:
        pick_up(matrix, new_pos1, new_pos2, inventory, items)
    if new_pos2 == 60:
        for i in range(1,len(matrix)):
            for j in range(1,len(matrix[0])-2):
                matrix[i][j] = matrix[i][j+1]
        for i in range(1,len(matrix)-1):
            matrix[i][84] = "."
        last_column_content = new_column(matrix)
        for i in range(1,len(matrix)-2):
            matrix[i][84] = last_column_content[i]
        npc_index = MOB_TYPES.index(u"\U0001F6B9")
        npc_to_display = MOB_TYPES[npc_index]
        mob_list_without_npc = MOB_TYPES[:npc_index:]
        mob_chance = random.randint(1,100)
        if mob_chance > 55:
            mob_pos_x = random.randint(1,24)
            mob_type = random.choice(MOB_TYPES)
            if matrix[mob_pos_x][84] != "#":
                matrix[mob_pos_x][84] = mob_type
        npc_chance = random.randint(1,1000)
        if npc_chance < 2:
            npc_pos_x = random.randint(1,24)
            npc_type = random.choice(npc_to_display)
            if matrix[npc_pos_x][84] != "#":
                matrix[npc_pos_x][84] = npc_type
        item_chance = random.randint(1,1000)
        item_list = [item[1] for item in items]
        if item_chance < 2:
            item_pos_x = random.randint(1,24)
            item_type = random.choice(item_list)
            if matrix[item_pos_x][84] != "#":
                matrix[item_pos_x][84] = item_type

    else:
        matrix[new_pos1][new_pos2] = "@"
        matrix[old_pos1][old_pos2] = "."
    return matrix


def new_column(matrix):
    old_stalactite = 0
    for i in range(1,14):
        if matrix[i][83] == "#":
            old_stalactite += 1
    stalactite = old_stalactite + random.choice([-1,0,1,1,1,2,3,4,3,3,4])
    old_stalagmite = 0
    for i in range(len(matrix)-8,len(matrix)-1):
        if matrix[i][83] == "#":
            old_stalagmite += 1
    stalagmite = old_stalagmite + random.choice([-1,0,1,1,1,2,3,4,3,3,4])
    if stalactite + stalagmite > 20:
        stalactite = stalactite - 2
        stalagmite = stalagmite - 2

    for j in range(1,stalactite):
                matrix[j][84] = "#"
    for k in range(0,stalagmite):
        matrix[-k][84] = "#"

    last_column_list = []
    for i in range(1,len(matrix)-1):
        last_column_list.append(matrix[i][84])

    return last_column_list


def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch


def user_input(x):
    if x not in "wsad":
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


def making_left_column(attributes, inv):
    keys = list(inv.keys())
    blank_line = ["",""]
    line_1 = ["Name", attributes["Name"]]
    line_2 = ["Class", attributes["Class"]]
    line_3 = ["Agility", attributes["agility"]]
    line_4 = ["Speed", attributes["speed"]]
    line_5 = ["Strenght", attributes["strenght"]]
    line_6 = ["Endurance", attributes["endurance"]]
    line_7 = ["HP", str(attributes["hp"])+"/"+str(attributes["endurance"]*10)]
    line_8 = ["MP", str(attributes["mp"])+"/"+str(attributes["mana"]*10)]
    line_9 = ["Exp", attributes["mana"]]
    if "hp potion" in keys and "mana potion" in keys:
        line_10 = ("Hp potions:", str(inv["hp potion"]))
        line_11 = ("Mana potions:", str(inv["mana potion"]))
    elif "hp potion" in keys and "mana potion" not in keys:
        line_10 = ("Hp potions: ", str(inv["hp potion"]))
        line_11 = ("Mana potions: ", "0")
    elif "hp potion" not in keys and "mana potion" in keys:
        line_10 = ("Hp potions: ", "0")
        line_11 = ("Mana potions: ", str(inv["mana potion"]))
    else:
        line_10 = ("Hp potions: ", "0")
        line_11 = ("Mana potions: ", "0")

    left_column = [blank_line, blank_line, line_1, line_2, line_3, line_4, line_5, line_6, line_7, line_8, line_9, blank_line, line_10, line_11]

    return left_column



terrain = background(TERRY, TERRX)
terrain[int(TERRY/2)][1] = "@"
terrain = level_creating(terrain)
for i in range(10):
    terrain = mobs_positions(terrain, MOB_TYPES,TERRY, TERRX)
    terrain = items2_positions(terrain, MOB_TYPES, items)
main_menu()
left_column = making_left_column(attributes,inv)
display_background(terrain,left_column)

while 1:
    x = getch()
    if x == 'p':
        sys.exit()
    if x == "i":
        stats = print_table(inv, equiped, items, left_column, attributes)
    if x == "1" and 'hp potion' in inv:
        if attributes['hp'] > attributes['endurance']*10-5:
            attributes['hp'] = attributes['endurance']*10
        else:
            attributes['hp'] +=5
        if inv["hp potion"] > 1:
            inv["hp potion"] = inv["hp potion"] - 1
            os.system("printf '\033c'")
            left_column = making_left_column(attributes, inv)
            display_background(terrain, left_column)
            x = getch()
        else:
            del inv["hp potion"]
            os.system("printf '\033c'")
            left_column = making_left_column(attributes, inv)
            display_background(terrain, left_column)
            x = getch()
    if x == "2" and 'mana potion' in inv:
        if attributes['mp'] > attributes['mana']*10-5:
            attributes['mp'] = attributes['mana']*10
        else:
            attributes['mp'] +=5
        if inv["mana potion"] > 1 or inv["mana potion" != "nothing"]:
            inv["mana potion"] = inv["mana potion"] - 1
            os.system("printf '\033c'")
            left_column = making_left_column(attributes, inv)
            display_background(terrain, left_column)
            x = getch()
        else:
            del inv["mana potion"]
            os.system("printf '\033c'")
            left_column = making_left_column(attributes, inv)
            display_background(terrain, left_column)
            x = getch()

    while x not in "wsad":
        x = getch()
    position = user_input(x)
    terrain = player_position(terrain, position[0], position[1], MOB_TYPES, inv, items, equiped)
    os.system("printf '\033c'")
    left_column = making_left_column(attributes,inv)
    display_background(terrain,left_column)