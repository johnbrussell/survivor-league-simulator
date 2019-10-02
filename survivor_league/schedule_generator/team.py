class Team:
    def __init__(self, *, conference, division, number, div_home, div_away, alt_div_home, alt_div_away,
                 alt_conf_home, alt_conf_away, rand_home, rand_away):
        self.conference = conference
        self.division = division
        self.name = number
        self.remaining_home_division = div_home
        self.remaining_away_division = div_away
        self.remaining_home_alt_division = alt_div_home
        self.remaining_away_alt_division = alt_div_away
        self.remaining_home_alt_conf = alt_conf_home
        self.remaining_away_alt_conf = alt_conf_away
        self.remaining_random_home = rand_home
        self.remaining_random_away = rand_away
        self.schedule = dict()
