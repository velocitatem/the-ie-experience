from game_configuration import ROOM_MATRIX
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