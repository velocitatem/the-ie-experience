
# TODO more puzzles

def kitchen_puzzle():
    pass


def puzzles():
    return {
        'classroom': {
            'requirements': ['laptop', 'coffee'],
            'puzzle': classroom_puzzle
        },
        'kitchen': {
            'requirements': ['pan'],
            'puzzle': kitchen_puzzle
        }

    }

def run_puzzle(puzzle_name, person):
    puzzle_object = puzzles()[puzzle_name]
    if person.has_items(puzzle_object['requirements']):
        puzzle_object['puzzle']()
