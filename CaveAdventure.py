# Cave Adventure

name = input("Welcome adventurer! What is your name?\n")
print("Hello, " + name + ". We are going to go on an adventure! \n")
print("You wake up and find yourself outside. ")

sword = "Sword"
lantern = "Lantern"
key = "Key"

inventory = []

def caveEntrance():
    print("You are standing outside and in front of you is the entrance to a cave. ")
    print("There is a waterfall to your left.")
    print("A cliff is located to the right. ")
    print("There is a forest path behind you.\n ")
    direction = input("Which direction would you like to go? Forward/Back/Left/Right \n")
    if direction == "Forward" or direction == "forward":
        caveRoom1()
    elif direction == "Back" or direction == "back":
        print("The game has ended because you were too scared to go into the cave. ")
        quit()
    elif direction == "Left" or direction == "left":
        print("You fell down the waterfall! You died. ")
        quit()
    elif direction == "Right" or direction == "right":
        print("There is a cliff. You would need rope to climb it. ")
        caveEntrance()
    else:
        print("That is not a valid option. ")
        caveEntrance()

def caveRoom1():
    print("You have entered the cave.")
    print("There is a dead end in front of you.")
    print("A wall is to your left.")
    print("The exit to the cave is behind you.")
    print("The cave continues on your right.\n")
    validChoice = False
    while validChoice == False:
        direction = input("Which direction would you like to go? Forward/Back/Left/Right \n")
        if direction == "Forward" or direction == "forward":
            print("You cannot go this way, because there is a dead end. ")
        elif direction == "Back" or direction == "back":
            validChoice = True
            caveEntrance()
        elif direction == "Left" or direction == "left":
            print("You cannot go this way.\n ")
        elif direction == "Right" or direction == "right":
            validChoice = True
            caveRoom2()
        else:
            print("That is not a valid option. ")
            caveEntrance()

def caveRoom2():
    global key
    print("You are now deeper into the cave, and it is getting darker. ")
    print("There is a little bit of sunlight, and you take a look around. You notice a shiny key on the ground beside you.")
    pickUp = input("Do you want to pick up the key? (Yes/No) \n")
    if pickUp.lower() == "yes":
        inventory.append(key)
        print("This item has been added to your inventory.")
    print("There is a wall to your left and right.")
    print("Behind you is the beginning of the cave.")
    print("The cave continues ahead.\n")
    validChoice = False
    while validChoice == False:
        direction = input("Which direction would you like to go? Forward/Back/Left/Right \n")
        if direction == "Forward" or direction == "forward":
            validChoice = True
            caveRoom3()
        elif direction == "Back" or direction == "back":
            validChoice = True
            caveRoom1()
        elif direction == "Left" or direction == "left":
            print("You cannot go this way.\n ")
        elif direction == "Right" or direction == "right":
            print("You cannot go this way.\n ")
        else:
            print("That is not a valid option. ")
            caveEntrance()

def caveRoom3():
    print("You continue going deeper into the cave and it is too dark to see well. ")
    print("There is a wall in front of you and to your left.")
    print("The cave continues on your right.")
    print("Behind you is the cave area that you were just in.\n")
    validChoice = False
    while validChoice == False:
        direction = input("Which direction would you like to go? Forward/Back/Left/Right \n")
        if direction == "Forward" or direction == "forward":
            print("You cannot go this way. \n")
        if direction == "Left" or direction == "left":
            print("You cannot go this way. \n")
        if direction == "Back" or direction == "back":
            validChoice = True
            caveRoom2()
        if direction == "Right" or direction == "right":
            validChoice = True
            caveRoom4()
        else:
            print("That is not a valid option. ")
            caveRoom3()

def caveRoom4():
    global lantern
    print("You continue following the path and see a lantern on the ground.")
    pickUp = input("Do you want to pick it up? (Yes/No)\n")
    if pickUp.lower() == "yes":
        inventory.append(lantern)
        print("You pick up the lantern and turn it on. The lantern works and you can now see clearly.")
        print("This item has been added into your inventory. ")
    print("There is a wall in front of you and to your right.")
    print("The cave continues on your left.")
    print("Behind you is the cave area that you were just in.\n")

    validChoice = False
    while validChoice == False:
        direction = input("Which direction would you like to go? Forward/Back/Left/Right \n")
        if direction == "Forward" or direction == "forward":
            print("You cannot go this way. \n")
        if direction == "Right" or direction == "right":
            print("You cannot go this way. \n")
        if direction == "Back" or direction == "back":
            validChoice = True
            caveRoom3()
        if direction == "Left" or direction == "left":
            validChoice = True
            caveRoom5()
        else:
            print("That is not a valid option. ")
            caveRoom4()

def caveRoom5():
    global lantern
    global sword
    if lantern in inventory:
        print("You continue following the path while holding up your lantern, and see a skeleton leaning against the wall holding a big sword.")
        print("The skeleton moves and talk to you: Hello " + name + "! If you want this sword, you have to answer the riddle correctly. You have 3 tries.")
        answer = "A skeleton"
        for i in range(3):
            riddle = input("I have a heart that doesn’t beat. An iron spine but I'm not strong. I'm all bones and no muscles. What am I? ")
            if riddle.lower() == answer.lower():
                print("That is the correct answer!")
                print("The sword has now been added to your inventory.")
                inventory.append(sword)
                killBear()
            else:
                if i < 2:
                    print("That is incorrect. Try again.")
                else:
                    print("That is incorrect. You have run out of tries and did not get the sword.")
                    killBear()

