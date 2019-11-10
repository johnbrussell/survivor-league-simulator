import unittest
from unittest.mock import patch

from survivor_league import league, schedule_generator


class TestLeague(unittest.TestCase):
    def test__generate_players(self):
        subject = league.League(schedule=schedule_generator.ScheduleGenerator().generate_schedule())

        self.assertEqual(len(subject.PLAYERS), league.NUM_PLAYERS)

    def test_simulate_season(self):
        subject = league.League(schedule=schedule_generator.ScheduleGenerator().generate_schedule())

        subject.simulate_season()

        num_still_alive = len([p for p in subject.PLAYERS if p.is_alive()])
        self.assertTrue(num_still_alive < len(subject.PLAYERS))
        self.assertEqual(subject._num_active_players(), num_still_alive)

    def test__simulate_week(self):
        subject = league.League(schedule=schedule_generator.ScheduleGenerator().generate_schedule())
        week_to_simulate = subject.SCHEDULE.weeks[0]
        games = week_to_simulate.games

        home_teams = set()
        away_teams = set()
        for game in games:
            for player in subject.PLAYERS:
                self.assertFalse(player.have_chosen_team(game.home_team.name))
                self.assertFalse(player.have_chosen_team(game.away_team.name))

            home_teams.add(game.home_team)
            away_teams.add(game.away_team)

        # home team wins every game
        with patch('random.random', return_value=0):
            subject._simulate_week(week_to_simulate)

        alive_players = [player for player in subject.PLAYERS if player.is_alive()]
        eliminated_players = [player for player in subject.PLAYERS if not player.is_alive()]

        for player in alive_players:
            self.assertEqual(len([t for t in home_teams if player.have_chosen_team(t.name)]), 1)
            self.assertEqual(len([t for t in away_teams if player.have_chosen_team(t.name)]), 0)

        for player in eliminated_players:
            self.assertEqual(len([t for t in home_teams if player.have_chosen_team(t.name)]), 0)
            self.assertEqual(len([t for t in away_teams if player.have_chosen_team(t.name)]), 1)

    def test__num_active_players(self):
        subject = league.League(schedule=schedule_generator.ScheduleGenerator().generate_schedule())

        self.assertEqual(subject._num_active_players(), len(subject.PLAYERS))

        subject.PLAYERS[0].eliminate(0)

        self.assertEqual(subject._num_active_players(), len(subject.PLAYERS) - 1)

    def test__active_players(self):
        subject = league.League(schedule=schedule_generator.ScheduleGenerator().generate_schedule())

        self.assertEqual(len(subject._active_players()), len(subject.PLAYERS))

        subject.PLAYERS[0].eliminate(0)

        self.assertEqual(len(subject._active_players()), len(subject.PLAYERS) - 1)
        self.assertFalse(subject.PLAYERS[0].name() in subject._active_players())

    def test__choose_teams(self):
        subject = league.League(schedule=schedule_generator.ScheduleGenerator().generate_schedule())

        with patch('survivor_league.player.Player.choose_team', return_value='winner'):
            choices = subject._choose_teams(subject.SCHEDULE.weeks[0].games)

        for player in subject.PLAYERS:
            self.assertTrue(player.name() in choices)
            self.assertEqual(choices[player.name()], 'winner')

    def test__determine_game_winners(self):
        subject = league.League(schedule=schedule_generator.ScheduleGenerator().generate_schedule())
        games = subject.SCHEDULE.weeks[0].games
        home_teams = [g.home_team for g in games]

        with patch('random.random', return_value=0):
            winners_names = subject._determine_game_winners(subject.SCHEDULE.weeks[0].games)

        self.assertEqual(len(home_teams), len(winners_names))
        for t in home_teams:
            self.assertTrue(t.name in winners_names)

    def test__eliminate_losers(self):
        subject = league.League(schedule=schedule_generator.ScheduleGenerator().generate_schedule())

        choices = dict()
        for p in subject.PLAYERS:
            choices[p.name()] = 0
        choices[subject.PLAYERS[0].name()] = 1

        winning_team_names = [0]

        subject._eliminate_losers(choices, winning_team_names, 300)

        self.assertListEqual(subject._active_players(), subject.PLAYERS[1:])
        self.assertFalse(subject.PLAYERS[0].is_alive())
        self.assertEqual(subject.PLAYERS[0]._elimination_week_num, 300)
