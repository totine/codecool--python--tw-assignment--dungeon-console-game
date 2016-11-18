from collections import Counter
import sys
import os
import random
import tty
import termios
import time
import csv
import os.path



attributes = {"strenght": 2, "agility": 2, "speed": 2, "power": 2, "endurance": 2, "mana": 2}
starting_attributes = {}
TERRX = 86
TERRY = 25
WINDOW_ROWS = 35
WINDOW_COLS = 117
RJUST_SIZE = 105
MOB_TYPES = [u"\U0001F577", u"\U0001F6B9", u"\U0001F43A", u"\U0001F40D", u"\U0001F41B"]
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


demon = ("""

                                                        ,-.
                                   ___,---.__          /'|`\          __,---,___
                                ,-'    \`    `-.____,-'  |  `-.____,-'    //    `-.
                              ,'        |           ~'\     /`~           |        `.
                             /      ___//              `. ,'          ,  , \___      \\
                            |    ,-'   `-.__   _         |        ,    __,-'   `-.    |
                            |   /          /\_  `   .    |    ,      _/\          \   |
                            \  |           \ \`-.___ \   |   / ___,-'/ /           |  /
                             \  \           | `._   `\\  |  //'   _,' |           /  /
                              `-.\         /'  _ `---'' , . ``---' _  `\         /,-'
                                 ``       /     \    ,='/ \`=.    /     \       ''
                                         |__   /|\_,--.,-.--,--._/|\   __|
                                         /  `./  \\`\ |  |  | /,//' \,'  \\
                                        /   /     ||--+--|--+-/-|     \   \\
                                       |   |     /'\_\_\ | /_/_/`\     |   |
                                        \   \__, \_     `~'     _/ .__/   /
                                         `-._,-'   `-._______,-'   `-._,-'""")


def satan():
    os.system("printf '\033c'")
    print(demon)
    for i in range(5):
        print("")
    print("{:^120}".format("PUNY MORTAL!"))
    text = getch()
    if not text:
        pass
    else:
        os.system("printf '\033c'")
        print(demon)
        for i in range(5):
            print("")
        print("{:^120}".format("You have bestown upon the mightiest of all demons!"))
        if getch():
            os.system("printf '\033c'")
            print(demon)
            for i in range(5):
                print("")
            print("{:^120}".format("TOTALLY BETTER THAN DIABLO!"))
            if getch():
                os.system("printf '\033c'")
                print(demon)
                for i in range(5):
                    print("")
                print("{:^120}".format("Smashing you in combat wouldn't be a much of task for me..."))
                if getch():
                    pass
                else:
                    os.system("printf '\033c'")
                    print(demon)
                    for i in range(5):
                        print("")
                    print("{:^130}".format("So lets play a game..."))
                    os.system("printf '\033c'")


def greetings():
    os.system("printf '\033c'")
    print(demon)
    for i in range(3):
        print("")
    print ('I am thinking of a 3-digit number. I shall teach you if you guess.')
    print ('\nI pity you, so here are some clues:')
    print ('\nWhen I say:    That means:')
    print ('\n  Cold       No digit is correct.')
    print ('\n  Warm       One digit is correct but in the wrong position.')
    print ('\n  Hot        One digit is correct and in the right position.')
    print ('\nI have thought up a number. You have 10 guesses to get it.')


def load():
    global attributes, inv, equiped, starting_attributes
    with open("inv.csv", "a+") as f:
        f.seek(0)
        reader = csv.reader(f)
        read_dict = dict(reader)
        for key in read_dict:
            read_dict[key] = int(read_dict[key])
        inv = Counter(read_dict)
    with open("att.csv", "a+") as f:
        f.seek(0)
        reader = csv.reader(f)
        read_dict = dict(reader)
        for key in read_dict:
            if read_dict[key] == read_dict["Name"] or read_dict[key] == read_dict["Class"]:
                read_dict[key] = read_dict[key]
            else:
                read_dict[key] = int(read_dict[key])
        attributes = Counter(read_dict)
    with open("satt.csv", "a+") as f:
        f.seek(0)
        reader = csv.reader(f)
        read_dict = dict(reader)
        for key in read_dict:
            if read_dict[key] == read_dict["Name"] or read_dict[key] == read_dict["Class"]:
                read_dict[key] = read_dict[key]
            else:
                read_dict[key] = int(read_dict[key])
        starting_attributes = Counter(read_dict)
    with open("eq.csv", "a+") as f:
        f.seek(0)
        read = csv.reader(f)
        eq = []
        for key in read:
            eq.append(tuple(key))
        equiped = eq
    os.system("printf '\033c'")
    tristram()


def save():
    with open("inv.csv", "w+") as f:
        w = csv.writer(f)
        for key, value in inv.items():
            w.writerow([key, value])
    with open("att.csv", "w+") as f:
        w = csv.writer(f)
        for key, value in attributes.items():
            w.writerow([key, value])
    with open("satt.csv", "w+") as f:
        w = csv.writer(f)
        for key, value in starting_attributes.items():
            w.writerow([key, value])
    with open("eq.csv", "w+") as f:
        w = csv.writer(f)
        for key in equiped:
            w.writerow([key[0], key[1]])

def level_up():
    st_input = input('\t\tYou leveled up. Type two first letters of an attribute you want to improve!: ')
    if st_input == "st":
        attributes['exp'] = 0
        attributes['lev'] += 1
        attributes["strenght"] += 1
        starting_attributes['lev'] += 1
        starting_attributes["strenght"] += 1
    elif st_input == "ag":
        attributes['exp'] = 0
        attributes['lev'] += 1
        attributes["agility"] += 1
        starting_attributes['lev'] += 1
        starting_attributes["agility"] += 1
    elif st_input == "sp":
        attributes['exp'] = 0
        attributes['lev'] += 1
        attributes["speed"] += 1
        starting_attributes['lev'] += 1
        starting_attributes["speed"] += 1
    elif st_input == "po":
        attributes['exp'] = 0
        attributes['lev'] += 1
        attributes["power"] += 1
        starting_attributes['lev'] += 1
        starting_attributes["power"] += 1
    elif st_input == "en":
        attributes['exp'] = 0
        attributes['lev'] += 1
        attributes["endurance"] += 1
        starting_attributes['lev'] += 1
        starting_attributes["endurance"] += 1
    elif st_input == "ma":
        attributes['exp'] = 0
        attributes['lev'] += 1
        attributes["mana"] += 1
        starting_attributes['lev'] += 1
        starting_attributes["mana"] += 1
    else:
        print("")
        print('{0:^110}'.format("That is not one of your attributes!(st/en/po/sp/ag/ma): "))
        level_up()
    os.system("printf '\033c'")
    tristram()


