from game_state.play import Play

"""
Context that will use the states
"""


class Game:
    # The game knows about the current concrete state
    _state = None

    def __init__(self):
        self.round_num = 1
        self.change_state_to(Play())
        self.play()

    def change_state_to(self, state):
        self._state = state
        # Concrete state knows about game instance
        self._state.game = self

    def play(self):
        self._state.handle_play()

    def roll(self):
        self._state.handle_roll()

    def round(self):
        self._state.handle_round(self.round_num)

    def quit(self):
        self._state.handle_quit()

    def keep(self):
        self._state.handle_keep()
