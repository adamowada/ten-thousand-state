from .state import State


class Quit(State):
    def handle_quit(self):
        print("# game switches state to Quit \n")
        print("OK. Maybe another time")
        exit()
