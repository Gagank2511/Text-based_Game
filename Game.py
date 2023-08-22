# This is the default function before editing (don't touch)
    # player_input = input(
    #     "...\n")
    # while True:
    #     if player_input.lower() == "...":
    #         passage()
    #     else:
    #         player_input = input(
    #             "Invalid input, please try again. ...\n")
    #         continue


def armoury(): # In armoury looking for sword
    global has_sword
    player_input = input("Go to the armoury and take a sword from the armoury. TAKE a sword from the armoury.\n")
    
    while True:
        if player_input.lower() == "take": # Takes sword from armoury
            has_sword = True
            town_destroyed()
        else:
            player_input = input("Invalid input, please try again. TAKE a sword from the armoury.\n")
            continue


def character_creation(): # Customize character name
    global player_name
    player_input = input(
        "...\n")
    while True:
        if player_input.lower() == "...": # Game Introduction
            introduction()
        else:
            player_input = input(
                "Invalid input, please try again. ...\n")
            continue


def choke_shaman(): # You choke the goblin shaman to death, taking his knife and a spellbook
    player_input = input(
        "...\n")
    while True:
        if player_input.lower() == "...": # Pursue the dragon
            follow_dragon()
        else:
            player_input = input(
                "Invalid input, please try again. ...\n")
            continue


def dragon_attack(): # Witnesses dragon attacking the town
    global has_amulet
    global has_spellbook
    player_input = input(
        "...\n")
    while True:
        if player_input.lower() == "...": # Follows father
            print("...")
            break
        elif player_input.lower() == "...": # Hides in cellar
            ...()
        elif player_input.lower() == "...": # Secures amulet
            has_amulet = True
            ...()
        elif player_input.lower() == "...": # Searches for spellbook
            has_spellbook = True
            ...()
        else:
            player_input = input(
                "Invalid input, please try again. ...\n")
            continue


def follow_dragon():
    ...


def follow_father(): # You follow your father to defend the town
    print("...") # Meet a gruesome fate alongside him


def goblin_cave(): # Arrive at goblin shaman's cave
    global has_knife
    global has_spellbook
    player_input = input(
        "...\n")
    while True:
        if player_input.lower() == "...": # Steal a magic book
            has_spellbook = True
            steal_book()
        elif player_input.lower() == "...": # Kill the goblin shaman
            has_knife = True
            has_spellbook = True
            choke_shaman()
        else:
            player_input = input(
                "Invalid input, please try again. ...\n")
            continue


def introduction(): # Introduces the story
    player_input = input(
        "...\n")
    while True:
        if player_input.lower() == "...": # Training with father
            training()
        else:
            player_input = input(
                "Invalid input, please try again. ...\n")
            continue


def move_on(): # Move on and find peace
    print("...") # Moved on and rebuilt family after the attack


def start_game(): # Start of the game
    player_input = input(
        """Welcome, in this game you will embark on a quest to slay a dragon. Your possible actions will be displayed in uppercase. Do you want to 
START the game or NOT?\n""")
    while True:
        if player_input.lower() == "start": # Character creation
            character_creation()
        elif player_input.lower() == "not": # Stop game
            print("That is a shame.")
            break
        else:
            player_input = input(
                "Invalid input, please try again. Do you want to START the game or NOT?\n")
            continue


def steal_book(): # You steal a magic book from the goblin shaman
    player_input = input(
        "...\n")
    while True:
        if player_input.lower() == "...": # Pursue the dragon
            follow_dragon()
        else:
            player_input = input(
                "Invalid input, please try again. ...\n")
            continue


def swear_vengeance(): # Swear to avenge your father
    # Can only go to cave without spellbook, go to market without sword or pursue dragon if have either a spellbook or a sword
    player_input = input(
        "...\n")
    while True:
        if player_input.lower() == "...": # Go to goblin shaman's cave to find useful items
            goblin_cave()
        elif player_input.lower() == "...": # Go to a local market to find a sword
            market()
        elif player_input.lower() == "...": # Pursue the dragon
            follow_dragon()
        else:
            player_input = input(
                "Invalid input, please try again. ...\n")
            continue


def town_destroyed(): # Town is destroyed
    if has_amulet == True: # Secured family heirloom
        print("...")
    elif has_spellbook == True: # Got spellbook from library
        print("...")
    elif has_sword == True: # Got sword from armoury
        print("...")
    else: # Hid in cellar
        print("...")
    player_input = input(
        "...\n")
    while True:
        if player_input.lower() == "...": # Swear to avenge your father
            swear_vengeance()
        elif player_input.lower() == "...": # Move on and find peace
            move_on()
        else:
            player_input = input(
                "Invalid input, please try again. ...\n")
            continue


def training(): # Training with father
    player_input = input(
        "...\n")
    while True:
        if player_input.lower() == "...": # Go to armoury to find sword
            armoury()
        elif player_input.lower() == "...": # Go to the window to see what is happening
            dragon_attack()
        else:
            player_input = input(
                "Invalid input, please try again. ...\n")
            continue


has_amulet = False
has_cursed_ring =  False
has_knife = False
has_spellbook = False
has_sword = False
player_name = ""

start_game()
