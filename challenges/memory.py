from graphics import *
import random

class MemoryGame:
    def __init__(self, win):
        self.win = win
        self.shapes = ["square", "circle", "triangle", "diamond", "star", "hexagon", "pentagon", "octagon"] * 2
        self.colors = ["red", "green", "blue", "yellow", "purple"]
        self.grid = []
        self.selected = []
        self.matches = 0
        self.user_wins = 0
        self.user_losses = 0

    def draw_grid(self):
        for row in range(3):
            self.grid.append([])
            for col in range(4):
                x = 100 + col * 100
                y = 100 + row * 100
                shape_type = self.shapes.pop()
                color = self.colors[random.randint(0,4)]
                if shape_type == "square":
                    shape = Rectangle(Point(x - 40, y - 40), Point(x + 40, y + 40))
                elif shape_type == "circle":
                    shape = Circle(Point(x, y), 40)
                elif shape_type == "triangle":
                    shape = Polygon(Point(x, y - 40), Point(x - 40, y + 40), Point(x + 40, y + 40))
                elif shape_type == "diamond":
                    shape = Polygon(Point(x, y - 40), Point(x - 40, y), Point(x, y + 40), Point(x + 40, y))
                elif shape_type == "star":
                    shape = Polygon(Point(x, y - 40), Point(x - 20, y - 10), Point(x - 40, y + 30), Point(x, y + 10), Point(x + 40, y + 30), Point(x + 20, y - 10))
                elif shape_type == "hexagon":
                    shape = Polygon(Point(x - 30, y), Point(x - 15, y + 30), Point(x + 15, y + 30), Point(x + 30, y), Point(x + 15, y - 30), Point(x - 15, y - 30))
                elif shape_type == "pentagon":
                    shape = Polygon(Point(x, y - 40), Point(x - 40, y - 15), Point(x - 25, y + 35), Point(x + 25, y + 35), Point(x + 40, y - 15))
                elif shape_type == "octagon":
                    shape = Polygon(Point(x - 30, y - 30), Point(x - 30, y + 30), Point(x - 10, y + 50), Point(x + 10, y + 50), Point(x + 30, y + 30), Point(x + 30, y - 30), Point(x + 10, y - 50), Point(x - 10, y - 50))
                shape.setFill(color)
                shape.setOutline("black")
                shape.draw(self.win)
                self.grid[row].append({"shape": shape, "type": shape_type, "color": color})

    def select_shape(self, shape):
        """
        This method is called when a shape is clicked by the user.
        It updates the state of the game by highlighting the selected shape
        and checking if the selected shapes match.
        """
        if len(self.selected) < self.num_shapes:
            if shape not in self.selected:
                shape.setFill("blue")
                self.selected.append(shape)
                if len(self.selected) == self.num_shapes:
                    self.win.after(1000, self.check_selection)
        else:
            self.selected = []

    def check_selection(self):
        """
        This method checks if the selected shapes match or not.
        If the shapes match, they are highlighted in green and the user score is updated.
        If the shapes don't match, they are reset to white and the user has one less chance.
        """
        selected_shapes = [shape.clone() for shape in self.selected]
        self.selected = []
        shape_types = [shape.getType() for shape in selected_shapes]
        shape_colours = [shape.config["fill"] for shape in selected_shapes]
        if shape_types == self.current_pattern["shapes"] and shape_colours == self.current_pattern["colours"]:
            for shape in selected_shapes:
                shape.setFill("green")
                shape.setOutline("green")
            self.matches += 1
            if self.matches == self.num_rounds:
                self.user_wins += 1
                self.end_game()
            else:
                self.win.after(1000, self.show_pattern)
        else:
            for shape in selected_shapes:
                shape.setFill("white")
            self.chances_left -= 1
            if self.chances_left == 0:
                self.user_losses += 1
                self.end_game()
            else:
                self.remaining_chances.setText(f"You have {self.chances_left} chances remaining.")

    def end_game(self,end=True):
        # Undraw all the shapes on the grid
        for row in self.grid:
            for item in row:
                item["shape"].undraw()

        # Create a text object to display the final result
        if self.user_wins == 3:
            final_result = Text(Point(250, 300), "Congratulations! You won the game.")
        else:
            final_result = Text(Point(250, 300), "Game over. Better luck next time.")
        final_result.setSize(20)
        final_result.draw(self.win)

        # Close the window after 2 seconds
        self.win.after(2000, self.win.close)

    def play(self):
        while self.user_wins < 3 and self.user_losses < 3:
            # Show message for remaining losses
            remaining_losses = Text(Point(250, 650), f"You have {3 - self.user_losses} remaining losses.")
            remaining_losses.setSize(18)
            remaining_losses.draw(self.win)

            # Generate a list of random shapes to display
            shapes_to_click = []
            for i in range(6):
                shape_type = random.choice(self.shapes)
                color = random.choice(self.colors)
                shape = self.generate_shape(shape_type, color)
                shape.draw(self.win)
                shapes_to_click.append((shape, shape_type, color))
                time.sleep(1)
                shape.undraw()
                time.sleep(0.5)

            # Get user input for clicking the shapes
            self.selected = []
            for i in range(6):
                click = self.win.getMouse()
                clicked_shape = self.get_clicked_shape(click, shapes_to_click)
                if clicked_shape:
                    clicked_shape.setFill("blue")
                    self.selected.append(clicked_shape)
                else:
                    self.user_losses += 1
                    remaining_losses.setText(f"You have {3 - self.user_losses} remaining losses.")
                    if self.user_losses == 3:
                        break

            # Check if user clicked the shapes in the correct order
            if self.selected == shapes_to_click:
                self.user_wins += 1
                if self.user_wins == 3:
                    self.end_game(won=True)
            else:
                for shape in self.selected:
                    shape.setFill("red")
                    time.sleep(0.5)
                    shape.setFill(shape.color)
                if self.user_losses == 3:
                    self.end_game(won=False)

            self.win.getMouse()


win = GraphWin("Memory Game", 500, 700)
game = MemoryGame(win)
game.draw_grid()
