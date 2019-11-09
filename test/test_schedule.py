import unittest

from survivor_league import schedule, game, week


class TestSchedule(unittest.TestCase):
    def test_games_for_week(self):
        weeks = [week.Week(number=1, games=[game.Game(home_team=1, away_team=2)]),
                 week.Week(number=2, games=[game.Game(home_team=3, away_team=4),
                                            game.Game(home_team=5, away_team=6)])]
        subject = schedule.Schedule(weeks=weeks)

        week_1 = subject.games_for_week(1)
        week_2 = subject.games_for_week(2)

        self.assertEqual(len(week_1), 1)
        self.assertEqual(len(week_2), 2)

        week_1_home = [g.home_team for g in week_1]
        week_1_away = [g.away_team for g in week_1]
        week_2_home = [g.home_team for g in week_2]
        week_2_away = [g.away_team for g in week_2]

        self.assertListEqual(week_1_home, [1])
        self.assertListEqual(week_1_away, [2])
        self.assertListEqual(week_2_home, [3, 5])
        self.assertListEqual(week_2_away, [4, 6])

    def test_num_weeks(self):
        weeks_1 = [1]
        weeks_2 = [2, 3, 4, 5]

        subject_1 = schedule.Schedule(weeks=weeks_1)
        subject_2 = schedule.Schedule(weeks=weeks_2)

        self.assertEqual(subject_1.num_weeks(), 1)
        self.assertEqual(subject_2.num_weeks(), 4)
