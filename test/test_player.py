import unittest

from survivor_league import player, game, team
from survivor_league.strategies import choose_randomly


class TestPlayer(unittest.TestCase):
    def test_have_chosen_team(self):
        subject = player.Player(name=0, strategy=None)

        self.assertFalse(subject.have_chosen_team(team_name='Some random team name'))

        subject._teams_chosen.add('Chosen team name')

        self.assertTrue(subject.have_chosen_team(team_name='Chosen team name'))

    def test_choose_team(self):
        subject = player.Player(name=0, strategy=choose_randomly.ChooseRandomly())

        teams = [team.Team(name=t, division=t, conference=t) for t in range(4)]
        games = [game.Game(home_team=t1, away_team=t2) for t1, t2 in zip(teams[:int(len(teams)/2)],
                                                                         teams[int(len(teams)/2):])]

        choice = subject.choose_team(games)

        self.assertTrue(len([t for t in teams if t.name == choice]) == 1)
        self.assertTrue(choice in subject._teams_chosen)
        self.assertTrue(subject.have_chosen_team(choice))

    def test_eliminate(self):
        subject = player.Player(name=0, strategy=choose_randomly.ChooseRandomly())

        self.assertTrue(subject.is_alive())
        self.assertIsNone(subject._elimination_week_num)

        subject.eliminate(3)

        self.assertFalse(subject.is_alive())
        self.assertEqual(subject._elimination_week_num, 3)
