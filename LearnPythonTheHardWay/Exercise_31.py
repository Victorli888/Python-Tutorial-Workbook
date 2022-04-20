print("You enter a dark and mysterious room with two iron clad doors\n"
    "do you go through door #1 or door # 2")
print("Please type either 1 or 2")
door = input("> ")

if door == "1":
    print("A Giant bear appears with a cheese in his mouth")
    print("What will you do?")
    print("1. Take the cake.")
    print("2. Scream at the bear.")

    bear = input("> ")

    if bear == "1":
        print(" The bear screams and eats you. \n GAME OVER.")
    elif bear == "2":
        print("Annoyed, The bear bites your head off. \n GAME OVER.")
    else:
        print(f"{bear} that's a way better choice. ")
        print("The bear runs off")

elif door == "2":
    print(""" You stare into an endless abyss at Cthulu's retina.
    1. Blueberries
    2. Yellow Jacket Clothespins
    3. Understanding revolvers yelling melodies.""")

    insanity = input("> ")

    if insanity == "1" or insanity == "2":  # Why would "1" or "2" not work??? Find out why
        #  This causes any input to be true. (impossible to enter else branch)
        print("Your body survives powered by a mind of jello.\n Well done")
    else:
        print("The insanity overwhelms you and rots your eyes "
              "Nice Job ")
else:
    print("This is not how you play my game.\nGAME OVER")
