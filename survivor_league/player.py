class Player:
    def __init__(self, name, strategy):
        self._teams_chosen = set()
        self._name = name
        self._strategy = strategy
        self._is_alive = True
        self._elimination_week_num = None

    def choose_team(self, games):
        ranked_teams = self._strategy.rank_teams(games, self._teams_chosen)
        if len(ranked_teams) == 0:
            return None

        choice = ranked_teams[0].name
        self._teams_chosen.add(choice)

        return ranked_teams[0].name

    def eliminate(self, week_num):
        self._is_alive = False
        self._elimination_week_num = week_num

    def elimination_week(self):
        return self._elimination_week_num

    def have_chosen_team(self, team_name):
        return team_name in self._teams_chosen

    def is_alive(self):
        return self._is_alive

    def name(self):
        return self._name

    def strategy_name(self):
        return self._strategy.name
