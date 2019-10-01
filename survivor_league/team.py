DEFAULT_ELO = 1300


class Team:
    def __init__(self, *, elo=DEFAULT_ELO):
        self.elo = elo
