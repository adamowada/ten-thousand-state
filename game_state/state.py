from abc import ABC


# Base state, aka interface
class State(ABC):
    @property
    def game(self):
        return self._game

    @game.setter
    def game(self, game):
        self._game = game
