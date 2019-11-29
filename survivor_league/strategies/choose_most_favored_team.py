class ChooseMostFavoredTeam:
    def __init__(self):
        self.name = "Choose most favored team"

    @staticmethod
    def rank_teams(games, ineligible_teams):
        games = sorted(games, key=lambda g: g.home_team_win_probability(), reverse=True)

        eligible_home_teams = [(game.home_team, game.home_team_win_probability()) for game in games
                               if game.home_team.name not in ineligible_teams]
        eligible_away_teams = [(game.away_team, 1 - game.home_team_win_probability()) for game in games
                               if game.away_team.name not in ineligible_teams]
        eligible_teams = eligible_home_teams + eligible_away_teams

        eligible_teams = [t[0] for t in
                          sorted(eligible_teams, key=lambda team_win_prob: team_win_prob[1], reverse=True)]

        return eligible_teams