def killBear():
    print("Suddenly you hear a noise... there's a bear running toward you!")
    if sword in inventory and lantern in inventory:
        print("You swing the sword and kill the bear.\n")
    if sword in inventory and lantern not in inventory:
        print("You can't see where the bear is, so you swing the sword wildly. The bear kills you.\n")
        quit()
    if lantern in inventory and sword not in inventory:
        print("You swing the lantern wildly and scare the bear away.\n")
    if lantern not in inventory and sword not in inventory:
        print("You were attacked by the bear. You died.\n")
        quit()
    if lantern not in inventory:
        print("It is too dark in the cave and you have to guess which way to go.")
    else:
        print("There is a dark pit in front of you.")
        print("There is a wall to your right.")
        print("The cave continues on your left.")
        print("Behind you is the cave area that you were just in.\n")

    validChoice = False

    while validChoice == False:
        direction = input("Which direction would you like to go? Forward/Back/Left/Right \n")
        if direction == "Forward" or direction == "forward":
            print("You fell into the dark pit. You died. \n")
            quit()
        if direction == "Right" or direction == "right":
            print("You cannot go this way. \n")
        if direction == "Back" or direction == "back":
            validChoice = True
            caveRoom4()
        if direction == "Left" or direction == "left":
            validChoice = True
            caveRoom6()
        else:
            print("That is not a valid option. ")
            caveRoom5()

def caveRoom6():
    print("You continue following the path.")
    print("There is a wall in front of you and on your left.")
    print("The end of the cave is to your right.")
    print("Behind you is the cave area that you were just in.\n")
    validChoice = False
    while validChoice == False:
        direction = input("Which direction would you like to go? Forward/Back/Left/Right \n")
        if direction == "Forward" or direction == "forward":
            print("You cannot go this way. \n")
        if direction == "Left" or direction == "left":
            print("You cannot go this way. \n")
        if direction == "Back" or direction == "back":
            validChoice = True
            caveRoom5()
        if direction == "Right" or direction == "right":
            validChoice = True
            caveRoom7()
        else:
            print("That is not a valid option. ")
            caveRoom6()

def caveRoom7():
    print("You have now made it to the end of the cave. ")
    print("There is a wall to your left.")
    print("There is a dark pit on your right.")
    print("The exit is in front of you.")
    print("Behind you is the cave area that you were just in.\n")
    validChoice = False
    while validChoice == False:
        direction = input("Which direction would you like to go? Forward/Back/Left/Right \n")
        if direction == "Forward" or direction == "forward":
            validChoice = True
            caveRoom8()
        if direction == "Left" or direction == "left":
            print("You cannot go this way. \n")
        if direction == "Back" or direction == "back":
            validChoice = True
            caveRoom6()
        if direction == "Right" or direction == "right":
           print("You fell into the dark pit. You died.")
           quit()
        else:
            print("That is not a valid option. ")
            caveRoom7()

def caveRoom8():
    global sword
    print("You have now made it to the end of the cave, but there are vines blocking the exit....")
    if sword in inventory:
        print("You cut the vines with your sword, and you notice a lock on the wall in front of you. \n")
        caveRoom9()
    if lantern in inventory:
        print("You hold the lantern up to the vines and burn them. You notice a lock on the wall in front of you. \n")
        caveRoom9()
    else:
        print("There is a wall to your left and right.")
        print("The vines are blocking the exit in front of you.")
        print("Behind you is the cave area that you were just in.")
        validChoice = False
        while validChoice == False:
            direction = input("Which direction would you like to go? Forward/Back/Left/Right \n")
            if direction == "Forward" or direction == "forward":
                print("You cannot go this way. \n")
            if direction == "Back" or direction == "back":
                 validChoice = True
                 caveRoom7()
            if direction == "Right" or direction == "right":
                print("You cannot go this way.")
                caveRoom8()
            else:
                print("That is not a valid option. ")
                caveRoom8()

def caveRoom9():
    global key
    print("You have to unlock the exit. ")
    if key in inventory:
        print("You attempt to unlock the door with your key. The door unlocks and you have now made it out of the cave!")
        caveExit()
    else:
        print("You have now way of getting out of the cave.")
        quit()

def caveExit():
    print("Congrats " + name + "!" + " You made it out of the cave. There is a treasure chest engraved with waves buried in sand in front of you with a lock.")
    print("Answer the riddle to unlock the treasure chest. You have 3 tries.")
    answer = "a reflection"
    for i in range(3):
        riddle = input("You can see me in water, but I never get wet. What am I?").lower()
        if riddle == answer:
            print("That is the correct answer!")
            print("You unlock the treasure chest with your key and find 100 golden dollars!")
            print("Thanks for playing " + name + "! ")
            quit()
        else:
            if i < 2:  # we subtract 1 because indices start at 0
                print("That is incorrect. Try again.")
            else:
                print("That is incorrect. You have run out of tries.")

    print("You have failed to unlock the treasure chest.")
    print("Thanks for playing " + name + "! ")
    quit()

caveEntrance()