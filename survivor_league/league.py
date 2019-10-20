import random

from survivor_league.strategies.choose_randomly import ChooseRandomly
from survivor_league import player


NUM_PLAYERS = 15
STRATEGIES = [ChooseRandomly]


class League:
    def __init__(self, schedule):
        self.PLAYERS = self._generate_players()
        self.SCHEDULE = schedule

    @staticmethod
    def _generate_players():
        return [player.Player(strategy=random.choice(STRATEGIES)) for _ in range(NUM_PLAYERS)]
