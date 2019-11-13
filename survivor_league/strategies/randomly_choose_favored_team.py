import random


class RandomlyChooseFavoredTeam:
    def __init__(self):
        self.name = "Randomly choose favored team"

    @staticmethod
    def rank_teams(games, ineligible_teams):
        eligible_home_team_names = [game.home_team.name for game in games if
                                    game.home_team.name not in ineligible_teams]
        eligible_away_team_names = [game.away_team.name for game in games if
                                    game.away_team.name not in ineligible_teams]
        eligible_team_names = eligible_home_team_names + eligible_away_team_names

        favored_teams = [g.favored_team() for g in games if g.favored_team().name in eligible_team_names]
        unfavored_teams = [g.unfavored_team() for g in games if g.unfavored_team().name in eligible_team_names]

        random.shuffle(favored_teams)
        random.shuffle(unfavored_teams)

        return favored_teams + unfavored_teams
