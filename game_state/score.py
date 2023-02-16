from .state import State
from game_logic import GameLogic
from .zilch import Zilch
from keep import Keep


class Score(State):
    def handle_score(self, dice):
        print("# game switches state to Score \n")

        if GameLogic.calculate_score(dice) == 0:
            self.game.change_state_to(Zilch())
            self.game.zilch()
            return

        self.game.change_state_to(Keep())
        self.game.keep()
