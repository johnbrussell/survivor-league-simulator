import unittest

from survivor_league.strategies import choose_randomly
from survivor_league import team, game


class TestChooseRandomly(unittest.TestCase):
    @staticmethod
    def generate_subject_teams_games_choice_count(num_eligible_teams, num_ineligible_teams=0):
        subject = choose_randomly.ChooseRandomly()

        teams = [team.Team(name=n, conference=1, division=1) for n in range(num_eligible_teams + num_ineligible_teams)]
        home_teams = teams[:int((len(teams)/2))]
        away_teams = teams[int(len(teams)/2):]
        games = [game.Game(home_team=h, away_team=a) for h, a in zip(home_teams, away_teams)]

        team_choice_count = {}
        for t in teams:
            team_choice_count[t.name] = 0

        return subject, teams, games, team_choice_count

    def test_choice_is_random(self):
        num_teams = 4

        subject, teams, games, team_choice_count = self.generate_subject_teams_games_choice_count(num_teams)

        for _ in range(100):
            ranked_teams = subject.rank_teams(games, {})
            team_choice_count[ranked_teams[0].name] += 1

        self.assertTrue(min(team_choice_count.values()) >= 15)
        self.assertTrue(max(team_choice_count.values()) < 35)

    def test_choice_does_not_include_ineligible_teams(self):
        num_eligible_teams = 4
        num_ineligible_teams = 2

        subject, teams, games, team_choice_count = self.generate_subject_teams_games_choice_count(num_eligible_teams,
                                                                                                  num_ineligible_teams)

        for _ in range(100):
            ranked_teams = subject.rank_teams(games, [t.name for t in teams[-num_ineligible_teams:]])
            team_choice_count[ranked_teams[0].name] += 1

        self.assertEqual(len([t for t in team_choice_count if team_choice_count[t] > 0]), num_eligible_teams)
        self.assertEqual(len([t for t in team_choice_count if team_choice_count[t] == 0]), num_ineligible_teams)
