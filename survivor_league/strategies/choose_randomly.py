import random


class ChooseRandomly:
    def __init__(self):
        self.name = "Choose randomly"

    @staticmethod
    def rank_teams(games, ineligible_teams):
        eligible_home_teams = [game.home_team for game in games if game.home_team.name not in ineligible_teams]
        eligible_away_teams = [game.away_team for game in games if game.away_team.name not in ineligible_teams]
        eligible_teams = eligible_home_teams + eligible_away_teams

        random.shuffle(eligible_teams)

        return eligible_teams
