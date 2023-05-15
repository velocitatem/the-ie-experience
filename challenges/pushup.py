# gym mini game

from graphics import*

class Button:
    # constructor
    def __init__(self, color, a, b, a2, b2, name, command=None):
        self.color = color
        self.a = a
        self.b = b
        self.a2 = a2
        self.b2 = b2
        self.name = name
        self.command = command
        self.active = True
        self.txt = None

    # appearance of the button (location + color)
    def appearance(self):
        rect = Rectangle(Point(self.a, self.b), Point(self.a2, self.b2))
        rect.setFill(self.color)
        rect.draw(win)
        self.txt = Text(Point((self.a + self.a2) / 2, (self.b + self.b2) / 2), self.name)
        self.txt.setFill("black")
        self.txt.draw(win)

    # active mode
    def activate(self):
        # Sets this button to 'active'.
        self.txt.setFill('black')
        self.active = True

    # inactive mode
    def deactivate(self):
        # Sets this button to 'inactive'.
        self.txt.setFill('grey')
        self.active = False

    # whether it has been clicked or not
    def clicked(self, p):
        # Returns true if button active and p is inside (note  p is a point)
        return (self.active and
                self.a <= p.getX() <= self.a2 and
                self.b <= p.getY() <= self.b2)


class GymBro:

    def __init__(self, hair, shirtcolor): #  def __init__(self, shirtcolor, hair, pantcolor):
        self.shirtcolor = shirtcolor
        self.hair = hair
        self.parts = []
        # self.pantcolor = pantcolor

    def down(self):
        # face
        face = Circle(Point(25, 55), radius=6)
        skin_color = color_rgb(255, 218, 185)
        face.setFill(skin_color)
        outline_color = color_rgb(150, 75, 0)
        face.setOutline(outline_color)
        face.draw(win)
        self.parts.append(face)
        nose = Circle(Point(25, 49), radius=1)
        nose.setFill(skin_color)
        nose.setOutline(outline_color)
        self.parts.append(nose)
        nose.draw(win)

        # hair
        hair = Polygon(Point(19, 49), Point(19, 61), Point(25, 61))
        hair.setFill("black")
        hair.draw(win)
        self.parts.append(hair)

        # neck
        neck = Rectangle(Point(31, 53), Point(33, 57))
        neck.setFill(skin_color)
        neck.setOutline(outline_color)
        neck.draw(win)
        self.parts.append(neck)

        # shirt
        shirt = Rectangle(Point(33, 49), Point(50, 60))
        shirt.setFill("lightblue")
        shirt.setOutline("darkblue")
        shirt.draw(win)
        self.parts.append(shirt)

        # ankle
        ankle = Rectangle(Point(75, 52), Point(77, 57))
        ankle.setFill(skin_color)
        ankle.setOutline(outline_color)
        ankle.draw(win)
        self.parts.append(ankle)

        # pant1
        pant1 = Rectangle(Point(50, 52), Point(75, 57))
        pant1.setFill("darkgrey")
        pant1.setOutline("black")
        pant1.draw(win)
        self.parts.append(pant1)

        # shoe
        shoe = Rectangle(Point(77, 43), Point(80, 57))
        shoe.setFill("black")
        shoe.setOutline("black")
        shoe.draw(win)
        self.parts.append(shoe)

        # arm
        arm1 = Polygon(Point(44, 48), Point(47, 50), Point(38, 57), Point(35, 54))
        arm1.setFill(skin_color)
        arm1.setOutline(outline_color)
        arm1.draw(win)
        self.parts.append(arm1)

        # arm 2
        arm2 = Polygon(Point(48, 49), Point(45, 52), Point(29, 43), Point(33, 43))
        arm2.setFill(skin_color)
        arm2.setOutline(outline_color)
        arm2.draw(win)
        self.parts.append(arm2)

        # hand
        line = Line(Point(33, 43), Point(33, 45.5))
        line.setOutline(outline_color)
        line.draw(win)
        self.parts.append(line)

    def up(self):
        # face
        face = Circle(Point(25, 60), radius=6)
        skin_color = color_rgb(255, 218, 185)
        face.setFill(skin_color)
        outline_color = color_rgb(150, 75, 0)
        face.setOutline(outline_color)
        face.draw(win)
        self.parts.append(face)
        nose = Circle(Point(25, 54), radius=1)
        nose.setFill(skin_color)
        nose.setOutline(outline_color)
        nose.draw(win)
        self.parts.append(nose)

        # hair
        hair = Polygon(Point(19, 54), Point(19, 66), Point(25, 66))
        hair.setFill(self.hair)
        hair.draw(win)
        self.parts.append(hair)

        # neck
        neck = Rectangle(Point(31, 58), Point(33, 62))
        neck.setFill(skin_color)
        neck.setOutline(outline_color)
        neck.draw(win)
        self.parts.append(neck)

        # shirt
        shirt = Rectangle(Point(33, 54), Point(50, 65))
        shirt.setFill(self.shirtcolor)
        shirt.setOutline("black")
        shirt.draw(win)
        self.parts.append(shirt)

        # ankle
        ankle = Rectangle(Point(75, 57), Point(77, 62))
        ankle.setFill(skin_color)
        ankle.setOutline(outline_color)
        ankle.draw(win)
        self.parts.append(ankle)

        # pant1
        pant1 = Rectangle(Point(50, 57), Point(75, 62))
        pant1.setFill("darkgrey")
        pant1.setOutline("black")
        pant1.draw(win)
        self.parts.append(pant1)

        # shoe
        shoe = Rectangle(Point(77, 48), Point(80, 62))
        shoe.setFill("black")
        shoe.setOutline("black")
        shoe.draw(win)
        self.parts.append(shoe)

        # hand
        hand = Polygon(Point(41, 45), Point(41, 48), Point(35, 45))
        hand.setFill(skin_color)
        hand.setOutline(outline_color)
        hand.draw(win)
        self.parts.append(hand)

        # arm 1
        arm2 = Rectangle(Point(38, 63), Point(41, 45))
        arm2.setFill(skin_color)
        arm2.setOutline(outline_color)
        arm2.draw(win)
        self.parts.append(arm2)



    def undraw(self):
        for part in self.parts:
            part.undraw()
        self.parts = []