def boss():
    satan()
    greetings()
    x = random.randint(1, 9)
    y = random.randint(0, 9)
    while x == y:
        y = random.randint(0, 9)
    z = random.randint(0, 9)
    while z == y or z == x:
        z = random.randint(0, 9)
    xyz = list(str(x) + str(y) + str(z))
    print(xyz)
    user_input = ''
    count = 0
    while user_input != xyz:
        count += 1
        if count > 10:
            boss_game_over()
        else:
            user_input = input('Guess: ').strip()
            while len(user_input) != 3 or not user_input.isnumeric():
                print('This is not even a three digit number!')
                user_input = input('Guess: ').strip()
            user_input = list(user_input)
            print(user_input)
            if xyz == user_input:
                print("")
                print("{0:^110}".format("You have defated me! NOOOOOOOOOOOOOOOOOO!"))
                time.sleep(1)
                level_up()
            else:
                a = ''
                b = ''
                c = ''
                if xyz[0] == user_input[0]:
                    a = 'hot'
                elif user_input[0] in xyz:
                    a = 'warm'
                if xyz[1] == user_input[1]:
                    b = 'hot'
                elif user_input[1] in xyz:
                    b = 'warm'
                if xyz[2] == user_input[2]:
                    c = 'hot'
                elif user_input[2] in xyz:
                    c = 'warm'
                else:
                    if [a, b, c] == ['', '', '']:
                        a = 'cold'
                abc = [a, b, c]
                abc.sort()
                if abc[0] == '':
                    if abc[1] == '':
                        print(abc[2])
                    else:
                        print(abc[1], abc[2])
                else:
                    print(abc[0], abc[1], abc[2])


def equip(inv, items, equiped, stats):
    choice = input("Name the thing you want to equip: ")
    equiped_check = [seq[1] for seq in equiped]
    if choice == 'helmet':
        value = 'head'
        if equiped_check[0] == "nothing":
            stats["endurance"] += 1
        elif equiped_check[0] == "cap":
            stats["mana"] = starting_attributes["mana"]
            stats["endurance"] += 1
    elif choice == 'cap':
        value = 'head'
        if equiped_check[0] == "nothing":
            stats["mana"] += 1
        elif equiped_check[0] == "helmet":
            stats["endurance"] = starting_attributes["endurance"]
            stats["mana"] += 1
    elif choice == 'mail':
        value = 'chest'
        if equiped_check[1] == "nothing":
            stats["endurance"] += 2
        elif equiped_check[1] == "robe":
            stats["mana"] = starting_attributes["mana"]
            stats["endurance"] += 2
    elif choice == 'robe':
        value = 'chest'
        if equiped_check[1] == "nothing":
            stats["mana"] += 2
        elif equiped_check[1] == "mail":
            stats["endurance"] = starting_attributes["endurance"]
            stats["mana"] += 2
    elif choice == 'graves':
        value = 'legs'
        if equiped_check[2] == "nothing":
            stats["endurance"] += 1
        elif equiped_check[2] == "boots":
            stats["speed"] = starting_attributes["speed"]
            stats["endurance"] += 1
    elif choice == 'boots':
        value = 'legs'
        if equiped_check[2] == "nothing":
            stats["speed"] += 1
        elif equiped_check[2] == "graves":
            stats["endurance"] = starting_attributes["endurance"]
            stats["speed"] += 1
    elif choice == 'sword':
        value = 'right hand'
        if equiped_check[3] == "nothing":
            stats["strenght"] += 2
        elif equiped_check[3] == "wand":
            stats["power"] = starting_attributes["power"]
            stats["strenght"] += 2
    elif choice == 'wand':
        value = 'right hand'
        if equiped_check[3] == "nothing":
            stats["power"] += 2
        elif equiped_check[3] == "sword":
            stats["strenght"] = starting_attributes["strenght"]
            stats["power"] += 2
    elif choice == 'shield':
        value = 'left hand'
        if equiped_check[4] == "nothing":
            stats["endurance"] += 2
        elif equiped_check[4] == "spell book":
            stats["mana"] = starting_attributes["mana"]
            stats["endurance"] += 2
    elif choice == 'spell book':
        value = 'left hand'
        if equiped_check[4] == "nothing":
            stats["mana"] += 2
        elif equiped_check[4] == "spell book":
            stats["strenght"] = starting_attributes["strenght"]
            stats["mana"] += 2
    keys = list(inv.keys())
    values = [seq[0] for seq in head] + [seq[0] for seq in chest] + [seq[0] for seq in legs] + [seq[0]
              for seq in head] + [seq[0] for seq in right_hand] + [seq[0] for seq in left_hand]
    if choice in keys and choice in values:
        if inv[choice] > 1:
            inv[choice] = inv[choice] - 1
            for idx, itm in enumerate(equiped):
                if itm[0] == value:
                    equiped[idx] = (value, choice)
            print("%s equiped!" % choice)
            time.sleep(1)
            stats = print_table(inv, equiped, items, stats)
        else:
            del inv[choice]
            for idx, itm in enumerate(equiped):
                if itm[0] == value:
                    equiped[idx] = (value, choice)
            print("%s equiped!" % choice)
            time.sleep(1)
            stats = print_table(inv, equiped, items, stats)
    else:
        stats = print_table(inv, equiped, items, stats)
    return stats


def drop(inv, items, stats):
    choice = input("Name the thing you want to drop: ")
    keys = list(inv.keys())
    values = [seq[0] for seq in head] + [seq[0] for seq in chest] + [seq[0] for seq in legs] + [seq[0]
              for seq in head] + [seq[0] for seq in right_hand] + [seq[0] for seq in left_hand]
    if choice in keys and choice in values:
        if inv[choice] > 1:
            inv[choice] = inv[choice] - 1
            print("%s dropped!" % choice)
            time.sleep(1)
            print_table(inv, equiped, items, stats)
        else:
            del inv[choice]
            print("%s dropped!" % choice)
            time.sleep(1)
            print_table(inv, equiped, items, stats)
    else:
        print_table(inv, equiped, items, stats)


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


