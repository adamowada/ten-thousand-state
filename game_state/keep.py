from .state import State
from game_logic import GameLogic
from .quit import Quit


class Keep(State):
    def handle_keep(self):
        """
        Return values that user would like to keep after being validated
        Loops until user quits or follows the rules (aka keeps values that are valid)
        Args:
            roll: tuple of integers
        Returns:
            tuple of values to keep aka "keepers"
            empty tuple signals a "quit"
        """
        print("# game switches state to Keep \n")
        while True:
            print("Enter dice to keep, or (q)uit:")
            keep_or_quit = input("> ")

            if keep_or_quit == "q":
                self.game.change_state_to(Quit())
                self.game.quit()

            keepers = convert_keepers(keep_or_quit)

            if GameLogic.validate_keepers(roll, keepers):
                return keepers
            else:
                print("Cheater!!! Or possibly made a typo...")
                formatted_roll = format_roll(roll)
                print(formatted_roll)