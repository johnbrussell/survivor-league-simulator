class Game:
    def __init__(self, *, home_team, away_team):
        self.home_team = home_team
        self.away_team = away_team

    def choose_winner(self, choice):
        if choice < self.home_team_win_probability():
            return self.home_team
        return self.away_team

    def favored_team(self):
        if self.home_team_win_probability() >= .5:
            return self.home_team
        return self.away_team

    def home_team_win_probability(self):
        elo_diff = self.home_team.elo - self.away_team.elo

        return 1.0 / (pow(10, (-elo_diff / 400.0)) + 1)

    def unfavored_team(self):
        if self.favored_team().name == self.home_team.name:
            return self.away_team
        return self.home_team
