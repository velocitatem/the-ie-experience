import random
import requests
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
# The IE Experience - A text-based adventure game
# Created by: India Antunez, Isabel de Valenzuela, Daniel Rosel, ...
# This is a game in which the player gets to experience the life of a student at IE University studying in Segovia. The player will have to make decisions that will affect the outcome of the game (and their life at IE University). As they progress through the game, they will be able to choose between different options that will lead them to different paths. The player will be able to interact with other characters and objects in the game. The game will end when the player has completed all the tasks and has reached the end of the game.
# Tasks: Sleeping, Eating, Studying, Socializing, Going to the Gym, Going to the Library
# Objects: Schedule, Phone, Coffee, Snack, Laptop, Water
# Status Bar: Health, Knowledge, Will to live
# Rooms: Kitchen, Walk to campus, Cafeteria, Classroom, Library, Gym, Bedroom
# The code must be modular !



def when_enter(person):
    person.health -= 1

caf_and_kitchen = [
    {'name': "Snack", 'action': lambda person: person.increase('health', 5), 'action_name': 'eat'},
    {'name': "Water", 'action': lambda person: person.increase('health', 5), 'action_name': 'drink'},
    {'name': "Coffee", 'action': lambda person: person.increase('will_to_live', 5), 'action_name': 'drink'},
]

ROOMS = [
    {
        'name': "Kitchen",
        'action': lambda person: person,
        'cover': "kitchen.png",
        'objects': [
            {'name': "Pan", 'action': lambda person: person.increase('health', 5), 'action_name': 'use'},
            *caf_and_kitchen
        ],
        'description': "You are in the kitchen. Here you recharge and enjoy some food."
    },
    {
        'name': "Cafeteria",
        'action': lambda person: person,
        'objects': [
            {'name': "Coffee", 'action': lambda person: person.increase('will_to_live', 5), 'action_name': 'drink'},
            *caf_and_kitchen
        ],
        'description': "You are in the cafeteria, your favorite plane. Here you can enjoy some food and coffee and socialize (if you can)",
        'cover': 'cafeteria.png'

    },
    {
        'name': "Classroom",
        'action': lambda person: person.increase('knowledge', 10).increase('will_to_live', -5),
        'objects': [
            {'name': "Laptop", 'action': lambda person: person.increase('knowledge', 5), 'action_name': 'use'},
            {'name': "Water", 'action': lambda person: person.increase('health', 5), 'action_name': 'drink'}
        ],
        'cover': 'classroom.png',
        'task': {
            'name': "Write code"
        },
        "description": "This is the CSAI classroom where the magic takes place. Its a bit smelly...\n"
    },
    {
        'name': "Library",
        'action': lambda person: person.increase('knowledge', 5),
        'cover': 'library.png',
        'description': "This is the library. Here you can study and get some work done."

    },
    {
        'name': "Gym",
        'action': lambda person: person.increase('health', 10).increase('will_to_live', 5),
        'description': "Lets get those gains!",
        'cover': 'gym.png'

    },
    {
        'name': "Bedroom",
        'action': lambda person: person.increase('will_to_live', 5).increase('health', 5),
        'objects': [
            {'name': "Phone", 'action': lambda person: person.grab(), 'action_name': 'pick up'},
            {'name': "Laptop", 'action': lambda person: person.increase('knowledge', 5), 'action_name': 'pick up'}
        ],
        'cover': 'bedroom.png',
        'description': "This is your bedroom. Here you can rest and relax and more ;)"
    }
]

ROOM_MATRIX = [
    [ 'Kitchen', "Cafeteria", "Classroom" ],
    [ "Bedroom", "Library", "Gym" ]
]


class Person():
    def __init__(self):
        self.health = 20
        self.knowledge = 20
        self.will_to_live = 20
        self.location = [0, 0]
        self.inventory = []

    def increase(self, attribute, amount):
        # TODO make sure not to go over 100 or under 0
        if attribute == "health":
            self.health += amount
        elif attribute == "knowledge":
            self.knowledge += amount
        elif attribute == "will_to_live":
            self.will_to_live += amount
        return self

    def get_status_report(self):
        return [
            ["Health", self.health],
            ["Knowledge", self.knowledge],
            ["Will to live", self.will_to_live]
        ]

    def grab(self, item):
        self.inventory.append(item)
        return self

    def get_location(self):
        return ROOM_MATRIX[self.location[1]][self.location[0]]


class GreetingWindow(Gtk.Window):
    def __init__(self):
        super().__init__(title="The IE Experience")
        self.set_border_width(10)
        # set dimension of window 500 by 500
        self.set_default_size(500, 700)

        # set background image of window
        self.image = Gtk.Image()
        self.image.set_from_file("IE.png")
        # crop image to 500 by 500
        self.image.set_pixel_size(500)
        # set image opactity to 0.6
        # make new grid
        self.grid = Gtk.Grid()
        # add image to grid at top
        self.grid.attach(self.image, 0, 0, 1, 1)

        # add a label and button to start the game - font size 20 padding top and bottom 10
        self.label = Gtk.Label()
        self.label.set_size_request(500, 100)
        self.label.set_margin_top(10)
        self.label.set_margin_bottom(10)
        self.label.set_markup("<span font_desc='20'>Welcome to the IE Experience!\nPress the button to start the game.</span>")

        self.button = Gtk.Button(label="Start Game")
        self.button.connect("clicked", self.start_game)
        # set button size to 100 by 50
        self.button.set_size_request(100, 50)
        # TODO set button color via css
        # hex: 00338d

        # horizontal center the label and button
        self.label.set_halign(Gtk.Align.CENTER)
        self.button.set_halign(Gtk.Align.CENTER)

        # add label and button to grid
        self.grid.attach(self.label, 0, 500, 1, 1)
        self.grid.attach(self.button, 0, 501, 1, 1)
        # add grid to window
        self.add(self.grid)

    def start_game(self, button):
        # close the greeting window
        self.destroy()
        # open the game window
        self.game = GameWindow()
        self.game.connect("destroy", Gtk.main_quit)
        self.game.show_all()
        Gtk.main()

