from puzzles import classroom_puzzle, kitchen_puzzle, gym_puzzle

coffee =  {'name': "Coffee", 'action': lambda person: person.increase('will_to_live', 20), 'action_name': 'drink'},

caf_and_kitchen = [
    {'name': "Snack", 'action': lambda person: person.increase('health', 15), 'action_name': 'eat'},
    {'name': "Water", 'action': lambda person: person.increase('health', 10), 'action_name': 'drink'},
    coffee
]

ROOMS = [
    {
        'name': "Kitchen",
        'action': lambda person: person,
        'cover': "kitchen.png",
        'objects': [
            {'name': "Pan", 'action_name': 'pick up'},
            *caf_and_kitchen,
            {'name': "Banana", 'action': lambda person: person.increase('health', 20), 'action_name': 'eat'},
            {'name': "Cookie", 'action': lambda person: person.increase('health', 20), 'action_name': 'eat'}
        ],
        'description': "You are in the kitchen. Here you recharge and enjoy some food."
    },
    {
        'name': "Cafeteria",
        'action': lambda person: person,
        'objects': [
            *caf_and_kitchen
        ],
        'description': "You are in the cafeteria, your favorite plane. Here you can enjoy some food and coffee and socialize (if you can)",
        'cover': 'cafeteria.png'

    },
    {
        'name': "Classroom",
        'action': lambda person: person.increase('knowledge', 10).increase('will_to_live', -5),
        'objects': [
            {'name': "Water", 'action': lambda person: person.increase('health', 10), 'action_name': 'drink'},
            coffee
        ],
        'cover': 'classroom.png',
        'task': {
            'name': "write code",
            'action': None
        },
        "description": "This is the CSAI classroom where the magic takes place. Its a bit smelly...\n"
    },
    {
        'name': "Library",
        'action': lambda person: person.increase('knowledge', 5),
        'cover': 'library.png',
        'objects': [
            coffee
        ],
        'description': "This is the library. Here you can study and get some work done."

    },
    {
        'name': "Gym",
        'action': lambda person: person.increase('health', 10).increase('will_to_live', 5),
        'description': "Lets get those gains!",
        'objects': [
            {'name': "Water", 'action': lambda person: person.increase('health', 10), 'action_name': 'drink'},
            {'name': "Protein", 'action': lambda person: person.increase('health', 20), 'action_name': 'drink'},
        ],
        'cover': 'gym.png'

    },
    {
        'name': "Bedroom",
        'action': lambda person: person.increase('will_to_live', 5).increase('health', 5),
        'objects': [
            {'name': "Phone", 'action_name': 'pick up'},
            {'name': "Laptop", 'action_name': 'pick up'},
            {'name': "Gym clothes", 'action_name': 'pick up'}
        ],
        'cover': 'bedroom.png',
        'description': "This is your bedroom. Here you can rest and relax and more ;)"
    },
    # Extra rooms:
]

ROOM_MATRIX = [
    [ 'Kitchen', "Cafeteria", "Classroom" ],
    [ "Bedroom", "Library", "Gym" ]
]


from challenges import pushup, capitals, debug, memory, rps

PUZZLES= {
        'classroom': {
            'requirements': ['laptop'],
            'puzzle': debug.classroom_puzzle,
            'teaser': "You will probably need to use your laptop and coffee to solve this puzzle."
        },
        'kitchen': {
            'requirements': ['pan'],
            'puzzle': rps.kitchen_puzzle,
            'teaser': "You will probably need to use your pan to solve this puzzle."
        },
        'gym': {
            'requirements': ['gym clothes'],
            'puzzle': pushup.gym_puzzle,
            'teaser': "You will probably need to use your gym clothes to solve this puzzle."
        }

    }
