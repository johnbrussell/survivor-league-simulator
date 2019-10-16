DEFAULT_ELO = 1300


class Team:
    def __init__(self, *, elo=DEFAULT_ELO, name, conference, division):
        self.elo = elo
        self.name = name
        self.conference = conference
        self.division = division
