import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
import sys

# internal dependencies
from person import Person
from game_configuration import ROOMS, ROOM_MATRIX, PUZZLES
from helpers import items_to


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
        if self.image is not None:
            self.remove(self.image)
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
        # Create the window that will be used to display the cover image for each room
        self.cover_image = CoverImageWindow()

        # initialize the person Object for the game
        self.person = Person()
        self.history = ['look']

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
        def on_input_handler(event):
            try:
                self.on_input(event)
            except Exception as e:
                print(e)

        self.input.connect("activate", self.on_input)
        # on arrow key up pressed
        self.input.connect("key-press-event", self.on_key_press_event)


        self.paint_status_bar()
        # paint inventory
        self.paint_inventory()

        # show text for the position under the status bar
        self.position_label = Gtk.Label()
        self.position_label.set_markup("<span font_desc='20'>You are in the " + self.person.get_location() + "</span>")
        self.position_label.set_halign(Gtk.Align.CENTER)
        self.position_label.set_valign(Gtk.Align.CENTER)
        self.grid.attach(self.position_label, 0, 1, 1, 1)

        self.cover_open(self.get_room_object())

    def on_key_press_event(self, widget, event):
        if event.keyval == 65362:
            self.input.set_text(self.history[-1])



    def paint_status_bar(self):
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

    def update_status_bar(self):
        # remove status bar
        self.grid.remove(self.status_bar)
        # repaint status bar
        self.paint_status_bar()
        self.show_all()


    def paint_inventory(self):
        # create a horizontally scrollable grid on the bottom of the screen
        self.inventory_grid = Gtk.Grid()
        self.inventory_grid.set_size_request(500, 100)
        self.inventory_grid.set_halign(Gtk.Align.CENTER)
        self.inventory_grid.set_valign(Gtk.Align.CENTER)
        # add padding to inventory grid (left and right)
        self.inventory_grid.set_column_spacing(10)
        # add inventory grid to main grid
        self.grid.attach(self.inventory_grid, 0, 3, 1, 1)
        # padding top
        self.grid.set_row_spacing(100)


        # create a label for the inventory
        self.inventory_label = Gtk.Label()
        self.inventory_label.set_markup("<span font_desc='20'>Inventory:</span>")
        self.inventory_label.set_halign(Gtk.Align.CENTER)
        self.inventory_label.set_valign(Gtk.Align.CENTER)
        self.inventory_grid.attach(self.inventory_label, 0, 0, 1, 1)
        # add all the items in the inventory to the inventory grid
        for index, item in enumerate(self.person.inventory):
            self.inventory_item_label = Gtk.Label()
            self.inventory_item_label.set_markup("<span font_desc='10'>" + item['name'] + "</span>")
            self.inventory_item_label.set_halign(Gtk.Align.CENTER)
            self.inventory_item_label.set_valign(Gtk.Align.CENTER)
            self.inventory_grid.attach(self.inventory_item_label, index, 1, 1, 1)

    def update_inventory(self):
        """
        This method updates the inventory grid.
        """
        # remove the inventory grid
        self.grid.remove(self.inventory_grid)
        # repaint the inventory grid
        self.paint_inventory()
        # show all the widgets
        self.show_all()



    # method to move the person to a different room based on the direction
    def move_rooms(self, direction):
        """
        This method moves the person to a different room based on the direction.
        Arguments:
            direction (str): The direction to move the person in.
        """
        # north, south, east, west
        if direction in ["north", "south"]:
            self.person.location[1] = not (self.person.location[1] == 1)
        elif direction == "east":
            self.person.location[0] = (self.person.location[0] + 1) % 3
        elif direction == "west":
            self.person.location[0] = (self.person.location[0] - 1) % 3


    def alert(self, message):
        """
        This method displays an alert with a message.
        Arguments:
            message (str): The message to be displayed in the alert.
        """
        # create a dialog
        dialog = Gtk.MessageDialog(self, 0, Gtk.MessageType.INFO,
            Gtk.ButtonsType.OK, message)
        # run the dialog
        dialog.run()
        # destroy the dialog
        dialog.destroy()

    def cover_open(self, room_object):
        if 'cover' in room_object.keys():
            # update the cover image
            self.cover_image.set_image(room_object['name'], room_object['cover'])
            self.cover_image.show_all()
        else:
            # if we don't have a cover image, hide the cover image window
            self.cover_image.hide_window()

    def get_room_object(self):
        return [room for room in ROOMS if room['name'] == self.person.get_location()][0]

    def on_input(self, value):
        """
        This method is called when the user presses enter in the input field of the window.
        Arguments:
            value (Gtk.Entry): The input field of the window.
        """
        score = self.person.get_score()
        if score > 80:
            self.alert("You have won the game!\Your score is: " + str(score))
            return
        value = value.get_text()
        self.input.set_text("")
        self.history.append(value)
        value = value.lower().strip().split(" ")
        room_object = self.get_room_object()
        print(value)
        if value[0] == "go":
            self.move_rooms(value[1])
            # update position label
            self.position_label.set_markup("<span font_desc='20'>You are in the " + self.person.get_location() + "</span>")
            # show the cover image
            room_object = [room for room in ROOMS if room['name'] == self.person.get_location()][0]
            print(room_object)
            self.cover_open(room_object)


        elif value[0] == "drink":
            drinks_in_room = items_to(room_object['objects'], "action_name", "drink")
            if len(drinks_in_room) == 0:
                self.alert("There are no drinks in this room")
                return
            for drink in drinks_in_room:
                if value[1] == drink['name'].lower():
                    # remove item from room
                    room_object['objects'].remove(drink)
                    drink['action'](self.person)
                    self.update_status_bar()

        elif value[0] == "eat":
            food_in_room = items_to(room_object['objects'], "action_name", "eat")
            if len(food_in_room) == 0:
                self.alert("There is no food in this room")
                return
            for food in food_in_room:
                if value[1] == food['name'].lower():
                    # remove item from room
                    room_object['objects'].remove(food)
                    food['action'](self.person)
                    self.update_status_bar()

        elif value[:2] == ["pick", "up"]:

            items_in_room = items_to(room_object['objects'], "action_name", "pick up")
            if len(items_in_room) == 0:
                self.alert("There are no items in this room")
                return
            for item in items_in_room:
                print(item)
                # TODO check if item has not been picked up
                # add to user inventory
                if " ".join(value[2:]) == item['name'].lower():
                    self.person.grab(item)
                    # remove item from room
                    room_object['objects'].remove(item)
                    print(f"Item {item['name']} picked up")
                    # update inventory
                    self.update_inventory()
            pass
        elif value[0] == "look":
            actions_list = ""
            for action in room_object['objects']:
                actions_list += str(action['action_name'].lower()
                + " " + action['name'].lower()
                + "\n")
            description = f"{room_object['description']}\nIn this room you can...\n{actions_list}"
            if room_object['name'].lower() in PUZZLES.keys():
                description += f"\nThere is also a puzzle in this room."
            # show a dialog box with the description
            dialog = Gtk.MessageDialog(self, 0, Gtk.MessageType.INFO, Gtk.ButtonsType.OK, "Room Description")
            # add text to show what the user can do (puzzles)
            dialog.format_secondary_text(description)
            # run the dialog box
            dialog.run()
            dialog.destroy()

        elif value[0] == "play":
            roomPuzzleKey = room_object['name'].lower()
            if roomPuzzleKey in PUZZLES.keys():
                puzzle = PUZZLES[roomPuzzleKey]
                # check if puzzle.requirements are in the user inventory
                conditions = [req.lower() in [item['name'].lower() for item in self.person.inventory] for req in puzzle['requirements']]
                if all(conditions):
                    puzzle['puzzle']()
                    puzzle['solved'](self.person)
                    self.update_status_bar()
                else:
                    self.alert("You don't have the requirements to complete this puzzle")

        elif value[0] in ['exit', 'die', 'bye']:
            # some game over thing
            sys.exit(0)
        else:
            self.alert("I don't understand that command")
