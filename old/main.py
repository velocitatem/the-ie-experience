# The IE Experience - A text-based adventure game
# Created by: India Antunez, Isabel de Valenzuela, Daniel Rosel, ...
# This is a game in which the player gets to experience the life of a student at IE University studying in Segovia. The player will have to make decisions that will affect the outcome of the game (and their life at IE University). As they progress through the game, they will be able to choose between different options that will lead them to different paths. The player will be able to interact with other characters and objects in the game. The game will end when the player has completed all the tasks and has reached the end of the game.
# Tasks: Sleeping, Eating, Studying, Socializing, Going to the Gym, Going to the Library
# Objects: Schedule, Phone, Coffee, Snack, Laptop, Water
# Status Bar: Health, Knowledge, Will to live
# Rooms: Kitchen, Walk to campus, Cafeteria, Classroom, Library, Gym, Bedroom
# The code must be modular !
# Importing all the necessary modules

import time
import random
import sys
import os
import curses
from curses import wrapper

stdscr = curses.initscr() # create a new screen
curses.noecho()
curses.cbreak()

# Defining the backpack class
class Backpack:
    def __init__(self):
        self.items = []

    def __str__(self):
        return f"Backpack: {self.items}"

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)

# Defining a Player
class Player:
    def __init__(self, name, health, knowledge, will_to_live, hunger):
        self.name = name
        self.health = health
        self.knowledge = knowledge
        self.hunger = hunger
        self.will_to_live = will_to_live
        self.current_room = None
        self.backpack = Backpack()

    def __str__(self):
        return f"Name: {self.name}"

    def get_status(self):
        return {
            "health": self.health,
            "Knowledge ": self.knowledge,
            "will_to_live": self.will_to_live,
            "hunger": self.hunger,
            "current_room": self.current_room
        }
    
    # Defining basic functionalities of player
    
    # Each of the following must also check if the player is in the correct room
    # Also must handle cases where the player does not have the item in their backpack
    # Also must handle cases if status is full
    
    def check_status_range(self, status):
        if status < 0:
            return 0
        elif status > 100:
            return 100
        else:
            return status

    def eat(self, food):
        # TODO - decrease hunger
        pass                            # pass is a placeholder for code that has npt yet been implemented

    def drink(self, drink):
        # TODO - decrease thirst
        pass

    def sleep(self):
        # TODO - increase health, increase will to live
        pass

    def study(self):
        # TODO - increase knowledge, decrease will to live
        pass

    def socialize(self):
        # TODO - increase will to live, decrease knowledge
        self.will_to_live = self.check_status_range(self.will_to_live + 10)
        self.knowledge = self.check_status_range(self.knowledge - 10)
        return self

    def go_to_gym(self):
        # TODO - increase health, increase will to live, decrease knowledge
        pass

    def go_to_library(self):
        # TODO - increase knowledge, decrease will to live
        pass

    def go_to_cafeteria(self):
        # TODO - decrease hunger, increase will to live
        pass
    

# Defining possible input commands
def eval_command(command, player):
    command_map = {
        "eat": player.eat,
        "drink": player.drink,
        "sleep": player.sleep,
        "study": player.study,
        "socialize": player.socialize
    }
    if command in command_map.keys():
        player=command_map[command]()
        return (player)
    else:
        return (player, "Invalid command")
    
# Clearing the status bar (graphically?)
def update_status_bar(player, scr):
    for i in range(20):
        scr.addstr(i, 0, " " * 100)
    for i, key in enumerate(player.get_status().keys()):
        scr.addstr(i, 0, f"{key}: {player.get_status()[key]}")

# Typing the input 
def get_input_string(scr):
    curses.echo()
    curses.curs_set(1)
    user_input = scr.getstr(20, 7, 100)
    curses.noecho()
    curses.curs_set(0)
    return str(user_input, "utf-8")




# Bedroom - Kitchen - Gym
#              |
#         Walk to campus
#              |
#           Classroom - Library
#              |
#          Cafeteria
# that is the general layout of the game


# Drawing the map (visual rep)
def draw_map(player, scr):
    # draw a 2D map of the rooms
    # the player is in the middle
    # create a square to represent the current room
    # create a line to represent the path to the next room
    # create a square to represent the next room
    rooms_matrix = [
        ["Bedroom", "Kitchen", "Gym"],
        ["", "Walk to campus", ""],
        ["", "Classroom", "Library"],
        ["", "Cafeteria", ""]
    ]
    # map is in the top right corner
    # clear the map
    for i in range(20):
        scr.addstr(i, 50, " " * 100)
    for i, row in enumerate(rooms_matrix):
        for j, room in enumerate(row):
            if room == player.current_room:
                scr.addstr(i, 50 + j * 10, f"[{room}]")
            else:
                scr.addstr(i, 50 + j * 10, f" {room} ")

def main(stdscr):
    stdscr.clear()

    # Print welcome message
    stdscr.addstr(0, 0, "Welcome to The IE Experience!")
    stdscr.addstr(1, 0, "Press any key to continue...")
    stdscr.refresh()

    # Wait for user input
    stdscr.getch()

    # Print instructions
    stdscr.addstr(0, 0, "Instructions:")
    stdscr.addstr(1, 0, "You are a student at IE University in Segovia. You have to make decisions that will affect the outcome of the game (and your life at IE University). As you progress through the game, you will be able to choose between different options that will lead you to different paths. You will be able to interact with other characters and objects in the game. The game will end when you have completed all the tasks and have reached the end of the game.")

    # create the player
    player = Player("Peter", 50, 50, 50, 50)

    rooms = ["Kitchen", "Walk to campus", "Cafeteria", "Classroom", "Library", "Gym", "Bedroom"]
    player.current_room = random.choice(rooms) 

    # create the items
    items = ["Schedule", "Phone", "Coffee", "Snack", "Laptop", "Water"]
    [player.backpack.add_item(item) for item in items]

    # print the initial status bar
    update_status_bar(player, stdscr)
    # draw_map(player, stdscr)

    # add input box at the bottom of the screen
    stdscr.addstr(20, 0, "Input: ") # add the input box
    stdscr.refresh()

    # begin game loop
    while True:
        # get char until enter is pressed
        user_input = get_input_string(stdscr)
        stdscr.clear()

        if "exit" in user_input:
            sys.exit()
        else:
            player = eval_command(user_input, player)
            if type(player) == tuple:
                stdscr.addstr(21, 0, player[1])
                stdscr.refresh()
                player = player[0]
            update_status_bar(player, stdscr)
            stdscr.addstr(20, 0, "Input: ") # add the input box
            stdscr.refresh()

    curses.nocbreak()
    stdscr.keypad(False)
    curses.echo()
    curses.endwin()

wrapper(main)