def print_table(inventory, equiped, items, stats):
    os.system("printf '\033c'")
    if inventory:
        longest_item = len(max(inventory, key=len)) + 1
        if longest_item < len("item name") + 1:
            longest_item = len("item name") + 1
    print("\n\t\t\t\t\t" * 5 + "Inventory: ")
    if len(inventory) > 0:
        sorted_tuples = sorted(inventory.items(), key=lambda x: -x[1])
        print("\t" * 5 + "{0:>7} {1:>{width}}".format("count", "item name", width=longest_item))
        print("\t" * 5 + "-" * (longest_item + 18))
        nazwy = [seq[0] for seq in head] + [seq[0] for seq in chest] + [seq[0]
                 for seq in legs] + [seq[0] for seq in right_hand] + [seq[0] for seq in left_hand]
        wagi = [seq[1] for seq in head] + [seq[1] for seq in chest] + [seq[1]
                 for seq in legs] + [seq[1] for seq in right_hand] + [seq[1] for seq in left_hand]
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
            equip(inventory, items, equiped, stats)
            return stats
        elif decision == 'd':
            drop(inventory, items, stats)
        else:
            return stats
            display_background(terrain, left_column)
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
        print("\n\n\n\n\n\n\n\n\n")

    def creator(attributes):
        print("\n\n\n\n\n\n\n")
        print("{:^105}".format("Create you character.\n"))
        print("{:^105}".format("Choose first of two abilities You'd like to expand (or q to go back):\n "))

        for i in attributes:
            print("{0:>45} {1:>15}".format(i, attributes.get(i)))

        st_input = str(input("\n\t\tWrite first two characters of ability you'd like to modify(ath else to back): "))
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
        else:
            os.execl(sys.executable, sys.executable, *sys.argv)

        print("\n\n\n\n\n\n\n\n\n")
        print("{:^105}".format("Choose first of two abilities You'd like to expand (or q to go back):\n"))
        for i in attributes:
            print("{0:>45} {1:>15}".format(i, attributes.get(i)))

        st_input = str(input("\n\t\tNow, choose second ability (or anything else, if you'd like to start over): "))
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
        else:
            os.execl(sys.executable, sys.executable, *sys.argv)
    print("\n\n\n\n\n\n\n\n\n")
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
        char_class = "Fighter"
    elif attributes["power"] == 3 and attributes["strenght"] == 3:
        char_class = "Templar"
    elif attributes["endurance"] == 3 and attributes["strenght"] == 3:
        char_class = "Warrior"
    elif attributes["speed"] == 3 and attributes["agility"] == 3:
        char_class = "Assasin"
    elif attributes["power"] == 3 and attributes["agility"] == 3:
        char_class = "Witch"
    elif attributes["endurance"] == 3 and attributes["agility"] == 3:
        char_class = "Sellsword"
    elif attributes["mana"] == 3 and attributes["agility"] == 3:
        char_class = "Magician"
    elif attributes["strenght"] == 3 and attributes["mana"] == 3:
        char_class = "Shaman"
    elif attributes["endurance"] == 3 and attributes["mana"] == 3:
        char_class = "Battle Mage"
    else:
        char_class = "Folk"
    name = input("\t\t\t\t\tPick your's character name: ")
    attributes["Name"] = name
    attributes["Class"] = char_class
    os.system("printf '\033c'")

    print("\n\n\n\n\n\n\n\n\n")
    print("\t\t\t\tYour character is %s the %s\n" % (attributes["Name"], attributes["Class"]))

    for i in attributes:
        if attributes[i] == attributes["Name"]:
            continue
        if attributes[i] == attributes["Class"]:
            continue
        print("{0:>45} {1:>15}".format(i, attributes.get(i)))
    global starting_attributes
    starting_attributes = attributes.copy()
    print("\n")
    print("{:^105}".format("Press any key to proceed or 'r' to restart: "))
    fin_choice = getch()
    if fin_choice == "r":
        os.execl(sys.executable, sys.executable, *sys.argv)
    else:
        pass
        os.system("printf '\033c'")
    attributes.update({'hp': int(10 * attributes['endurance']),
                       'mp': int(10 * attributes['mana']), 'exp': 0, 'lev': 1})
    global starting_attributes
    starting_attributes = attributes.copy()
    tristram()
    return attributes


def main_menu():
    title = [" _        _______ _________   ______  _________ _______  ______   _        _______ ",
             "( (    /|(  ___  )\__   __/  (  __  \ \__   __/(  ___  )(  ___ \ ( \      (  ___  )",
             "|  \  ( || (   ) |   ) (     | (  \  )   ) (   | (   ) || (   ) )| (      | (   ) |",
             "|   \ | || |   | |   | |     | |   ) |   | |   | (___) || (__/ / | |      | |   | |",
             "| (\ \) || |   | |   | |     | |   | |   | |   |  ___  ||  __ (  | |      | |   | |",
             "| | \   || |   | |   | |     | |   ) |   | |   | (   ) || (  \ \ | |      | |   | |",
             "| )  \  || (___) |   | |     | (__/  )___) (___| )   ( || )___) )| (____/\| (___) |",
             "|/    )_)(_______)   )_(     (______/ \_______/|/     \||/ \___/ (_______/(_______)",
             "                                                                                   "]

    for line in title:
        print("{:>100}".format(line))
    m_l = [("" * 2), "1.Start Game", "2.Load Game", "3.Help", "4.Credits", "5.Quit"]
    for n in m_l:
        print("{:^110}".format(n))
        print("")

    choice = getch()

    if choice == "1":
        os.system("printf '\033c'")
        character_creator()
    elif choice == "2":
        if os.path.isfile('inv.csv'):
            load()
        else:
            print("\n"*5)
            print("{0:^110}".format("You don't have any save file. "))
            time.sleep(1)
            os.system("printf '\033c'")
            main_menu()

    elif choice == "3":
        help_l = [("" * 10), "HELP", "Use WSAD for moving your character.", "I - Inventory",
                  "P - Quit Game", "1 - HP potion", "2 - Mana potion"]
        os.system("printf '\033c'")
        print("\n\n\n\n\n")
        for i in help_l:
            print("{:^110}".format(i))
        print("")
        print("{:^110}".format("Press ENTER to go back"))
        if getch():
            os.system("printf '\033c'")
            main_menu()
        else:
            os.system("printf '\033c'")
            main_menu()
    elif choice == "4":
        credits = [("" * 10), "Michał Goździkiewicz", "Joanna Gargaś", "Marek Frankowicz", "Łukasz Bielenin"]
        os.system("printf '\033c'")
        print("\n\n\n\n\n")
        for s in credits:
            print("{:^110}".format(s))
        print("")
        print("{:^110}".format("Press any key to go back"))
        if getch():
            os.system("printf '\033c'")
            main_menu()
        else:
            os.system("printf '\033c'")
            main_menu()
    elif choice == "5":
        sys.exit()
    else:
        os.system("printf '\033c'")
        main_menu()


