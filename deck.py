from card import *
from random import shuffle

class Deck:

    def __init__(self):
        values = [x for x in range(2,14)]
        suits = "d c h s".split()

        self.deck_of_cards = [ Card(v,s) for v in values for s in suits ]

        shuffle(self.deck_of_cards)

    def takeCards(self, num):
        return [self.deck_of_cards.pop() for _ in range(0,num)]

    def __repr__(self):
        return str(self.deck_of_cards)
