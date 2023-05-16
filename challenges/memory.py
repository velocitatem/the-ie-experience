from graphics import *
import random
import time
import math

class CircleFG:
    def __init__(self, center, radius, color):
        self.center = center
        self.radius = radius
        self.color = color
        self.circ = None

    def draw(self, win):
        self.circ = Circle(self.center, self.radius)
        self.setFill(self.color)
        self.circ.draw(win)

    def setFill(self, color):
        self.color = color
        if self.circ:
            self.circ.setFill(self.color)

    def is_clicked(self, p):
        if not self.circ:
            return False
        if p is None:
            return False
        x, y = p.getX(), p.getY()
        cx, cy = self.center.getX(), self.center.getY()
        r = self.radius
        if (cx - x) ** 2 + (cy - y) ** 2 <= r ** 2:
            return True
        return False

    def undraw(self):
        if self.circ:
            self.circ.undraw()
            self.circ = None


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
    try:
        win.getMouse()
    except Exception as e:
        return False
    instructions.undraw()

    # Game loop
    while user_score < 3 and computer_score < 3:

        # Choose a random circle to be the different one
        index = random.randint(0, 9)

        # Create 10 circles with a random color
        circles = []
        colours = ['pink', 'red', 'purple', 'green', 'blue']
        color = random.choice(colours)


        # Calculate the dimensions of each cell
        cell_width = win.getWidth() // 3
        cell_height = win.getHeight() // 3

        # Draw the horizontal lines
        for i in range(1, 3):
            line = Line(Point(0, i * cell_height), Point(win.getWidth(), i * cell_height))
            line.setOutline("white")


        # Draw the vertical lines
        for i in range(1, 3):
            line = Line(Point(i * cell_width, 0), Point(i * cell_width, win.getHeight()))
            line.setOutline("white")


        # Calculate the radius of the circles
        radius = min(cell_width, cell_height) // 4

        # set index counter to 0
        i = 0
        # Create the circles in the center of each cell
        for row in range(3):
            for col in range(3):
                if i == index:
                    center_x = (col * cell_width) + (cell_width // 2)
                    center_y = (row * cell_height) + (cell_height // 2)
                    center = Point(center_x, center_y)
                    colour = 'yellow'
                    circle = CircleFG(center, radius, colour)
                    circles.append(circle)
                    circle.draw(win)

                else:
                    center_x = (col * cell_width) + (cell_width // 2)
                    center_y = (row * cell_height) + (cell_height // 2)
                    center = Point(center_x, center_y)
                    circle = CircleFG(center, radius, color)
                    circles.append(circle)
                    circle.draw(win)
                i += 1


        # Wait for 5 seconds
        time.sleep(2)

        # Turn the circles all the same colour
        for i in range(9):
           circles[i].setFill("pink")
           circles[i].draw(win)

        # Check which circle was clicked on
        clicked_circle = None
        while clicked_circle is None:
            click = win.checkMouse()
            for circle in circles:
                if circle.is_clicked(click):
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
        countdown_text.setText(f"Next round starting in {i}...")
        time.sleep(1)
        countdown_text.setText("")

    # Clear the circles from the screen
    for circle in circles:
        circle.undraw()

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
    try:
        return memory_game()
    except:
        return False
    
if __name__ == "__main__":
    print(run())