def background(x, y):
    matrix = []
    for row in range(x):
        matrix.append([])
        for column in range(y):
            if row == 0 or row == x - 1 or column == 0 or column == y - 1:
                matrix[row].append('#')
            else:
                matrix[row].append('.')
    return matrix


def start_background():
    matrix = [
        list("##################################################################################################"),
        list("#................................................................................................#"),
        list("#...... .----| |-. ..............................................................................#"),
        list("#..... /          \................................................###...........................#"),
        list("#...../____________\ .............................................#o###..........................#"),
        list("#.....||_|_| /  \  |............................................#####o###........................#"),
        list("#.....||_|_| | .|  |...........................................#o#\#|#/###.......................#"),
        list("#.....|______|__|__|............................................###\|/#o#........................#"),
        list("#................................................................# }|{ #.........................#"),
        list("#..................................................................|||...........................#"),
        list("#............................................................................................... #"),
        list("#......______________............................................................................#"),
        list("#......|Not Tristram|.........................⛧..................................................#"),
        list("#.......‾‾‾‾‾|‾|‾‾‾‾................................................................. ###........#"),
        list("#...................................................................................#o###........#"),
        list("#.....................................................................)............#####o###.....#"),
        list("#................................................................/ \ ((...........#o#\#|#/###....#"),
        list("#.............................................................../   \||............###\|/#o#.....#"),
        list("#............................................"u"\U0001F6B9""................/     \|.............# }|{ #..\....#"),
        list("#...................____-^-____.............................../.......\...............}|{........#"),
        list("#................../     _   ' \..............................|,^, ,^,|..........................#"),
        list("#................./     |_|     \.............................||_| |_||..........................#"),
        list("#................/               \............................||_| |_||..........................#"),
        list("#.............../|     _____     |\...........................|       |..........................#"),
        list("#............... |    |==|==|    |............................'======='..........................#"),
        list("#................|    |--|--|    |...............................................................#"),
        list("#................|    |==|==|    |...............................................................#"),
        list("#................^^^^^^^^^^^^^^^^^..............@................................................#"),
        list("#................................................................................................#"),
        list("##################################################################################################")]

    return matrix


def start_disp(matrix):
    for i in matrix:
        print("".join(i).rjust(RJUST_SIZE, " "))


def display_background(matrix, left_column):
    length_list_1 = [len(str(item[0])) for item in left_column]
    length_list_2 = [len(str(item[1])) for item in left_column]
    max_size_1 = max(length_list_1) + 2
    max_size_2 = max(length_list_2) + 2
    for i in range(0, len(matrix)):
        if i < len(left_column):
            print(left_column[i][0].ljust(max_size_1, " "), str(left_column[i][1]).ljust(max_size_2, " "), end="")
            print(''.join(matrix[i]))
        else:
            print(''.join(matrix[i]).rjust(max_size_1 + max_size_2 + len(matrix[0]) + 1, " "))


def random_barriers(game_matrix, max_size=15):
    barrier_size_x = random.randint(1, max_size)
    barrier_size_y = random.randint(1, max_size)
    barrier_start_x = random.randint(1, len(game_matrix) - barrier_size_x)
    barrier_start_y = random.randint(1, len(game_matrix[0]) - barrier_size_y)
    for i in range(barrier_start_x, barrier_start_x + barrier_size_x):
        for j in range(barrier_start_y, barrier_start_y + barrier_size_y):
            game_matrix[i][j] = "#"
    return game_matrix


def level_creating(game_matrix):
    stalactite = random.randint(2, 6)
    stalagmite = random.randint(2, 6)
    for i in range(2, len(game_matrix[0])):
        stalactite = stalactite + random.randint(-1, 1)
        stalagmite = stalagmite + random.randint(-1, 1)
        if stalactite > 7 or stalactite < 2:
            stalactite = random.randint(2, 4)
        if stalagmite > 7 or stalagmite < 2:
            stalagmite = random.randint(2, 4)
        for j in range(1, stalactite):
            game_matrix[j][i] = "#"
        for k in range(1, stalagmite):
            game_matrix[-k][i] = "#"
    return game_matrix


