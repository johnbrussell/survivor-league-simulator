import unittest

from survivor_league import league, schedule_generator


class TestLeague(unittest.TestCase):
    def test__generate_players(self):
        subject = league.League(schedule=schedule_generator.ScheduleGenerator().generate_schedule())

        self.assertEqual(len(subject.PLAYERS), league.NUM_PLAYERS)
