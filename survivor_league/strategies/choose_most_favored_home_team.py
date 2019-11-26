import random


class ChooseMostFavoredHomeTeam:
    def __init__(self):
        self.name = "Choose most favored home team"

    @staticmethod
    def rank_teams(games, ineligible_teams):
        eligible_home_teams = [game.home_team for game in games if game.home_team.name not in ineligible_teams]
        eligible_away_teams = [game.away_team for game in games if game.away_team.name not in ineligible_teams]

        favored_home_teams = [g.favored_team() for g in games if g.favored_team() in eligible_home_teams]
        unfavored_home_teams = [g.unfavored_team() for g in games if g.unfavored_team() in eligible_home_teams]
        favored_away_teams = [g.favored_team() for g in games if g.favored_team() in eligible_away_teams]
        unfavored_away_teams = [g.unfavored_team() for g in games if g.unfavored_team() in eligible_away_teams]

        favored_home_teams = sorted(favored_home_teams, key=lambda x: x.elo, reverse=True)
        unfavored_home_teams = sorted(unfavored_home_teams, key=lambda x: x.elo, reverse=True)
        favored_away_teams = sorted(favored_away_teams, key=lambda x: x.elo, reverse=True)
        unfavored_away_teams = sorted(unfavored_away_teams, key=lambda x: x.elo, reverse=True)

        return favored_home_teams + favored_away_teams + unfavored_home_teams + unfavored_away_teams
