from .state import State
from .roll import Roll


class Round(State):
    def handle_round(self, round_num):
        print("# game switches state to Round \n")
        print(f"Starting round {round_num}")

        self.game.change_state_to(Roll())
        self.game.roll()
