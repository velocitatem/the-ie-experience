# The IE Experience - A text-based adventure game
# Created by: Daniel Rosel, ...
# This is a game in which the player gets to experience the life of a student at IE University studying in Segovia. The player will have to make decisions that will affect the outcome of the game (and their life at IE University). As they progress through the game, they will be able to choose between different options that will lead them to different paths. The player will be able to interact with other characters and objects in the game. The game will end when the player has completed all the tasks and has reached the end of the game.
# Tasks: Sleeping, Eating, Studying, Socializing, Going to the Gym, Going to the Library
# Characters: Professor, Student, Friend, Stranger
# Objects: Food, Drink, Book, Exercise Equipment, Computer
# Status Bar: Health, Energy, Hunger, Thirst, Happiness, Knowledge, Money

# Importing all the necessary modules
import time
import random
import sys

# Defining the variables
health, energy, hunger, thirst, happiness, knowledge, money = 100, 100, 100, 100, 100, 0, 0 # Status Bar Variables
player_name = "" # Player Name
player_age = 0 # Player Age

# Defining the functions
def start_game(): # Function that starts the game
    print("Welcome to The IE Experience!")
    print("This is a game in which you get to experience the life of a student at IE University studying in Segovia.")
    print("You will have to make decisions that will affect the outcome of the game (and your life at IE University).")

def player_name_age(): # Function that asks the player for their name and age
    global player_name
    global player_age
    player_name = input("What is your name? ")
    player_age = int(input("How old are you? "))
    print("Hello, " + player_name + "! You are " + str(player_age) + " years old.")

def player_status_bar(): # Function that displays the player's status bar
    print(f"\tHealth: {health}\n\tEnergy: {energy}\n\tHunger: {hunger}\n\tThirst: {thirst}\n\tHappiness: {happiness}\n\tKnowledge: {knowledge}\n\tMoney: {money}")

def player_sleep(): # Function that allows the player to sleep
    global energy
    global hunger
    global thirst
    global happiness
    global knowledge
    global money
    print("You are going to sleep.")
    # ask how many hours the player wants to sleep
    # if the player sleeps for 8 hours, then the player's energy will be 100

def player_eat(): # Function that allows the player to eat
    global energy
    global hunger
    global thirst
    global happiness

def player_study(): # Function that allows the player to study
    global energy
    global knowledge

def player_socialize(): # Function that allows the player to socialize
    global energy
    global happiness

def player_gym(): # Function that allows the player to go to the gym
    global energy
    global happiness

def player_library(): # Function that allows the player to go to the library
    global energy
    global knowledge

def player_tasks(): # Function that allows the player to choose what they want to do
    print("What would you like to do?")
    options = ["Sleep", "Eat", "Study", "Socialize", "Go to the Gym", "Go to the Library"]
    for i in range(len(options)):
        print(f"{i + 1}. {options[i]}")
    choice = int(input("Enter the number of the option you want to choose: "))
    methods = [player_sleep, player_eat, player_study, player_socialize, player_gym, player_library]
    methods[choice - 1]()

if __name__ == "__main__":
    start_game()
    player_name_age()
    player_status_bar()
    while True:
        player_tasks()