def mobs_positions(game_matrix, mob_list, TERRY, TERRX):
    mob_pos_x = random.randint(1, TERRY - 1)
    mob_pos_y = random.randint(1, TERRX - 1)
    mob_type = random.choice(mob_list)
    if game_matrix[mob_pos_x][mob_pos_y] not in ["#", "@"]:
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
        roll = (random.randint(1, 10)) + attributes["strenght"]
        mobhp -= roll
        print('Your hit dealt ', str(roll), ' damage.')
        print('Enemy have %d HP left.' % mobhp)
        time.sleep(1)
        sys.stdout.write("\033[F")
        sys.stdout.write("\033[K")
        sys.stdout.write("\033[F")
        sys.stdout.write("\033[K")
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
            print(
                'Enemy have %d HP left.' % mobhp)
            time.sleep(1)
            sys.stdout.write("\033[F")
            sys.stdout.write("\033[K")
            sys.stdout.write("\033[F")
            sys.stdout.write("\033[K")
            if attributes['hp'] < 1:
                matrix = game_over(matrix)
                os.system("printf '\033c'")
                display_background(matrix,[["",""]])
                sys.exit()
            else:
                battle(matrix, new_pos1, new_pos2, mobhp, inv)
    elif choice == '2':
        roll = (random.randint(1, 6))
        mobhp -= roll
        print('Your hit dealt ', str(roll), ' damage')
        print('Enemy have %d HP left.' % mobhp)
        time.sleep(1)
        sys.stdout.write("\033[F")
        sys.stdout.write("\033[K")
        sys.stdout.write("\033[F")
        sys.stdout.write("\033[K")
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
                roll = (random.randint(1, 6)) + int(attributes["agility"] / 2)
                mobhp -= roll
                print('Your hit dealt ', str(roll), ' damage')
                print(
                    'Enemy have %d HP left.' % mobhp)
                time.sleep(1)
                sys.stdout.write("\033[F")
                sys.stdout.write("\033[K")
                sys.stdout.write("\033[F")
                sys.stdout.write("\033[K")
                sys.stdout.write("\033[F")
                sys.stdout.write("\033[K")
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
                    print(
                        'Enemy have %d HP left.' % mobhp)
                    time.sleep(1)
                    sys.stdout.write("\033[F")
                    sys.stdout.write("\033[K")
                    sys.stdout.write("\033[F")
                    sys.stdout.write("\033[K")
                    if attributes['hp'] < 1:
                        matrix = game_over(matrix)
                        os.system("printf '\033c'")
                        display_background(matrix,[["",""]])
                        sys.exit()
                    else:
                        battle(matrix, new_pos1, new_pos2, mobhp, inv)
            else:
                roll = (random.randint(1, 6)) + 3
                attributes['hp'] -= roll
                print('You lost ', str(roll), " health points. You have ", repr(attributes['hp']), " left.")
                print(
                    'Enemy have %d HP left.' % mobhp)
                time.sleep(1)
                sys.stdout.write("\033[F")
                sys.stdout.write("\033[K")
                sys.stdout.write("\033[F")
                sys.stdout.write("\033[K")
                if attributes['hp'] < 1:
                    matrix = game_over(matrix)
                    os.system("printf '\033c'")
                    display_background(matrix,[["",""]])
                    sys.exit()
                else:
                    battle(matrix, new_pos1, new_pos2, mobhp, inv)

    elif choice == '3':
        if attributes['mp'] > 5:
            roll = (random.randint(1, 15)) + attributes['power']
            attributes['mp'] -= 5
            mobhp -= roll
            print('Your spell dealt ', str(roll), ' damage. You have ', repr(attributes['mp']), " mana left.")
            print(
                'Enemy have %d HP left.' % mobhp)
            time.sleep(1)
            sys.stdout.write("\033[F")
            sys.stdout.write("\033[K")
            sys.stdout.write("\033[F")
            sys.stdout.write("\033[K")
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
                print(
                    'Enemy have %d HP left.' % mobhp)
                time.sleep(1)
                sys.stdout.write("\033[F")
                sys.stdout.write("\033[K")
                sys.stdout.write("\033[F")
                sys.stdout.write("\033[K")
                if attributes['hp'] < 1:
                    matrix = game_over(matrix)
                    os.system("printf '\033c'")
                    display_background(matrix,[["",""]])
                    sys.exit()
                else:
                    battle(matrix, new_pos1, new_pos2, mobhp, inv)
        else:
            print('You do not have enough mana!')
            time.sleep(1)
            sys.stdout.write("\033[F")
            sys.stdout.write("\033[K")
            battle(matrix, new_pos1, new_pos2, mobhp, inv)
    elif choice == '4':
        if "hp potion" in inv or "mana potion" in inv:
            print('Would you like to use\n1. Health potion or\n2. Mana potion?')
            x = getch()
            sys.stdout.write("\033[F")
            sys.stdout.write("\033[K")
            sys.stdout.write("\033[F")
            sys.stdout.write("\033[K")
            sys.stdout.write("\033[F")
            sys.stdout.write("\033[K")
            if x == "1":
                if 'hp potion' in inv:
                    if attributes['hp'] >= attributes['endurance'] * 10 - 5:
                        attributes['hp'] = attributes['endurance'] * 10
                    else:
                        attributes['hp'] += 5
                    print('You regained 5 Health points. You have ', repr(attributes['hp']), " left.")
                    time.sleep(2)
                    sys.stdout.write("\033[F")
                    sys.stdout.write("\033[K")
                    if inv["hp potion"] > 1:
                        inv["hp potion"] = inv["hp potion"] - 1
                        battle(matrix, new_pos1, new_pos2, mobhp, inv)
                    else:
                        del inv["hp potion"]
                        battle(matrix, new_pos1, new_pos2, mobhp, inv)
                else:
                    print('You have no Health potions left!')
                    time.sleep(1)
                    sys.stdout.write("\033[F")
                    sys.stdout.write("\033[K")
            if x == "2":
                if 'mana potion' in inv:
                    if attributes['mp'] >= attributes['mana'] * 10 - 5:
                        attributes['mp'] = attributes['mana'] * 10
                    else:
                        attributes['hp'] += 5
                    print('You regained 5 Mana points. You have ', repr(attributes['mp']), " left.")
                    time.sleep(2)
                    sys.stdout.write("\033[F")
                    sys.stdout.write("\033[K")
                    if inv["mana potion"] > 1 or inv["mana potion" != "nothing"]:
                        inv["mana potion"] = inv["mana potion"] - 1
                        battle(matrix, new_pos1, new_pos2, mobhp, inv)
                    else:
                        del inv["mana potion"]
                        battle(matrix, new_pos1, new_pos2, mobhp, inv)
                else:
                    print('You have no Health potions left!')
                    time.sleep(2)
                    sys.stdout.write("\033[F")
                    sys.stdout.write("\033[K")
                    battle(matrix, new_pos1, new_pos2, mobhp, inv)
            else:
                battle(matrix, new_pos1, new_pos2, mobhp, inv)
        else:
            print("You don't have any items to use. ")
            time.sleep(1)
            sys.stdout.write("\033[F")
            sys.stdout.write("\033[K")
            battle(matrix, new_pos1, new_pos2, mobhp, inv)
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
            print('You lost ', repr(roll), ' Health points. You have ', repr(attributes['hp']), " left.")
            if attributes['hp'] < 1:
                matrix = game_over(matrix)
                os.system("printf '\033c'")
                display_background(matrix,[["",""]])
                sys.exit()
            else:
                battle(matrix, new_pos1, new_pos2, mobhp, inv)
    else:
        battle(matrix, new_pos1, new_pos2, mobhp, inv)

