import random
from graphics import *

class RockPaperScissors:
    def __init__(self, win):
        self.win = win
        self.user_wins = 0
        self.comp_wins = 0
        self.rounds = 0
        self.outcomes = {
            "rock": {"win": "scissors", "lose": "paper"},
            "paper": {"win": "rock", "lose": "scissors"},
            "scissors": {"win": "paper", "lose": "rock"}
                        }

    def play(self, choice):
        self.rounds += 1
        comp_choice = random.choice(list(self.outcomes.keys()))

        user_choice_text = Text(Point(250, 200), "You chose: " + choice)
        user_choice_text.draw(self.win)

        comp_choice_text = Text(Point(250, 300), "Computer chose: " + comp_choice)
        comp_choice_text.draw(self.win)

        if self.outcomes[choice]["win"] == comp_choice:
            self.user_wins += 1
            result_text = Text(Point(250, 500), "You win!")
            result_text.draw(self.win)
        elif self.outcomes[choice]["lose"] == comp_choice:
            self.comp_wins += 1
            result_text = Text(Point(250, 500), "Computer wins!")
            result_text.draw(self.win)
        else:
            result_text = Text(Point(250, 500), "It's a tie!")
            result_text.draw(self.win)

        countdown_text = Text(Point(250, 600), "Next round starting in 3...")
        countdown_text.draw(self.win)

        for i in range(3, 0, -1):
            countdown_text.setText("Next round starting in " + str(i) + "...")
            time.sleep(1)

        user_choice_text.undraw()
        comp_choice_text.undraw()
        result_text.undraw()
        countdown_text.undraw()

    def run(self):
        while self.user_wins < 3 and self.comp_wins < 3:
            instructions_text = Text(Point(250, 50), "Choose rock, paper, or scissors:")
            instructions_text.draw(self.win)
            # draw the buttons
            rock_button = Rectangle(Point(150, 100), Point(350, 150))
            rock_button.draw(self.win)
            rock_text = Text(Point(250, 125), "Rock")
            rock_text.draw(self.win)

            paper_button = Rectangle(Point(150, 200), Point(350, 250))
            paper_button.draw(self.win)
            paper_text = Text(Point(250, 225), "Paper")
            paper_text.draw(self.win)

            scissors_button = Rectangle(Point(150, 300), Point(350, 350))
            scissors_button.draw(self.win)
            scissors_text = Text(Point(250, 325), "Scissors")
            scissors_text.draw(self.win)


            choice = None
            while choice not in self.outcomes:
                click = self.win.getMouse()
                if 150 <= click.getX() <= 350 and 100 <= click.getY() <= 150:
                    choice = "rock"
                elif 150 <= click.getX() <= 350 and 200 <= click.getY() <= 250:
                    choice = "paper"
                elif 150 <= click.getX() <= 350 and 300 <= click.getY() <= 350:
                    choice = "scissors"

            rock_button.undraw()
            rock_text.undraw()
            paper_button.undraw()
            paper_text.undraw()
            scissors_button.undraw()
            scissors_text.undraw()

            instructions_text.undraw()

            self.play(choice)


        outcome = False
        if self.user_wins >= 3:
            end_text = Text(Point(250, 350), "Congratulations, you won!")
            end_text.draw(self.win)
            outcome = True
        else:
            end_text = Text(Point(250, 350), "Sorry, you lost.")
            end_text.draw(self.win)

        time.sleep(3)
        end_text.undraw()
        self.win.close()
        return outcome

def kitchen_puzzle():
    win = GraphWin("Rock Paper Scissors", 500, 700)
    game = RockPaperScissors(win)
    return game.run()

def run():
    return kitchen_puzzle()

if __name__ == "__main__":
    print(run())
