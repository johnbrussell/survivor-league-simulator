import random

from survivor_league import team, game, week, schedule


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
        self.num_byes = NUM_BYES
        self.num_weeks = NUM_WEEKS

    def generate_schedule(self):
        teams = self._generate_teams()
        return self._generate_schedule(teams)

    def _generate_teams(self):
        teams = list()

        for c in range(self.num_conferences):
            for d in range(self.num_divisions):
                for t in range(self.num_teams):
                    teams.append(team.Team(conference=c, division=d, name=f"{c}-{d}-{t}"))

        return teams

    def _generate_schedule(self, teams):
        weeks = list()
        for _ in range(self.num_weeks):
            weeks.append(self._generate_week(teams))

        return schedule.Schedule(weeks=weeks)

    def _generate_week(self, teams):
        non_bye_teams = self._filter_bye_teams(teams)

        home_teams = non_bye_teams[:int(len(non_bye_teams)/2)]
        away_teams = non_bye_teams[int(len(non_bye_teams)/2):]
        return week.Week(games=[game.Game(home_team=h, away_team=a) for h, a in zip(home_teams, away_teams)])

    def _filter_bye_teams(self, teams):
        non_bye_teams = [t for t in teams if not self._determine_bye_week()]
        if len(non_bye_teams) % 2 != 0:
            random.shuffle(non_bye_teams)
            non_bye_teams = non_bye_teams[1:]
        return non_bye_teams

    def _determine_bye_week(self):
        chance_of_bye = float(self.num_byes) / self.num_weeks

        return random.random() < chance_of_bye
