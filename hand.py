import numpy as np


class Hand:

    def __init__(self, cards):
        self.cards = cards
        self.cards.sort()
        self.handType = self.evaluate()

    def __repr__(self):
        return str(self.cards)

    def sortHandByRank(self):
        self.cards.sort()

    def sortbysuitkey(self,item):
        return item.suit

    def sortHandBySuit(self):
        self.cards.sort(key=self.sortbysuitkey)

    def isFlush(self):
        self.sortHandBySuit()
        if (self.cards[0].suit == self.cards[-1].suit): return True
        return False

    def isStraight(self):
        self.sortHandByRank()

        if (self.cards[-1].rank - self.cards[0].rank == len(self.cards) - 1): return True

        # convert hand to a Wheel in case high card is an Ace
        if (self.cards[-1].rank == 14 and self.cards[-2].rank == 5):
            self.cards[-1].rank = 1
            self.sortHandByRank()
            return True

        return False


    def evaluate(self):

        handType = "HIGH"

        if (len(self.cards) != 5): raise ValueError("Evaluate() accepts 5 cards only!")

        # build a histogram of ranks to evaluate one pair, two pair, set(trips), full house (boat), quads
        numpy_hist = np.histogram([card.rank for card in self.cards], bins=15)
        ranks_histogram = sorted([x for x in numpy_hist[0] if x != 0], reverse=True)

        if ranks_histogram == [4, 1]: handType = "QUADS"
        if ranks_histogram == [3, 2]: handType = "FULLHOUSE"
        if ranks_histogram == [3, 1, 1]: handType = "TRIPS"
        if ranks_histogram == [2, 2, 1]: handType = "TWOPAIR"
        if len(ranks_histogram) == 4: handType = "PAIR"
        if handType != "HIGH": return handType

        if (self.isFlush()): handType = "FLUSH"

        if (self.isStraight()):
            if (handType == "FLUSH"):
                handType = "STRAIGHTFLUSH"
            else:
                handType = "STRAIGHT"

        return handType

    def compare(self, other):
      
        typeToNum = {"STRAIGHTFLUSH":9,"QUADS":8,"FULLHOUSE":7,"FLUSH":6,"STRAIGHT":5,"TRIPS":4,"TWOPAIR":3,"PAIR":2,"HIGH":1}

        res = 0
        print(typeToNum[self.handType],typeToNum[other.handType])
        if (typeToNum[self.handType] > typeToNum[other.handType]): res = 1
        if (typeToNum[self.handType] < typeToNum[other.handType]): res = -1
        if(res != 0): return res


        # if both straights then compare the high cards
        if(res == 0 and self.handType in ["STRAIGHT", "STRAIGHTFLUSH"]):
            if(self.cards[-1] > other.cards[-1]): res = 1
            elif (self.cards[-1] < other.cards[-1]): res = -1
            return res

        # if both flushes or nothing then compare each other's ranks to find the higher
        if (res == 0 and self.handType in ["FLUSH","HIGH"]):
            for x in reversed(range(5)):
                if(self.cards[x] > other.cards[x]): return 1
                elif(self.cards[x] < other.cards[x]): return -1
            return res

        # if both hands have quads, trips or set, the 3rd card in sorted hand will always be part of the quad,trip or set
        if (res == 0 and self.handType in ["QUADS","TRIPS","FULLHOUSE"]):
            if(self.cards[2] > other.cards[2]): res = 1
            elif (self.cards[2] < other.cards[2]): res = -1
            else:
                # if table itself got quads or fullhouse then both hands will have them
                # so compare by kickers by removing matched quads or sets
                # in case of fullhouse, kicker is the pair
                selfKicker = sorted([x.rank for x in self.cards if x.rank != self.cards[2].rank],reverse=True)
                otherKicker = sorted([x.rank for x in other.cards if x.rank != self.cards[2].rank],reverse=True)
                if(selfKicker > otherKicker): res = 1
                if(selfKicker < otherKicker): res = -1
            return res

        # if two pair, then evaluate the highest pair first, then second pair, then kicker
        # detect pairs by extracting duplicates, sorting, appending the kicker, and comparing the lists
        if (res == 0 and self.handType in ["TWOPAIR", "PAIR"]):
            selfDupes = [x for n,x in enumerate(self.cards) if x in self.cards[:n]]
            selfDupes.sort(reverse=True)
            selfKicker = [k for k in self.cards if k not in selfDupes]
            selfKicker.sort(reverse=True)
            selfDupes.extend(selfKicker)

            otherDupes = [x for n, x in enumerate(other.cards) if x in other.cards[:n]]
            otherDupes.sort(reverse=True)
            otherKicker = [k for k in other.cards if k not in otherDupes]
            otherKicker.sort(reverse=True)
            otherDupes.extend(otherKicker)

            print(selfDupes, otherDupes)
            if selfDupes < otherDupes: res = -1
            elif selfDupes > otherDupes: res = 1


        return res
