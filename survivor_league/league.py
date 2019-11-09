import random

from survivor_league.strategies.choose_randomly import ChooseRandomly
from survivor_league import player


NUM_PLAYERS = 15
STRATEGIES = [ChooseRandomly]


class League:
    def __init__(self, schedule):
        self.PLAYERS = self._generate_players()
        self.SCHEDULE = schedule

    def simulate_season(self):
        for week in self.SCHEDULE.weeks:
            if self._num_active_players() <= 1:
                continue

            self._simulate_week(week)

    def _active_players(self):
        return [p for p in self.PLAYERS if p.is_alive()]

    def _choose_teams(self, games):
        player_choices = dict()

        for p in self._active_players():
            player_choices[p.name()] = p.choose_team(games)

        return player_choices

    @staticmethod
    def _determine_game_winners(games):
        winners_names = list()

        for game in games:
            choice = random.random()
            winners_names.append(game.choose_winner(choice).name)

        return winners_names

    def _eliminate_losers(self, player_choices, winning_team_names, week_num):
        # this is tricky; it relies on list mutability by using the fact that self._active_players is a subset of
        #  the actual Players in self.PLAYERS, not copies
        for p in self._active_players():
            if player_choices[p.name()] not in winning_team_names:
                p.eliminate(week_num)

    @staticmethod
    def _generate_players():
        return [player.Player(name=p, strategy=random.choice(STRATEGIES)) for p in range(NUM_PLAYERS)]

    def _num_active_players(self):
        return len(self._active_players())

    def _simulate_week(self, week):
        games = self.SCHEDULE.games_for_week(week.number)

        player_choices = self._choose_teams(games)

        game_winners = self._determine_game_winners(games)

        self._eliminate_losers(player_choices, game_winners, week.number)
