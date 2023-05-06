
from puzzles import classroom_puzzle

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
            {'name': "Pan", 'action': lambda person: person.increase('health', 5), 'action_name': 'take'},
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
            'name': "write code",
            'action': classroom_puzzle,
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
    },
    # Extra rooms:
]

ROOM_MATRIX = [
    [ 'Kitchen', "Cafeteria", "Classroom" ],
    [ "Bedroom", "Library", "Gym" ]
]
