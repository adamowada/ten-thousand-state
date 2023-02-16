from .state import State
from .round import Round


class Zilch(State):
    def handle_zilch(self):
        """
        Display zilch message
        Returns:
            None
        """
        print("# game switches state to Zilch \n")
        print("****************************************")
        print("**        Zilch!!! Round over         **")
        print("****************************************")
        self.game.change_state_to(Round())
        self.game.round()
