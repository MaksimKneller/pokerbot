class Card:

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __le__(self, other):
        return self.rank <= other.rank

    def __lt__(self,other):
        return self.rank < other.rank


    def __ge__(self, other):
        return self.rank >= other.rank

    def __eq__(self, other):
        return self.rank == other.rank

    def __repr__(self):
        letters = {11:'J', 12:'Q', 13:'K', 14:'A',1:'A'}
        letter = letters.get(self.rank, str(self.rank))
        return "%s%s" % (letter, self.suit)

