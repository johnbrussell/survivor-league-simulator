import unittest

from survivor_league.strategies import randomly_choose_favored_team
from survivor_league import team, game


class TestRandomlyChooseFavoredTeam(unittest.TestCase):
    def test_favor_favored_teams(self):
        subject = randomly_choose_favored_team.RandomlyChooseFavoredTeam()

        team_1 = team.Team(name=1, conference=1, division=1, elo=1100)
        team_2 = team.Team(name=2, conference=2, division=2, elo=1200)
        team_3 = team.Team(name=3, conference=3, division=3, elo=1300)
        team_4 = team.Team(name=4, conference=4, division=4, elo=1400)
        teams = [team_1, team_2, team_3, team_4]
        home_teams = teams[:int((len(teams)/2))]
        away_teams = teams[int(len(teams)/2):]
        games = [game.Game(home_team=h, away_team=a) for h, a in zip(home_teams, away_teams)]

        ranked_teams = subject.rank_teams(games, [])

        self.assertTrue(team_4 in ranked_teams[:2])

    def test_ignore_ineligible_teams(self):
        subject = randomly_choose_favored_team.RandomlyChooseFavoredTeam()

        team_1 = team.Team(name=1, conference=1, division=1, elo=1100)
        team_2 = team.Team(name=2, conference=2, division=2, elo=1200)
        team_3 = team.Team(name=3, conference=3, division=3, elo=1300)
        team_4 = team.Team(name=4, conference=4, division=4, elo=1400)
        teams = [team_1, team_2, team_3, team_4]
        home_teams = teams[:int((len(teams) / 2))]
        away_teams = teams[int(len(teams) / 2):]
        games = [game.Game(home_team=h, away_team=a) for h, a in zip(home_teams, away_teams)]

        ranked_teams = subject.rank_teams(games, [1, 4])

        self.assertEqual(len(ranked_teams), 2)
        self.assertTrue(team_4 not in ranked_teams)
