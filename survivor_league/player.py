class Player:
    def __init__(self):
        self._teams_chosen = set()

    def have_chosen_team(self, team_name):
        return team_name in self._teams_chosen
