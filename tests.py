import RiskAssessment as pages
from . import *
c = cu

class PlayerBot(Bot):
    def play_round(self):
        yield Decision, dict()