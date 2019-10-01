import unittest

from survivor_league import team


class TestTeam(unittest.TestCase):
    def test_set_elo(self):
        expected_elo = 1400

        subject = team.Team(elo=expected_elo)

        self.assertEqual(expected_elo, subject.elo)

    def test_fall_back_to_default_elo(self):
        expected_elo = team.DEFAULT_ELO

        subject = team.Team()

        self.assertEqual(expected_elo, subject.elo)
