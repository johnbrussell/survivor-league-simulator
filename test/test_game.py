import unittest

from survivor_league import game, team


class TestGame(unittest.TestCase):
    def test_odds_even_for_equal_elos(self):
        team_1 = team.Team(name=1)
        team_2 = team.Team(name=2)

        subject = game.Game(team_1=team_1, team_2=team_2)

        self.assertEqual((team_1.name, .5), subject.odds())

    def test_odds_favorable_for_favored_team(self):
        team_1 = team.Team(name=1, elo=1300)
        team_2 = team.Team(name=2, elo=1200)

        subject = game.Game(team_1=team_1, team_2=team_2)

        self.assertGreater(subject.odds()[1], .5)

    def test_odds_unfavorable_for_unfavored_team(self):
        team_1 = team.Team(name=1, elo=1300)
        team_2 = team.Team(name=2, elo=1400)

        subject = game.Game(team_1=team_1, team_2=team_2)

        self.assertLess(subject.odds()[1], .5)
