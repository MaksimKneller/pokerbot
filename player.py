
class Player:

    games = 0
    wins = 0

    def __init__(self, _name):
        self.name = _name

    def setHand(self, _hand):
        self.hand = _hand

    def __repr__(self):
        return self.name

    def getWinRate(self):
        winrate = 0.0
        if self.games > 0: winrate = (self.wins/self.games)*100.0
        return winrate
