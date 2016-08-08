#!/usr/bin/env python3
# HW05_ex00_TextAdventure.py
##############################################################################
# Imports
from sys import exit

# Body


def infinite_stairway_room(name1,count=0):
    name=name1
    print(name+" walks through the door to see a dimly lit hallway.")
    print("At the end of the hallway is a", count * 'long ', 'staircase going towards some light')
    next = input("> ")

    # infinite stairs option
    if next == "take stairs":
        print(name+' takes the stairs')
        if (count > 0):
            print("but "+name+" is not happy about it")
        infinite_stairway_room(count + 1)
    # option 2 == ?????
    if next == option_2:
        pass


def gold_room(name1):
    name=name1
    print("This room is full of gold.  How much does "+name+" take?")

    next = input("> ")
    if "0" in next or "1" in next:
        how_much = int(next)
    else:
        dead("Man, learn to type a number.")

    if how_much < 50:
        print("Nice, "+name+" is not greedy, you win!")
        exit(0)
    else:
        dead(name+"You greedy goose!")


def bear_room(name1):
    name=name1
    print("There is a bear here.")
    print("The bear has a bunch of honey.")
    print("The fat bear is in front of another door.")
    print("How is "+name+" going to move the bear?")
    bear_moved = False

    while True:
        next = input("> ")

        if next == "take" or "honey":
            dead("The bear looks at "+name+" then slaps his face off.")
        elif next == "taunt" and not bear_moved:
            print("The bear has moved from the door. "+name+" can go through it now.")
            bear_moved = True
        elif next == "taunt" and bear_moved:
            dead("The bear gets pissed off and chews "+name+"\'s leg off.")
        elif next == "open" or "door" and bear_moved:
            gold_room()
        else:
            print("I got no idea what that means.")


def cthulhu_room(name1):
    name=name1
    print("Here "+name+" sees the great evil Cthulhu.")
    print("He, it, whatever stares at "+name+" and "+name+" goes insane.")
    print("Does"+name+" flee for his life or eat his head?")

    next = input("> ")

    if "flee" in next:
        main()
    elif "head" in next:
        dead("Well that was tasty!")
    else:
        cthulhu_room()


def dead(why):
    print("{}\n Good job!".format(why))
    exit(0)


############################################################################
def main():
    # START the TextAdventure game
    name=input("Enter your name: ")
    print("You are in a dark room.")
    print("There is a door to your right and left.")
    print("Which one do you take?")

    next = input("> ")

    if next == "left":
        bear_room(name)
    elif next == "right":
        cthulhu_room(name)
    else:
        infinite_stairway_room(name,3)
        dead("You stumble around the room until you starve.")

if __name__ == '__main__':
    main()
