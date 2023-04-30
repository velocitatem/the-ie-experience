from graphics import *
from button import Button

global knowledge
global health
global will_to_live

def titleScreen():
    # drawing the Title Screen
    win = GraphWin("Title screen", 500, 500)
    win.setCoords(-10, 10, 500, 500)
    win.setBackground("lightblue")
    welcome = Text(Point(250, 270), "Welcome to the IE Experience").draw(win)
    welcome.setFill("white")
    welcome.setSize(20)

    # graphic elements of welcome page
    pass

    # Explanation of the game (potentially we can also put this on the screen)
    print("In this minigame you will live the experience of an IE student.")
    print("You will be asked to complete a certain number of tasks to get through a day of classes successfully.")

    # Play button
    play_button = Button(win, Point(250, 220), 50, 20, "Play")
    play_button.activate()
    p = win.getMouse()

    if play_button.clicked(p):
        welcome.undraw()
        play_button.undraw()
        introScene()


def introScene():
    # graphics.py design should go here
    pass

    # explanation
    print("You are now starting your day as an IE student. This is your room.")
    print("Your goal is to get through Monday with a will to live, health and knowledge > 20 ")
    print()
    print("Rules: correct decisions will add 10 points, irresponsible decisions will substract 5 points")
    print("if at any point any of the status bars reaches 0, you will loose the game")
    print("You can now choose to have breakfast to start the day")
    print()
    breakfast = input("Type yes if you would like to have breakfast: ")

    # initializing variables to a certain value
    will_to_live = 20
    health = 20
    knowledge = 20

    if breakfast == 'yes':
        will_to_live += 10
        health += 10
        print("YUM, that coffee was good")
    else:
        will_to_live -= 5
        health += 5
        print("another day you dont have breakfast...")

    # Moving to the next scene: going to uni
    print("You have 15 minutes to get to uni! You better rush!")
    to_uni = input("type yes if you would like to go to uni: ")

    if to_uni == 'yes':
        will_to_live -= 2
        toUni()
    elif to_uni == 'no':
        while to_uni != 'yes':
            breakfast2 = input("Would you like another coffee?")
            will_to_live += 10
            health += 1
            print("YUM, that coffee was good")
            to_uni = input("Would you like to go to uni now? ")
            if to_uni == 'yes':
                will_to_live -= 2
                toUni()
                break
    else:
        to_uni = input("Invalid input. Please try again: ")

def toUni():
    # grapics.py code should go here


    # main hall description
    print("You are now in the claustro, this is IE's central patio")

    # where to go now
    direction = input("Where would you like to go: stay, up (classroom), down(cafeteria), left(library) or right(back home)? ")
    if direction == 'up':
        classroom_CSAI()
    elif direction == 'down':
        theCave()
    elif direction == 'left':
        library()
    elif direction == 'right':
        home()
    elif direction == 'stay':
        pass # CHOOSE WHAT TO DO HERE
    else:
        direction = input("Invalid input. Please type again")


def classroom_CSAI():
    # grapics.py code should go here

    # classroom intro
    print("This is the CSAI classroom where the magic takes place")
    print("This room is a bit smelly...")
    print("You should probably know it has an exit to the left in case you have to run away")
    print("At the front there is a blackboard you can click to complete a short puzzle!")

    # insert puzzle
    pass

    # insert exit path (go to diff room)
    pass

def theCave():
    # grapics.py code should go here

    # cafeteria Intro
    print("This is the Cave, every students favourite place")
    coffee = input("Would you like to order something?: ")
    if coffee == "yes":
        cafeteria_food_option = input("We have coffee, granola bar and cookies. Type the snack of your choice: ")
        if cafeteria_food_option == "coffee":
            will_to_live += 10
            health -= 5
            # ADD EXIT OPTION
        elif cafeteria_food_option == "granola bar":
            health -= 20
            # ADD EXIT OPTION
        elif cafeteria_food_option == "cookie":
            will_to_live += 10
            health -= 10
            # ADD EXIT OPTION
    elif coffee == "no":
        direction = input("Where would you like to go next? ")
        if direction == 'up':
            toUni() # MAYBE RE-DEFINE THIS AS CLAUSTRO
        elif direction == 'down':
            direction = input("No room here. You can only go up the stairs. Please choose another direction: ")
        elif direction == 'left':
            direction = input("No room here. You can only go up the stairs. Please choose another direction: ")
        elif direction == 'right':
            direction = input("No room here. You can only go up the stairs. Please choose another direction: ")
        elif direction == 'stay':
            pass  # CHOOSE WHAT TO DO HERE
    else:
        coffee = input("Invalid input. Please type your response again: ")

def library():
    # grapics.py code should go here
    pass
    
    # library intro
    print("This is the IE library. You can exit this room going *down* the stairs.")
    print("Since exams are coming up you should start studying")

    # insert puzzle
    pass

    # insert exit path (go to diff room)
    pass


def home():
    # grapics.py code should go here
    pass

    # home intro
    print("You are finally home. Monday was tough...")
    
    # insert any other thing 
    pass

titleScreen()
    
   
