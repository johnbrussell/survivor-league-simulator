class Game:
    def __init__(self, *, home_team, away_team):
        self.home_team = home_team
        self.away_team = away_team

    def home_team_win_probability(self):
        elo_diff = self.home_team.elo - self.away_team.elo

        return 1.0 / (pow(10, (-elo_diff / 400.0)) + 1)