def boss_game_over():
    GAME_OVER = """
      ▄████  ▄▄▄       ███▄ ▄███▓▓█████     ▒█████   ██▒   █▓▓█████  ██▀███
     ██▒ ▀█▒▒████▄    ▓██▒▀█▀ ██▒▓█   ▀    ▒██▒  ██▒▓██░   █▒▓█   ▀ ▓██ ▒ ██▒
    ▒██░▄▄▄░▒██  ▀█▄  ▓██    ▓██░▒███      ▒██░  ██▒ ▓██  █▒░▒███   ▓██ ░▄█ ▒
    ░▓█  ██▓░██▄▄▄▄██ ▒██    ▒██ ▒▓█  ▄    ▒██   ██░  ▒██ █░░▒▓█  ▄ ▒██▀▀█▄
    ░▒▓███▀▒ ▓█   ▓██▒▒██▒   ░██▒░▒████▒   ░ ████▓▒░   ▒▀█░  ░▒████▒░██▓ ▒██▒
     ░▒   ▒  ▒▒   ▓▒█░░ ▒░   ░  ░░░ ▒░ ░   ░ ▒░▒░▒░    ░ ▐░  ░░ ▒░ ░░ ▒▓ ░▒▓░
      ░   ░   ▒   ▒▒ ░░  ░      ░ ░ ░  ░     ░ ▒ ▒░    ░ ░░   ░ ░  ░  ░▒ ░ ▒░
    ░ ░   ░   ░   ▒   ░      ░      ░      ░ ░ ░ ▒       ░░     ░     ░░   ░
          ░       ░  ░       ░      ░  ░       ░ ░        ░     ░  ░   ░
                                                         ░                   """
    os.system("printf '\033c'")
    print("{0:^110}".format(GAME_OVER))
    sys.exit()

def game_over(matrix):
    GAME_OVER = """
      ▄████  ▄▄▄       ███▄ ▄███▓▓█████     ▒█████   ██▒   █▓▓█████  ██▀███
     ██▒ ▀█▒▒████▄    ▓██▒▀█▀ ██▒▓█   ▀    ▒██▒  ██▒▓██░   █▒▓█   ▀ ▓██ ▒ ██▒
    ▒██░▄▄▄░▒██  ▀█▄  ▓██    ▓██░▒███      ▒██░  ██▒ ▓██  █▒░▒███   ▓██ ░▄█ ▒
    ░▓█  ██▓░██▄▄▄▄██ ▒██    ▒██ ▒▓█  ▄    ▒██   ██░  ▒██ █░░▒▓█  ▄ ▒██▀▀█▄
    ░▒▓███▀▒ ▓█   ▓██▒▒██▒   ░██▒░▒████▒   ░ ████▓▒░   ▒▀█░  ░▒████▒░██▓ ▒██▒
     ░▒   ▒  ▒▒   ▓▒█░░ ▒░   ░  ░░░ ▒░ ░   ░ ▒░▒░▒░    ░ ▐░  ░░ ▒░ ░░ ▒▓ ░▒▓░
      ░   ░   ▒   ▒▒ ░░  ░      ░ ░ ░  ░     ░ ▒ ▒░    ░ ░░   ░ ░  ░  ░▒ ░ ▒░
    ░ ░   ░   ░   ▒   ░      ░      ░      ░ ░ ░ ▒       ░░     ░     ░░   ░
          ░       ░  ░       ░      ░  ░       ░ ░        ░     ░  ░   ░
                                                         ░                   """
    ascii_prepare = GAME_OVER.split("\n")
    ascii_matrix = []
    for i in range(len(ascii_prepare)):
        ascii_matrix.append(list(ascii_prepare[i]))
    ascii_len_list = []
    for i in range(len(ascii_matrix)):
        ascii_len_list.append(len(ascii_matrix[i]))
    for j in range(max(ascii_len_list)-min(ascii_len_list)):
        for i in range(len(ascii_matrix)):
            if len(ascii_matrix[i]) < max(ascii_len_list):
                ascii_matrix[i].append(" ")

    print(len(matrix[0]), len(ascii_matrix[0]), len(matrix), len(ascii_matrix))
    game_over_start_x = int(((len(matrix[0]) - len(ascii_matrix[0])) / 2))
    game_over_start_y = int(((len(matrix) - len(ascii_matrix)) / 2))
    for i in range(game_over_start_y, game_over_start_y + len(ascii_matrix)):

        for j in range(game_over_start_x, game_over_start_x + len(ascii_matrix[0])):
            matrix[i][j] = ascii_matrix[i - game_over_start_y][j - game_over_start_x]

    return matrix


def travel():
    x = input('Hello! Would you like to go back to definitely not Tristram? (yes for travel): ').lower()
    if x == 'yes':
        os.system("printf '\033c'")
        tristram()
    else:
        print('As you wish')
        time.sleep(1)


def encounter(matrix, new_pos1, new_pos2):  # [u"\U0001F577", u"\U0001F6B9", u"\U0001F43A",u"\U0001F40D",u"\U0001F41B"]
    if matrix[new_pos1][new_pos2] == u"\U0001F6B9":
        mobhp = 15
        print('You have encountered an NPC ')
        choice = input('What would you like to do (fight/travel/sell/buy/save): ').lower()
        if choice == 'fight':
            print('1. Strong attack\n2. Quick attack\n3. Spell\n4. Use item\n5. Run ')
            battle(matrix, new_pos1, new_pos2, mobhp, inv)
        elif choice == 'travel':
            travel()
        elif choice == 'sell':
            sell(inv, equiped, items)
        elif choice == 'buy':
            buy(inv)
        elif choice == 'save':
            print("Your progress has been saved: ")
            time.sleep(1)
            save()
        else:
            print("Farewell!")
            time.sleep(1)
    else:
        if matrix[new_pos1][new_pos2] == u"\U0001F577":
            mobhp = 15
        elif matrix[new_pos1][new_pos2] == u"\U0001F43A":
            mobhp = 25
        elif matrix[new_pos1][new_pos2] == u"\U0001F40D":
            mobhp = 30
        else:
            mobhp = 10
        print('You were attacked by a feroucious beast! ')
        print('1. Strong attack\n2. Quick attack\n3. Spell\n4. Use item\n5. Run ')
        battle(matrix, new_pos1, new_pos2, mobhp, inv)
    return matrix


