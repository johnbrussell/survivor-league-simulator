import unittest

from survivor_league import schedule_generator


class TestScheduleGenerator(unittest.TestCase):
    def test__generate_teams_returns_correct_number_of_teams(self):
        subject = schedule_generator.ScheduleGenerator()

        teams = subject._generate_teams()

        expected_num_teams = schedule_generator.NUM_CONFERENCES * \
                             schedule_generator.NUM_DIVISIONS_PER_CONFERENCE * \
                             schedule_generator.NUM_TEAMS_PER_DIVISION

        self.assertEqual(expected_num_teams, len(teams))
