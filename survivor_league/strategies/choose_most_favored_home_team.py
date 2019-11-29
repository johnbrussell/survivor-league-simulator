import random


class ChooseMostFavoredHomeTeam:
    def __init__(self):
        self.name = "Choose most favored home team"

    @staticmethod
    def rank_teams(games, ineligible_teams):
        eligible_home_teams = [(game.home_team, game.home_team_win_probability()) for game in games
                               if game.home_team.name not in ineligible_teams]
        eligible_away_teams = [(game.away_team, 1 - game.home_team_win_probability()) for game in games
                               if game.away_team.name not in ineligible_teams]

        favored_home_teams = [t for t in eligible_home_teams if t[1] >= 0.5]
        unfavored_home_teams = [t for t in eligible_home_teams if t[1] < 0.5]
        favored_away_teams = [t for t in eligible_away_teams if t[1] >= 0.5]
        unfavored_away_teams = [t for t in eligible_away_teams if t[1] < 0.5]

        favored_home_teams = sorted(favored_home_teams, key=lambda x: x[1], reverse=True)
        unfavored_home_teams = sorted(unfavored_home_teams, key=lambda x: x[1], reverse=True)
        favored_away_teams = sorted(favored_away_teams, key=lambda x: x[1], reverse=True)
        unfavored_away_teams = sorted(unfavored_away_teams, key=lambda x: x[1], reverse=True)

        teams = [t[0] for t in favored_home_teams] + [t[0] for t in favored_away_teams] + \
            [t[0] for t in unfavored_home_teams] + [t[0] for t in unfavored_away_teams]

        return teams