def sell(inventory, equiped, items):
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
        nazwy = [seq[0] for seq in head] + [seq[0] for seq in chest] + [seq[0]
                                                                        for seq in legs] + [seq[0] for seq in right_hand] + [seq[0] for seq in left_hand]
        wagi = [seq[1] for seq in head] + [seq[1] for seq in chest] + [seq[1]
                                                                       for seq in legs] + [seq[1] for seq in right_hand] + [seq[1] for seq in left_hand]
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
        choice = input("What do you want to sell?(n to exit): ")
        keys = list(inv.keys())
        values = [seq[0] for seq in head] + [seq[0] for seq in chest] + [seq[0] for seq in legs] + [seq[0]
                                                                                                    for seq in head] + [seq[0] for seq in right_hand] + [seq[0] for seq in left_hand]
        if choice == "n":
            pass
        elif choice in keys and choice in values:
            if inv[choice] > 1:
                inv[choice] = inv[choice] - 1
                inv['gold'] = inv['gold'] + 1
                print("%s sold for 1 gold!" % choice)
                time.sleep(1)
                sell(inventory, equiped, items)
            else:
                del inv[choice]
                inv['gold'] = inv['gold'] + 1
                print("%s sold for 1 gold!" % choice)
                time.sleep(1)
                sell(inventory, equiped, items)
        else:
            print("Can't do that!")
            time.sleep(1)
            sell(inventory, equiped, items)
    else:
        print("Sell what? Look at you!")
        time.sleep(1)


def buy(inventory):
    sys.stdout.write("\033[F")
    sys.stdout.write("\033[K")
    choice = input("What do you want? 'hp potion', or 'mana potion'? 10 g each!: ")
    sys.stdout.write("\033[F")
    sys.stdout.write("\033[K")
    while choice == "hp potion" or choice == "mana potion":
        choice2 = input("How many?: ")
        sys.stdout.write("\033[F")
        sys.stdout.write("\033[K")
        while not choice2.isnumeric():
            print ("HOW MANY!!! Don't you understand?")
            time.sleep(2)
            sys.stdout.write("\033[F")
            sys.stdout.write("\033[K")
            choice2 = input("How many?: ")
            sys.stdout.write("\033[F")
            sys.stdout.write("\033[K")
        choice2 = int(choice2)
        if "gold" in inventory:
            if choice == "hp potion":
                if choice2 * 10 < inv['gold']:
                    inv['gold'] = inv['gold'] - choice2 * 10
                    inv['hp potion'] = inv['hp potion'] + choice2
                    print("%d hp potion bought for %d gold!" % (choice2, choice2 * 10))
                    time.sleep(2)
                    break
                elif choice2 * 10 == inv['gold']:
                    del inv['gold']
                    inv['hp potion'] = inv['hp potion'] + choice2
                    print("%d hp potion bought for %d gold!" % (choice2, choice2 * 10))
                    time.sleep(2)
                    break
                else:
                    print("You poor bastard! You can't afford it!")
                    time.sleep(2)
                    break
            elif choice == "mana potion":
                if choice2 * 10 < inv['gold']:
                    inv['gold'] = inv['gold'] - choice2 * 10
                    inv['mana potion'] = inv['mana potion'] + choice2
                    print("%d mana potion bought for %d gold!" % (choice2, choice2 * 10))
                    time.sleep(2)
                    break
                elif choice2 * 10 == inv['gold']:
                    del inv['gold']
                    inv['mana potion'] = inv['mana potion'] + choice2
                    print("%d mana potion bought for %d gold!" % (choice2, choice2 * 10))
                    time.sleep(2)
                    break
                else:
                    print("You poor bastard! You can't afford it!")
                    time.sleep(2)
                    break
        else:
            print("Gold? You know what it is don't you?")
            time.sleep(2)
            break
    print("Hmmmm! Good bye! ")
    time.sleep(2)
    return


def pick_up(matrix, new_pos1, new_pos2, inventory, items):
    old_player_pos = [(index, row.index("@")) for index, row in enumerate(matrix) if "@" in row]
    old_player_pos = old_player_pos[0]
    old_pos1 = old_player_pos[0]
    old_pos2 = old_player_pos[1]
    itemsss = [seq[1] for seq in items]
    if matrix[new_pos1][new_pos2] in itemsss:
        picked_loot = matrix[new_pos1][new_pos2]
        matrix[new_pos1][new_pos2] = "@"
        matrix[old_pos1][old_pos2] = "."
        item_random(picked_loot, inventory)
        return matrix


def new_column(matrix):
    old_stalactite = 0
    for i in range(1, 14):
        if matrix[i][83] == "#":
            old_stalactite += 1
    stalactite = old_stalactite + random.choice([-1, 0, 1, 1, 1, 2, 3, 4, 3, 3, 4])
    old_stalagmite = 0
    for i in range(len(matrix) - 8, len(matrix) - 1):
        if matrix[i][83] == "#":
            old_stalagmite += 1
    stalagmite = old_stalagmite + random.choice([-1, 0, 1, 1, 1, 2, 3, 4, 3, 3, 4])
    if stalactite + stalagmite > 20:
        stalactite = stalactite - 2
        stalagmite = stalagmite - 2

    for j in range(1, stalactite):
        matrix[j][84] = "#"
    for k in range(0, stalagmite):
        matrix[-k][84] = "#"

    last_column_list = []
    for i in range(1, len(matrix) - 1):
        last_column_list.append(matrix[i][84])

    return last_column_list


