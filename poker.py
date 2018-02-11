from hand import *
from deck import *
from player import *
from tqdm import tqdm

from itertools import combinations

def getHoleCards():
    return d.takeCards(2)

def getFlopCards():
    return d.takeCards(3)

def getTurnCard():
    return d.takeCards(1)

def getRiverCard():
    return d.takeCards(1)


def findBestHand(possibleHands):

    hand = Hand(list(possibleHands.pop()))

    if(len(possibleHands) == 0):
        return hand

    hand2 = findBestHand(possibleHands)
    res = hand.compare(hand2)

    if res == -1:
        return hand2
    elif res == 1 or res == 0:
        return hand


def findWinningPlayers(players):

    winningPlayers = []

    # find one of the highest hands
    bestPlayer = players[0]

    for player in players:
        if player.hand.compare(bestPlayer.hand) == 1:
            bestPlayer = player


    # find if anyone eles tied with the best hand
    for player in players:

        if player.name == bestPlayer.name: continue

        if player.hand.compare(bestPlayer.hand) == 0:
            winningPlayers.append(player)


    winningPlayers.append(bestPlayer)

    return winningPlayers





if (__name__ == '__main__'):

    __DEBUG__ = False

    allPlayers = [
        Player("Batman"),
        Player("Spiderman"),
        Player("TheFlash"),
        Player("Superman"),
        Player("Aquaman"),
        Player("Wolverine"),
        Player("Storm"),
        Player("Arnold"),
        Player("SpongeBob") ]


    for x in tqdm(range(100000)):

        playersInGame = []

        d = Deck()

        flopCards = getFlopCards()
        turnCard = getTurnCard()
        riverCard = getRiverCard()

        for player in allPlayers:
            holeCards = getHoleCards()

            if(player.name == "Batman"):
                if (holeCards[0].rank != 14 or holeCards[1].rank != 14): continue

            player.setHand(findBestHand([h for h in combinations(holeCards + flopCards + turnCard + riverCard, 5)]))
            player.games +=1
            playersInGame.append(player)


        winningPlayers = findWinningPlayers(playersInGame)


        if(len(winningPlayers) == 1):
            winningPlayers[0].wins += 1



    for player in allPlayers:
        tqdm.write("{0:<10} WinRate: {1:>5.3}%".format(player.name, player.getWinRate()))