class Schedule():
    def __init__(self, weeks):
        self.weeks = weeks

    def games_for_week(self, week_num):
        return self.weeks[week_num].games