import random
import time


def gym_puzzle():
    global win

    # draw the window
    win = GraphWin("Gym mini game", 500, 500) # default size is 400x400
    win.setBackground("grey")
    win.setCoords(0, 0, 100, 100)

    # draw the lifting button
    button = Button("white", 40, 10, 60, 20, "push-up")
    button.appearance() # drawing the button
    button.activate() # activating the button

    # gymbro
    gym_person = GymBro("black", "lightblue")
    gym_person.up()

    push_up_count = 0

    txt = Text(Point(50, 30), push_up_count)
    txt.setFill("white")
    txt.draw(win)

    title = "------ ** PUSH UP CHALLENGE ** ------"
    txt2 = Text(Point(50, 85),title)
    txt2.setSize(25)
    txt2.setFill("white")
    txt2.draw(win)


    while push_up_count < 10:
        p = win.getMouse()

        if button.clicked(p):
            gym_person.undraw()
            gym_person.down()
            time.sleep(0.5)
            gym_person.undraw()
            push_up_count += 1
            txt.setText(push_up_count)
            gym_person.up()
            button.deactivate()
            button.activate()

    button.name = "Quit"
    button.appearance()
    txt.setText("WORKOUT COMPLETED")
    txt.setSize(20)
    # run async:
    txt.setFill("white")
    win.getMouse()

    win.close()
    return True

def run():
    return gym_puzzle()


if __name__ == '__main__':
    print(gym_puzzle())
