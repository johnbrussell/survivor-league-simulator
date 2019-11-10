class Schedule():
    def __init__(self, weeks):
        self.weeks = weeks

    def games_for_week(self, week_num):
        valid_weeks = [w for w in self.weeks if w.number == week_num]
        return valid_weeks[0].games

    def num_weeks(self):
        return len(self.weeks)
