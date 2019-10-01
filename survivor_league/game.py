class Game:
    def __init__(self, *, team_1, team_2):
        self.team_1 = team_1
        self.team_2 = team_2

    def odds(self):
        elo_diff = self.team_1.elo - self.team_2.elo

        return self.team_1.name, 1.0 / (pow(10, (-elo_diff / 400.0)) + 1)
