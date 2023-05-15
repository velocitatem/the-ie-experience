from graphics import *
import random

def capitals():
    # Create a list of 15 countries and their capitals
    countries = ["Spain", "France", "Italy", "Germany", "Netherlands", "Belgium", "Greece", "Portugal", "Denmark",
                 "Sweden",
                 "Norway", "Finland", "Poland", "Russia", "Switzerland"]
    capitals = ["Madrid", "Paris", "Rome", "Berlin", "Amsterdam", "Brussels", "Athens", "Lisbon", "Copenhagen",
                "Stockholm",
                "Oslo", "Helsinki", "Warsaw", "Moscow", "Bern"]

    win = None
    input_box = None
    user_score = 0
    computer_score = 0
    score_text = None
    countdown_text = None

    # Set up the graphics window
    win = GraphWin("Capital Game", 500, 700)

    # Set up the text input box
    input_box = Entry(Point(250, 650), 20)
    input_box.draw(win)

    # Set up the score counter and display
    user_score = 0
    computer_score = 0
    score_text = Text(Point(250, 50), f"User: {user_score}    Computer: {computer_score}")
    score_text.draw(win)

    # Set up the countdown message
    countdown_text = Text(Point(250, 100), "")
    countdown_text.draw(win)

    # Game loop
    while user_score < 3 and computer_score < 3:

        # Choose a random country
        index = random.randint(0, len(countries) - 1)
        country = countries[index]

        # Prompt the user for the capital
        prompt = Text(Point(250, 300), f"What is the capital of {country}?")
        prompt.draw(win)

        # Wait for the user to enter a guess
        guess = None
        while guess is None:
            click = win.checkMouse()
            if click is not None:
                guess = input_box.getText().strip().capitalize()

        # Clear the input box and hide the prompt
        input_box.setText("")
        prompt.undraw()

        # Check the answer and update the scores
        if guess == capitals[index]:
            user_score += 1
            score_text.setText(f"User: {user_score}    Computer: {computer_score}")
            result_text = Text(Point(250, 400), "Correct!")
        else:
            computer_score += 1
            score_text.setText(f"User: {user_score}    Computer: {computer_score}")
            result_text = Text(Point(250, 400), f"Wrong! The capital is {capitals[index]}")
        capitals.pop(index)
        countries.pop(index)

        result_text.draw(win)

        # Display the result for 1 second
        time.sleep(1)
        result_text.undraw()

        # Display countdown message
        for i in range(3, 0, -1):
            countdown_text.setText(f"Next round starting in {i}...")
            time.sleep(1)
        countdown_text.setText("")

    won_or_not = None
    if user_score == 3:
        final_text = Text(Point(250, 400), "Congratulations, you won!")
        won_or_not = True
    else:
        final_text = Text(Point(250, 400), "Sorry, you lost!")
        won_or_not = False
    final_text.draw(win)

    # Wait for click before closing the window
    win.getMouse()
    win.close()
    return won_or_not

def run():
    return capitals()

if __name__ == "__main__":
    print(run())

