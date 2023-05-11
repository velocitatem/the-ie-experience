from graphics import *
import random

def classroom_puzzle():

    # Set up window
    win = GraphWin("Debugging Game", 500, 700)

    # Create message for user
    welcome = Text(Point(250, 100), "Welcome to the Debugging Game!")
    welcome.setSize(20)
    welcome.draw(win)

    # Set up variables to track wins and losses
    user_wins = 0
    user_losses = 0

    # Play game until either user wins 3 times or loses 3 times
    while user_wins < 3 and user_losses < 3:

        # Generate random code with a deliberate bug
        code = "x = 5\ny = 2\nz = x + y * 2"  # There is a bug in this code
        code_box = Entry(Point(250, 300), 50)
        code_box.setText(code)
        code_box.draw(win)

        # Prompt user to enter their debug
        prompt = Text(Point(250, 350), "Please debug the code above:")
        prompt.setSize(18)
        prompt.draw(win)

        # Get user input for debug
        user_input = Entry(Point(250, 400), 30)
        user_input.draw(win)

        # Wait for user to enter their debug
        while not win.checkMouse():
            pass

        # Check if user input is correct
        if user_input.getText() == "z = x + y * 2":
            result = Text(Point(250, 450), "Correct! You win this round.")
            user_wins += 1
        else:
            result = Text(Point(250, 450), "Incorrect. Try again.")
            user_losses += 1

        # Remove input boxes and display result
        code_box.undraw()
        prompt.undraw()
        user_input.undraw()
        result.setSize(18)
        result.draw(win)

        # Display number of remaining losses as a countdown from 3
        if user_losses < 3:
            remaining_losses = Text(Point(250, 550), f"You have {3 - user_losses} remaining losses.")
            remaining_losses.setSize(18)
            remaining_losses.draw(win)

        # Wait for mouse click before clearing the screen for the next round
        win.getMouse()
        for item in win.items[:]:
            item.undraw()
        welcome.draw(win)


    if user_wins == 3:
        final_result = Text(Point(250, 300), "Congratulations! You won the game.")
    else:
        final_result = Text(Point(250, 300), "Game over. Better luck next time.")
    final_result.setSize(20)
    final_result.draw(win)

    # Wait for mouse click before closing the window
    win.getMouse()
    win.close()
