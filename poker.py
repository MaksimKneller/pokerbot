from hand import *
from deck import *

def getHoleCards():
    return d.takeCards(2)

def getFlopCards():
    return d.takeCards(3)

def getTurnCard():
    return d.takeCards(1)

def getRiverCard():
    return d.takeCards(1)



if (__name__ == '__main__'):

    d = Deck()

    holeCards = getHoleCards()
    flopCards = getFlopCards()
    turnCard = getTurnCard()
    riverCard = getRiverCard()

    hand1 = Hand(d.takeCards(5))
    hand2 = Hand(d.takeCards(5))

    #hand1 = Hand([Card(2,'d'),Card(5,'h'),Card(6,'d'),Card(7,'c'),Card(9,'c')])
    #hand2 = Hand([Card(4,'c'),Card(10,'d'),Card(10,'h'),Card(3,'h'),Card(10,'s')])

    res = hand1.compare(hand2)

    print(str(hand1.cards), hand1.handType)
    print(str(hand2.cards), hand2.handType)

    print(res)