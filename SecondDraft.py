# The IE Experience - A text-based adventure game
# Created by: India Antunez, Isabel de Valenzuela, Daniel Rosel, ...
# This is a game in which the player gets to experience the life of a student at IE University studying in Segovia. The player will have to make decisions that will affect the outcome of the game (and their life at IE University). As they progress through the game, they will be able to choose between different options that will lead them to different paths. The player will be able to interact with other characters and objects in the game. The game will end when the player has completed all the tasks and has reached the end of the game.
# Tasks: Sleeping, Eating, Studying, Socializing, Going to the Gym, Going to the Library
# Objects: Schedule, Phone, Coffee, Snack, Laptop, Water
# Status Bar: Health, Knowledge, Will to live
# Rooms: Kitchen, Walk to campus, Cafeteria, Classroom, Library, Gym, Bedroom
# The code must be modular !
import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


def when_enter(person):
    person.health -= 1

ROOMS = [
    {
        'name': "Kitchen",
        'action': lambda person: person.increase('health', 10)
    },
    {
        'name': "Cafeteria",
        'action': lambda person: person.increase('will_to_live', 5).increase('health', 5)
    },
    {
        'name': "Classroom",
        'action': lambda person: person.increase('knowledge', 10)
    },
    {
        'name': "Library",
        'action': lambda person: person.increase('knowledge', 5)
    },
    {
        'name': "Gym",
        'action': lambda person: person.increase('health', 10).increase('will_to_live', 5)
    },
    {
        'name': "Bedroom",
        'action': lambda person: person.increase('will_to_live', 5).increase('health', 5)
    }
]

ROOM_MATRIX = [
    [ 'Kitchen', "Cafeteria", "Classroom" ],
    [ "Bedroom", "Library", "Gym" ]
]

import random
import requests
class Person():
    def __init__(self):
        self.health = 20
        self.knowledge = 20
        self.will_to_live = 20
        self.location = [0, 0]

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
        self.image.set_opacity(0.6)
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





class GameWindow(Gtk.Window):
    def __init__(self):
        super().__init__(title="The IE Experience - Game")
        self.set_border_width(10)
        # set dimension of window 500 by 500
        self.set_default_size(500, 500)

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
        # add status bar to grid
        self.status_bar.set_halign(Gtk.Align.CENTER)
        self.status_bar.set_valign(Gtk.Align.CENTER)

        self.grid.attach(self.status_bar, 0, 0, 1, 1)
        self.grid.attach(self.status_bar, 0, 0, 1, 1)

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
            self.person.location[1] = not (self.person.location[1] == 0)
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

def main():
    win = GreetingWindow()
    win.connect("destroy", Gtk.main_quit)
    win.show_all()
    Gtk.main()

if __name__ == "__main__":
    main()
