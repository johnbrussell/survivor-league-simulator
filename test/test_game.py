import unittest

from survivor_league import game, team


class TestGame(unittest.TestCase):
    def test_odds_even_for_equal_elos(self):
        team_1 = team.Team(name=1, conference=1, division=1)
        team_2 = team.Team(name=2, conference=1, division=1)

        subject = game.Game(home_team=team_1, away_team=team_2)

        self.assertEqual(.5, subject.home_team_win_probability())

    def test_odds_favorable_for_favored_team(self):
        team_1 = team.Team(name=1, elo=1300, conference=1, division=1)
        team_2 = team.Team(name=2, elo=1200, conference=1, division=1)

        subject = game.Game(home_team=team_1, away_team=team_2)

        self.assertGreater(subject.home_team_win_probability(), .5)

    def test_odds_unfavorable_for_unfavored_team(self):
        team_1 = team.Team(name=1, elo=1300, conference=1, division=1)
        team_2 = team.Team(name=2, elo=1400, conference=1, division=1)

        subject = game.Game(home_team=team_1, away_team=team_2)

        self.assertLess(subject.home_team_win_probability(), .5)

    def test_choose_winner(self):
        team_1 = team.Team(name=1, elo=1300, conference=1, division=1)
        team_2 = team.Team(name=2, elo=1400, conference=1, division=1)

        subject = game.Game(home_team=team_1, away_team=team_2)

        winner = subject.choose_winner(subject.home_team_win_probability() / 2)

        self.assertTrue(winner.name == 1)

        winner = subject.choose_winner(1 - (subject.home_team_win_probability() / 2))

        self.assertTrue(winner.name == 2)

    def test_favored_team(self):
        team_1 = team.Team(name=1, elo=1300, conference=1, division=1)
        team_2 = team.Team(name=2, elo=1400, conference=1, division=1)

        subject = game.Game(home_team=team_1, away_team=team_2)
        favored_team = subject.favored_team()
        self.assertEqual(favored_team.name, team_2.name)

        subject = game.Game(home_team=team_2, away_team=team_1)
        favored_team = subject.favored_team()
        self.assertEqual(favored_team.name, team_2.name)

    def test_unfavored_team(self):
        team_1 = team.Team(name=1, elo=1300, conference=1, division=1)
        team_2 = team.Team(name=2, elo=1400, conference=1, division=1)

        subject = game.Game(home_team=team_1, away_team=team_2)
        favored_team = subject.unfavored_team()
        self.assertEqual(favored_team.name, team_1.name)

        subject = game.Game(home_team=team_2, away_team=team_1)
        favored_team = subject.unfavored_team()
        self.assertEqual(favored_team.name, team_1.name)
