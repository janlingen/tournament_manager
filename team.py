class Team:
    def __init__(self, name):
        self.name = name
        self._wins = 0

    @property
    def wins(self):
        return self._wins

    @wins.setter
    def wins(self, x):
        self.wins = x
