import unittest

from survivor_league import schedule_generator
from survivor_league.schedule_generator import NUM_CONFERENCES, NUM_TEAMS_PER_DIVISION, NUM_DIVISIONS_PER_CONFERENCE, \
    NUM_WEEKS, NUM_BYES


class TestScheduleGenerator(unittest.TestCase):
    def test__generate_teams_returns_correct_number_of_teams(self):
        subject = schedule_generator.ScheduleGenerator()

        teams = subject._generate_teams()

        expected_num_teams = NUM_CONFERENCES * NUM_DIVISIONS_PER_CONFERENCE * NUM_TEAMS_PER_DIVISION

        self.assertEqual(expected_num_teams, len(teams))

    def test__give_teams_byes_gives_the_right_number_of_teams_byes(self):
        # This test is by design intentionally slightly flaky.  If you encounter an error with the assertions,
        #  try running again.
        subject = schedule_generator.ScheduleGenerator()

        n_trials = 100
        sum_num_non_bye_teams = 0
        for i in range(n_trials):
            non_bye = subject._filter_bye_teams(subject._generate_teams())
            self.assertTrue(len(non_bye) % 2 == 0)
            sum_num_non_bye_teams += len(non_bye)

        num_non_bye_teams = float(sum_num_non_bye_teams) / n_trials

        num_teams = NUM_CONFERENCES * NUM_DIVISIONS_PER_CONFERENCE * NUM_TEAMS_PER_DIVISION
        expected_avg_num_non_byes = num_teams - float(NUM_BYES) / NUM_WEEKS * num_teams
        allowable_num_bye_difference = 1
        self.assertTrue(num_non_bye_teams > expected_avg_num_non_byes - allowable_num_bye_difference)
        self.assertTrue(num_non_bye_teams < expected_avg_num_non_byes + allowable_num_bye_difference)

    def test_generate_schedule_returns_correct_number_of_weeks_with_correct_number_of_games(self):
        subject = schedule_generator.ScheduleGenerator()

        result = subject.generate_schedule().weeks

        self.assertEqual(len(result), NUM_WEEKS)
        for week in result:
            self.assertTrue(
                len(week.games) <= NUM_CONFERENCES * NUM_DIVISIONS_PER_CONFERENCE * NUM_TEAMS_PER_DIVISION / 2.0
            )

    def test_assign_games_randomly(self):
        subject = schedule_generator.ScheduleGenerator()
        result = subject.generate_schedule().weeks

        first_half_weeks = result[:int(len(result) / 2)]
        second_half_weeks = result[-int(len(result) / 2):]

        # Each week, there is a greater than 1 / (num_weeks / num_other_teams) chance one team plays another
        num_weeks = NUM_WEEKS - NUM_BYES
        num_teams = NUM_TEAMS_PER_DIVISION * NUM_DIVISIONS_PER_CONFERENCE * NUM_CONFERENCES
        expected_games = (num_weeks - 1) / (num_teams - 1) / 2 + 1
        max_allowable_games = expected_games + 1

        num_successes = 0
        num_failures = 0

        for early_week in first_half_weeks:
            for game in early_week.games:
                t1 = game.home_team
                t2 = game.away_team

                times_played = 1

                for late_week in second_half_weeks:
                    for late_game in late_week.games:
                        if late_game.home_team in {t1, t2} and late_game.away_team in {t1, t2}:
                            times_played += 1

                    if times_played < max_allowable_games:
                        num_successes += 1
                    else:
                        num_failures += 1

        minimum_valid_ratio = 900 / 25
        if num_failures == 0:
            num_successes += minimum_valid_ratio
            num_failures += 1
        self.assertTrue(num_successes / num_failures > minimum_valid_ratio)
