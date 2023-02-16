from .state import State
from game_logic import GameLogic
from score import Score


class Roll(State):
    def handle_roll(self, num_dice):
        print("# game switches state to Roll \n")
        print(f"Rolling {num_dice} dice...")
        roll = GameLogic.roll_dice(num_dice)

        formatted_roll = self.format_roll(roll)

        print(formatted_roll)

        self.game.change_state_to(Score())
        self.game.score(roll)

    @ staticmethod
    def format_roll(roll):
        """
        converts given roll into display friendly string
        Args:
            roll: e.g. (5, 1, 1, 4, 5, 5)
        Returns:
            string: e.g. *** 5 1 1 4 5 5 ***
        """
        values_as_strings = [str(value) for value in roll]

        formatted_roll = " ".join(values_as_strings)

        return f"*** {formatted_roll} ***"
