from sys import exit  # From sys we import the exit function that's already packaged with python


def gold_room():
    print("This room is full of gold. How much do you take?")

    choice = input("> ")
    if "0" in choice or "1" in choice:
        how_much = int(choice)
    else:
        dead("Man, learn to type a number.")

    if how_much <= 50:
        print("Nice, You're not greedy, you win!")
        exit(0)
    else:
        dead("You greedy Bastard...")


def bear_room():
    print("There is a bear here.")
    print("The bear has a bunch of honey.")
    print("The fat bear is in front of another door.")
    print("How are you going to move the bear?")
    bear_moved = False

    while True:  # this creates an infinite loop
        choice = input("> ")

        if choice == "take honey":
            dead("The bear mauled you face off")
        elif choice == "taunt bear" and not bear_moved:
            print("The bear moves from the door.")
            print("You can go through it now.")
            bear_moved = True  # since the beear moved we chang the state of the variable
        elif choice == "taunt bear" and bear_moved:
            dead("The bear gets mad and mauls your face")
        elif choice == "open door" and bear_moved:  # we call on the "bear_moved" variable
            gold_room()  # this is the only exit from the infinite While loop
        else:
            print("I've got no idea what you're saying.")


def cthulhu_room():
    print("Here you see the great Cthulhu.")
    print("He, it, whatever stares at you and you go insane.")
    print("Do you flee for your life or eat your head?")

    choice = input("> ")

    if "flee" in choice:  # in choice is much more versatile to use with inputs
        start()
    elif "head" in choice:
        dead("Man that is a tasty burger!")
    else:
        cthulhu_room()


def dead(why):
    print(f'{why} aaaaaand you\'re dead.')
    exit(0)  # calling back to that pre-packaged exit function


def start():
    print("You are in a dark room.")
    print("There is a door to your right and left.")
    print("Which one do you take?")

    choice = input("> ")

    if choice == "left":
        bear_room()
    elif choice == "right":
        cthulhu_room()
    else:
        dead("you stumble around and starve to death.")


start()  # start file by calling the "Start()" function
