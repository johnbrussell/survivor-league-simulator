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
