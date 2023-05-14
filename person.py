from game_configuration import ROOM_MATRIX
class Person():
    def __init__(self):
        # define the person's attributes at the start of the game
        self.health = 20
        self.knowledge = 20
        self.will_to_live = 20
        self.location = [2, 1]
        self.inventory = []

    def __increase__(self, actual, amount):
        if actual + amount > 100:
            return 100
        elif actual + amount < 0:
            return 0
        else:
            return actual + amount


    def increase(self, attribute, amount):
        # TODO make sure not to go over 100 or under 0
        if attribute == "health":
            self.health = self.__increase__(self.health, amount)
        elif attribute == "knowledge":
            self.knowledge = self.__increase__(self.knowledge, amount)
        elif attribute == "will_to_live":
            self.will_to_live = self.__increase__(self.will_to_live, amount)
        return self

    def get_status_report(self):
        # return a list of lists of the person's attributes
        return [
            ["Health", self.health],
            ["Knowledge", self.knowledge],
            ["Will to live", self.will_to_live]
        ]

    def grab(self, item):
        # add item to inventory
        self.inventory.append(item)
        return self

    def get_location(self):
        # get the room the person is in (text name)
        return ROOM_MATRIX[self.location[1]][self.location[0]]

    def get_score(self):
        # return average of attributes
        return (self.health + self.knowledge + self.will_to_live) / 3