def player_tristram(matrix, pos1, pos2):
    old_player_pos = [(index, row.index("@")) for index, row in enumerate(matrix) if "@" in row]
    old_player_pos = old_player_pos[0]
    old_pos1 = old_player_pos[0]
    old_pos2 = old_player_pos[1]
    new_pos1 = old_pos1 + pos1
    new_pos2 = old_pos2 + pos2

    if matrix[new_pos1][new_pos2] in ("#", "-", "|", "/", "o", "‾", "}", ")", "(", ",", "^", "=", "-", "^", "{", "_"):
        return matrix
    elif matrix[new_pos1][new_pos2] == "⛧":
        go_to_dungeon()
    elif matrix[new_pos1][new_pos2] == u"\U0001F6B9":
        npc_tristram()
    else:
        matrix[new_pos1][new_pos2] = "@"
        matrix[old_pos1][old_pos2] = "."
    return matrix


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
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0]) - 2):
                matrix[i][j] = matrix[i][j + 1]
        for i in range(1, len(matrix) - 1):
            matrix[i][84] = "."
        last_column_content = new_column(matrix)
        for i in range(1, len(matrix) - 2):
            matrix[i][84] = last_column_content[i]
        npc_index = MOB_TYPES.index(u"\U0001F6B9")
        npc_to_display = MOB_TYPES[npc_index]
        mob_list_without_npc = MOB_TYPES[:npc_index:]
        mob_chance = random.randint(1, 100)
        if mob_chance > 40:
            mob_pos_x = random.randint(1, 24)
            mob_type = random.choice(MOB_TYPES)
            if matrix[mob_pos_x][84] != "#":
                matrix[mob_pos_x][84] = mob_type
        npc_chance = random.randint(1, 1000)
        if npc_chance < 2:
            npc_pos_x = random.randint(1, 24)
            npc_type = random.choice(npc_to_display)
            if matrix[npc_pos_x][84] != "#":
                matrix[npc_pos_x][84] = npc_type
        item_chance = random.randint(1, 1500)
        item_list = [item[1] for item in items]
        if item_chance < 2:
            item_pos_x = random.randint(1, 24)
            item_type = random.choice(item_list)
            if matrix[item_pos_x][84] != "#":
                matrix[item_pos_x][84] = item_type

    else:
        matrix[new_pos1][new_pos2] = "@"
        matrix[old_pos1][old_pos2] = "."
    for mob in MOB_TYPES:
        for i in range(random.randint(3, 30)):
            if mob == u"\U0001F6B9":
                break
            old_mob_pos = [(index, row.index(mob)) for index, row in enumerate(matrix) if mob in row]
            if old_mob_pos == []:
                break
            old_mob_pos = old_mob_pos[0]
            old_mob_pos1 = old_mob_pos[0]
            old_mob_pos2 = old_mob_pos[1]
            new_mob_pos1 = old_mob_pos1 + random.randint(-1, 1)
            new_mob_pos2 = old_mob_pos2 + random.randint(-1, 1)
            if matrix[new_mob_pos1][new_mob_pos2] != ".":
                break
            matrix[new_mob_pos1][new_mob_pos2] = mob
            matrix[old_mob_pos1][old_mob_pos2] = "."
    return matrix


def npc_tristram():
    os.system("printf '\033c'")
    if attributes['exp'] < 20:
        print("\n"*8)
        print("{:^110}""{:^20}".format("Only the worthy can battle the Lord of the Underworld!\n\n",
              "Get more experience!(20 needed)"))
        time.sleep(2)
        os.system("printf '\033c'")
        tristram()
    else:
        print("{:^70}""{:^70}".format("You may meet the Lord of the Underworld now!", ""))
        boss()


def go_to_dungeon():
    os.system("printf '\033c'")
    terrain = background(TERRY, TERRX)
    terrain[int(TERRY / 2)][1] = "@"
    for i in range(10):
        terrain = mobs_positions(terrain, MOB_TYPES, TERRY, TERRX)
        terrain = items2_positions(terrain, MOB_TYPES, items)
    terrain = level_creating(terrain)
    left_column = making_left_column(attributes, inv)
    display_background(terrain, left_column)
    while 1:
        x = getch()
        if x == 'p':
            sys.exit()
        if x == "i":
            stats = print_table(inv, equiped, items, attributes)
        if x == "1" and 'hp potion' in inv:
            if attributes['hp'] > attributes['endurance'] * 10 - 5:
                attributes['hp'] = attributes['endurance'] * 10
            else:
                attributes['hp'] += 5
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
            if attributes['mp'] > attributes['mana'] * 10 - 5:
                attributes['mp'] = attributes['mana'] * 10
            else:
                attributes['mp'] += 5
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
        left_column = making_left_column(attributes, inv)
        display_background(terrain, left_column)


def tristram():
    start_terrain = start_background()
    start_disp(start_terrain)
    while 1:
        x = getch()
        if x == 'p':
            sys.exit()
        while x not in "wsad":
            x = getch()
        position = user_input(x)
        start_terrain = player_tristram(start_terrain, position[0], position[1])
        os.system("printf '\033c'")
        start_disp(start_terrain)


def new_column(matrix):
    old_stalactite = 0
    for i in range(1, 14):
        if matrix[i][83] == "#":
            old_stalactite += 1
    stalactite = old_stalactite + random.choice([-1, 0, 1, 1, 1, 2, 3, 4, 3, 3, 4])
    old_stalagmite = 0
    for i in range(len(matrix) - 8, len(matrix) - 1):
        if matrix[i][83] == "#":
            old_stalagmite += 1
    stalagmite = old_stalagmite + random.choice([-1, 0, 1, 1, 1, 2, 3, 4, 3, 3, 4])
    if stalactite + stalagmite > 20:
        stalactite = stalactite - 2
        stalagmite = stalagmite - 2

    for j in range(1, stalactite):
        matrix[j][84] = "#"
    for k in range(0, stalagmite):
        matrix[-k][84] = "#"

    last_column_list = []
    for i in range(1, len(matrix) - 1):
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
    blank_line = ["", ""]
    line_1 = ["Name", attributes["Name"]]
    line_2 = ["Class", attributes["Class"]]
    level_line = ["Level", attributes['lev']]
    line_3 = ["Agility", attributes["agility"]]
    line_4 = ["Speed", attributes["speed"]]
    line_5 = ["Strenght", attributes["strenght"]]
    line_6 = ["Power", attributes["power"]]
    line_7 = ["HP", str(attributes["hp"]) + "/" + str(attributes["endurance"] * 10)]
    line_8 = ["MP", str(attributes["mp"]) + "/" + str(attributes["mana"] * 10)]
    line_9 = ["Exp", attributes["exp"]]
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
    if 'gold' in keys:
        line_12 = ("Gold:", str(inv["gold"]))
    else:
        line_12 = ("Gold:", "0")
    left_column = [
        blank_line,
        blank_line,
        line_1,
        line_2,
        blank_line,
        level_line,
        blank_line,
        line_3,
        line_4,
        line_5,
        line_6,
        line_7,
        line_8,
        line_9,
        blank_line,
        line_10,
        line_11,
        blank_line,
        line_12]
    return left_column


main_menu()
