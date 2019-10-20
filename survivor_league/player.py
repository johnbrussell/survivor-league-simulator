class Player:
    def __init__(self, strategy):
        self._teams_chosen = set()
        self._strategy = strategy

    def choose_team(self, games):
        ranked_teams = self._strategy.rank_teams(games, self._teams_chosen)
        if len(ranked_teams) == 0:
            return None
        return ranked_teams[0].name

    def have_chosen_team(self, team_name):
        return team_name in self._teams_chosen
