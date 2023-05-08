
def classroom_puzzle():
    pass

def kitchen_puzzle():
    pass

def gym_puzzle():
    pass

from game_configuration import PUZZLES

def run_puzzle(puzzle_name, person):
    puzzle_object = PUZZLES[puzzle_name]
    if person.has_items(puzzle_object['requirements']):
        puzzle_object['puzzle']()
