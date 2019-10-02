from survivor_league import team


NUM_CONFERENCES = 2
NUM_DIVISIONS_PER_CONFERENCE = 4
NUM_TEAMS_PER_DIVISION = 4
NUM_WEEKS = 17
NUM_BYES = 1


class ScheduleGenerator:
    def __init__(self):
        self.num_conferences = NUM_CONFERENCES
        self.num_divisions = NUM_DIVISIONS_PER_CONFERENCE
        self.num_teams = NUM_TEAMS_PER_DIVISION

    def generate_schedule(self):
        teams = self._generate_teams()

    def _generate_teams(self):
        teams = list()

        for c in range(self.num_conferences):
            for d in range(self.num_divisions):
                for t in range(self.num_teams):
                    teams.append(team.Team(conference=c, division=d, name=t))

        return teams
