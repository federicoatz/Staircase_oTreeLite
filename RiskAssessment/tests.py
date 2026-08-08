from . import *


class PlayerBot(Bot):
    def play_round(self):
        if self.round_number == 1:
            yield Instructions
        yield Decision, dict(choice='A')
