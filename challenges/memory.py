from graphics import *
import random
import time
import math

class CircleFG:
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color


    def draw(self, win):
        c = self.color
        r = self.radius
        circ = Circle(Point(self.x, self.y), self.radius)
        circ.setFill(self.color)
        circ.draw(win)

    def distance(self, point):
        x1 = point.getX()
        y1 = point.getY()
        return math.sqrt((self.x - x1) * 2 + (self.y - y1) * 2)

    def clicked(self, point):
        return self.distance(point) <= self.radius

    def setFill(self, color):
        self.color = color

def memory_game():
    # Set up the graphics window
    win = GraphWin("Circle Game", 500, 700)

    # Set up the score counter and display
    user_score = 0
    computer_score = 0
    score_text = Text(Point(250, 50), f"User: {user_score}    Computer: {computer_score}")
    score_text.draw(win)

    # Set up the countdown message
    countdown_text = Text(Point(250, 100), "")

    # Set up the instructions
    instructions = Text(Point(250, 300), "Click on the circle that is a different color. Get 3 right to win, 3 wrong to lose.")
    instructions.draw(win)

    # Wait for click to start the game
    win.getMouse()
    instructions.undraw()

    # Game loop
    while user_score < 3 and computer_score < 3:

        # Choose a random circle to be the different one
        index = random.randint(0, 9)

        # Create 10 circles with a random color
        circles = []
        colours = ["pink", "red", "purple", "green", "blue"]
        color = random.choice(colours)
        for i in range(10):
            circle = CircleFG(50 + i * 50, 500, 50, color)
            circle.draw(win)
            circles.append(circle)

        # Set the index-th circle to be a different color
        circles[index].setFill("orange")

        # Print the circles
        for i in range(2):
            for j in range(5):
                circles[i].draw(win)

        # Wait for 5 seconds
        time.sleep(5)

        # Turn the circles all the same colour
        for i in range(10):
           circles[i].setFill("black")

        for i in range(2):
            for j in range(5):
                circles[i].draw(win)

        # Check which circle was clicked on
        clicked_circle = None
        while clicked_circle is None:
            click = win.checkMouse()
            for circle in circles:
                if circle.clicked(click):
                    clicked_circle = circle

        # Check the answer and update the scores
        if clicked_circle == circles[index]:
            user_score += 1
            score_text.setText(f"User: {user_score}    Computer: {computer_score}")
            result_text = Text(Point(250, 400), "Correct!")
        else:
            computer_score += 1
            score_text.setText(f"User: {user_score}    Computer: {computer_score}")
            result_text = Text(Point(250, 400), "Wrong!")
        result_text.draw(win)

        # Display the result for 2 seconds
        time.sleep(2)
        result_text.undraw()

        # Clear the circles from the screen
        for circle in circles:
            circle.undraw()

        # Display countdown message
        for i in range(3, 0, -1):
            countdown_text.setText(f"Next round starting in {i}...")
            time.sleep(1)
        countdown_text.setText("")

    # Display the final message
    if user_score == 3:
        final_text = Text(Point(250, 400), "Congratulations, you won!")
        final_text.draw(win)
    elif computer_score == 3:
        final_text = Text(Point(250, 400), "Sorry, you lost!")
        final_text.draw(win)

    # Wait for click before closing the window
    win.getMouse()
    win.close()

def run():
    memory_game()

run()