from graphics import *
from button import Button

# Initial screen drawing

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

    win.getMouse()
    win.close()
    
    