class CoverImageWindow(Gtk.Window):
    def __init__(self):
        super().__init__(title="The IE Experience")
        self.set_border_width(0)
        self.image = None

    def set_image(self, name, file):
        # if we already have a cover image, remove it
        if self.image:
            self.remove(self.cover_image)
        self.image = Gtk.Image()
        self.image.set_from_file(file)
        self.add(self.image)
        self.show_all()
        # show window after we set the image
        self.show()

    def hide_window(self):
        self.hide()

    def close(self):
        self.destroy()

class GameWindow(Gtk.Window):
    def __init__(self):
        super().__init__(title="The IE Experience - Game")
        self.set_border_width(10)
        # set dimension of window 500 by 500
        self.set_default_size(700, 500)
        self.cover_image = CoverImageWindow()

        self.person = Person()

        # we add the input to the bottom of the window
        # we add 5 columns of labels to the top (status bar) [health, knowledge, will to live, time, location]

        # make new grid
        self.grid = Gtk.Grid()
        # add grid to window
        self.add(self.grid)

        # set input
        self.input = Gtk.Entry()
        self.input.set_size_request(500, 50)
        self.input.set_placeholder_text("Enter your command here")
        # position input at bottom of window
        self.input.set_halign(Gtk.Align.CENTER)
        # add input to grid
        self.grid.attach(self.input, 0, 2, 1, 1)

        # input handler
        self.input.connect("activate", self.on_input)

        # set status bar
        self.status_bar = Gtk.Grid()
        self.status_bar.set_size_request(500, 100)
        # crate progress bars for health, knowledge, will to live
        for index, status in enumerate(self.person.get_status_report()):
            status_name = status[0]
            status_value = status[1]
            # create label for status name
            self.status_name_label = Gtk.Label()
            self.status_name_label.set_markup("<span font_desc='20'>" + status_name + "</span>")
            # create progress bar for status value
            self.status_value_progress_bar = Gtk.ProgressBar()
            self.status_value_progress_bar.set_fraction(status_value / 100)
            # add label and progress bar to status bar
            self.status_bar.attach(self.status_name_label, index, 0, 1, 1)
            self.status_bar.attach(self.status_value_progress_bar, index, 1, 1, 1)
            # add padding to status bar (left and right)
            self.status_bar.set_column_spacing(10)


        # add status bar to grid
        self.status_bar.set_halign(Gtk.Align.CENTER)
        self.status_bar.set_valign(Gtk.Align.CENTER)

        self.grid.attach(self.status_bar, 0, 0, 1, 1)
        self.grid.set_halign(Gtk.Align.CENTER)

        # show text for the position under the status bar
        self.position_label = Gtk.Label()
        self.position_label.set_markup("<span font_desc='20'>You are in the " + self.person.get_location() + "</span>")
        self.position_label.set_halign(Gtk.Align.CENTER)
        self.position_label.set_valign(Gtk.Align.CENTER)
        self.grid.attach(self.position_label, 0, 1, 1, 1)



    def move_rooms(self, direction):
        # north, south, east, west
        if direction == "north":
            self.person.location[1] = not (self.person.location[1] == 1)
        elif direction == "south":
            self.person.location[1] = not (self.person.location[1] == 1)
        elif direction == "east":
            self.person.location[0] = (self.person.location[0] + 1) % 3
        elif direction == "west":
            self.person.location[0] = (self.person.location[0] - 1) % 3

    def on_input(self, value):
        value = value.get_text()
        value = value.lower().strip().split(" ")
        if value[0] == "go":
            self.move_rooms(value[1])
            # update position label
            self.position_label.set_markup("<span font_desc='20'>You are in the " + self.person.get_location() + "</span>")
            # show the cover image
            room_object = [room for room in ROOMS if room['name'] == self.person.get_location()][0]
            print(room_object)

            if 'cover' in room_object.keys():
                self.cover_image.set_image(room_object['name'], room_object['cover'])
                self.cover_image.show_all()
            else:
                self.cover_image.hide_window()

        elif value[0] == "drink":
            pass
        elif value[0] == "eat":
            pass
        elif value[0] == "use":
            pass
        elif value[:1] == ["pick", "up"]:
            pass
        elif value[0] == "look":
            room_object = [room for room in ROOMS if room['name'] == self.person.get_location()][0]
            actions_list = ""
            for action in room_object['objects']:
                actions_list += str(action['action_name'].lower()
                + " " + action['name'].lower()
                + "\n")

            description = f"{room_object['description']}\nIn this room you can...\n{actions_list}"
            # show a dialog box with the description
            dialog = Gtk.MessageDialog(self, 0, Gtk.MessageType.INFO, Gtk.ButtonsType.OK, "Room Description")
            dialog.format_secondary_text(description)
            dialog.run()
            dialog.destroy()





def main():
    win = GreetingWindow()
    win.connect("destroy", Gtk.main_quit)
    win.show_all()
    Gtk.main()

if __name__ == "__main__":
    main()
