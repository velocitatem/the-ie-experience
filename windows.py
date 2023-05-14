# internal dependencies
from person import Person
from game_configuration import ROOMS, ROOM_MATRIX, PUZZLES
from helpers import items_to

from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget, QLineEdit, QProgressBar, QGridLayout, QGroupBox, QRadioButton, QMessageBox, QHBoxLayout
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtCore import Qt
import sys


class GreetingWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("The IE Experience")
        self.setFixedSize(500, 500)
        self.setStyleSheet("background-image: url('IE.png');")


        # Create a central widget and set its layout
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        layout.setAlignment(Qt.AlignCenter)
        layout.setSpacing(10)

        # Create the label and set its properties
        self.label = QLabel("Welcome to the IE Experience!\nPress the button to start the game.", self)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setFont(QFont("Arial", 20))
        layout.addWidget(self.label)

        # Create the button and set its properties
        self.button = QPushButton("Start Game", self)
        self.button.clicked.connect(self.start_game)
        self.button.setFixedSize(100, 50)
        layout.addWidget(self.button)

    def start_game(self):
        # Close the greeting window
        self.close()

        # Open the game window
        self.game = GameWindow()
        self.game.show()


class CoverImageWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("The IE Experience")
        self.setFixedSize(600, 600)
        self.label = None

    def set_image(self, name, file):
        # if we already have a cover image, remove it
        if self.label is not None:
            self.label.setParent(None)
            self.label.deleteLater()
        self.label = QLabel(self)
        pixmap = QPixmap(file)
        self.label.setPixmap(pixmap)
        self.setCentralWidget(self.label)
        self.show()

    def hide_window(self):
        self.hide()

    def closeEvent(self, event):
        self.destroy()


class GameWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("The IE Experience - Game")
        self.setFixedSize(700, 500)

        self.cover_image = CoverImageWindow()
        self.person = Person()
        self.history = ['look']

        # Create a central widget and set its layout
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        layout.setAlignment(Qt.AlignCenter)
        layout.setSpacing(10)

        # Create the input field
        self.input = QLineEdit(self)
        self.input.setFixedSize(500, 50)
        self.input.setPlaceholderText("Enter your command here")
        self.input.returnPressed.connect(self.on_input) # When the user presses enter, call on_input
        layout.addWidget(self.input)

        # Create the position label
        self.position_label = QLabel(self)
        self.position_label.setAlignment(Qt.AlignCenter)
        self.position_label.setFixedSize(500, 100)
        layout.addWidget(self.position_label)

        self.update_status_bar()
        self.update_inventory()

        self.paint_position_label()
        self.cover_open(self.get_room_object())


    def paint_position_label(self):
        self.position_label.setText(f"You are in the {self.person.get_location()}")

    def update_status_bar(self):
        if dir(self).count('status_bar') > 0:
            self.status_bar.deleteLater()
        # we create status bars for all the user stats and add them to the layout
        # the staus bars are all in a horizontal layout
        self.status_bar = QGroupBox(self)
        self.status_bar.setFixedSize(700, 100)

        self.status_bar.move(0, 300)
        status_layout = QVBoxLayout(self.status_bar)
        for stat in self.person.get_status_report(): # get_status_report returns a list of lits (name, vlaue)

            stat_layout = QHBoxLayout()
            stat_layout.addWidget(QLabel(stat[0], self.status_bar))
            stat_layout.addWidget(QProgressBar(self.status_bar))
            stat_layout.itemAt(1).widget().setValue(stat[1])
            status_layout.addLayout(stat_layout)
        # status bar must always be at the top of the screen
        self.status_bar.move(0, 0)
        self.layout().addWidget(self.status_bar)
        score = self.person.get_score()
        if score > 80:
            self.alert("You have won the game!\nYour score is: " + str(score))
            return









    def update_inventory(self):
        if dir(self).count('inventory_grid') > 0:
            self.inventory_grid.deleteLater()
        self.inventory_grid = QWidget(self)
        self.inventory_grid.setFixedSize(500, 100)
        # must must be at the bottom of the screen
        self.inventory_grid.move(0, 400)
        # center it on the screen


        inventory_layout = QVBoxLayout(self.inventory_grid)
        self.inventory_label = QLabel("Inventory:", self.inventory_grid)
        inventory_layout.addWidget(self.inventory_label)
        for item in self.person.inventory:
            item_label = QLabel(item['name'], self.inventory_grid)
            inventory_layout.addWidget(item_label)
        self.layout().addWidget(self.inventory_grid)



    # method to move the person to a different room based on the direction
    def move_rooms(self, direction):
        """
        This method moves the person to a different room based on the direction.
        Arguments:
            direction (str): The direction to move the person in.
        """
        # north, south, east, west
        if direction in ["north", "south"]:
            self.person.location[1] = not (self.person.location[1] == 1)
        elif direction == "east":
            self.person.location[0] = (self.person.location[0] + 1) % 3
        elif direction == "west":
            self.person.location[0] = (self.person.location[0] - 1) % 3


    def alert(self, message):
        """
        This method displays an alert with a message.
        Arguments:
            message (str): The message to be displayed in the alert.
        """
        alert = QMessageBox(self)
        alert.setText(message)
        alert.exec_()


    def cover_open(self, room_object):
        if 'cover' in room_object.keys():
            # update the cover image
            self.cover_image.set_image(room_object['name'], room_object['cover'])
            self.cover_image.show()
        else:
            # if we don't have a cover image, hide the cover image window
            self.cover_image.hide_window()

    def get_room_object(self):
        return [room for room in ROOMS if room['name'] == self.person.get_location()][0]

    def on_input(self):
        """
        This method is called when the user presses enter in the input field of the window.
        Arguments:
            value (Gtk.Entry): The input field of the window.
        """
        # get the value of the input field
        value = self.input.text()


        self.input.setText("")
        self.history.append(value)
        value = value.lower().strip().split(" ")
        room_object = self.get_room_object()
        print(value)
        if value[0] == "go":
            self.move_rooms(value[1])
            # update position label
            # self.position_label.set_markup("<span font_desc='20'>You are in the " + self.person.get_location() + "</span>")
            # in pyqt:
            self.position_label.setText(f"You are in the {self.person.get_location()}")
            # show the cover image
            room_object = [room for room in ROOMS if room['name'] == self.person.get_location()][0]
            print(room_object)
            self.cover_open(room_object)


        elif value[0] == "drink":
            drinks_in_room = items_to(room_object['objects'], "action_name", "drink")
            if len(drinks_in_room) == 0:
                self.alert("There are no drinks in this room")
                return
            for drink in drinks_in_room:
                if value[1] == drink['name'].lower():
                    # remove item from room
                    room_object['objects'].remove(drink)
                    drink['action'](self.person)
                    self.update_status_bar()

        elif value[0] == "eat":
            food_in_room = items_to(room_object['objects'], "action_name", "eat")
            if len(food_in_room) == 0:
                self.alert("There is no food in this room")
                return
            for food in food_in_room:
                if value[1] == food['name'].lower():
                    # remove item from room
                    room_object['objects'].remove(food)
                    food['action'](self.person)
                    self.update_status_bar()

        elif value[:2] == ["pick", "up"]:

            items_in_room = items_to(room_object['objects'], "action_name", "pick up")
            if len(items_in_room) == 0:
                self.alert("There are no items in this room")
                return
            for item in items_in_room:
                print(item)
                # TODO check if item has not been picked up
                # add to user inventory
                if " ".join(value[2:]) == item['name'].lower():
                    self.person.grab(item)
                    # remove item from room
                    room_object['objects'].remove(item)
                    print(f"Item {item['name']} picked up")
                    # update inventory
                    self.update_inventory()
            pass
        elif value[0] == "look":
            actions_list = ""
            for action in room_object['objects']:
                actions_list += str(action['action_name'].lower()
                + " " + action['name'].lower()
                + "\n")
            description = f"{room_object['description']}\nIn this room you can...\n{actions_list}"
            if room_object['name'].lower() in PUZZLES.keys():
                description += f"\nThere is also a puzzle in this room."
                description += PUZZLES[room_object['name'].lower()]['teaser']
            # show a dialog box with the description
            dialog = QMessageBox(self)
            dialog.setText(description)
            dialog.exec_()


        elif value[0] == "play":
            roomPuzzleKey = room_object['name'].lower()
            if roomPuzzleKey in PUZZLES.keys():
                puzzle = PUZZLES[roomPuzzleKey]
                # check if puzzle.requirements are in the user inventory
                conditions = [req.lower() in [item['name'].lower() for item in self.person.inventory] for req in puzzle['requirements']]

                if all(conditions):
                    try:
                        puzzle.run()
                        puzzle['solved'](self.person)
                        self.update_status_bar()
                    except Exception as e:
                        print(e)

                else:
                    self.alert("You don't have the requirements to complete this puzzle")

        elif value[0] in ['exit', 'die', 'bye']:
            # some game over thing
            sys.exit(0)
        else:
            self.alert("I don't understand that command")
