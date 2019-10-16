import unittest

from survivor_league import player


class TestPlayer(unittest.TestCase):
    def test_have_chosen_team(self):
        subject = player.Player()

        self.assertFalse(subject.have_chosen_team(team_name='Some random team name'))

        subject._teams_chosen.add('Chosen team name')

        self.assertTrue(subject.have_chosen_team(team_name='Chosen team name'))
