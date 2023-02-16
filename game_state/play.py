from .state import State
from .round import Round
from .quit import Quit


class Play(State):
    def handle_play(self):
        print("# game switches state to Play \n")
        print("play the game")
        print("Welcome to Ten Thousand")
        choice = None
        while choice != "y" and choice != "n":
            print("(y)es to play or (n)o to decline")
            choice = input("> ")
            if choice == "y":
                self.game.change_state_to(Round())
                self.game.round()
            if choice == "n":
                self.game.change_state_to(Quit())
                self.game.quit()
