from random import shuffle

class deckOfCards:

    def __init__(self):
        """
        Represent a standard deck of playing cards, where the first letter represents the suite, and the second number/letter represents the value.
        Clubs and Spades are black, Diamonds and Hearts are red.
        """
        self.deck52 = [
            "cA", "c2", "c3", "c4", "c5", "c6", "c7", "c8", "c9", "c10", "cJ", "cQ", "cK",
            "dA", "d2", "d3", "d4", "d5", "d6", "d7", "d8", "d9", "d10", "dJ", "dQ", "dK",
            "hA", "h2", "h3", "h4", "h5", "h6", "h7", "h8", "h9", "h10", "hJ", "hQ", "hK", 
            "sA", "s2", "s3", "s4", "s5", "s6", "s7", "s8", "s9", "s10", "sJ", "sQ", "sK"          
            ]
        self.gameDeck = []

    def shuffleDeck(self):
        """Copies decek52 to gameDeck in randomized order"""
        self.gameDeck = self.deck52.copy()
        shuffle(self.gameDeck)
        return self.gameDeck
    
    def countDeck(self): # for testing, return number of cards in deck
        return len(self.gameDeck)
        
    def printDeck(self): # for testing, shows the deck order
        print(self.gameDeck)
    
    def dealOne(self):
        """return the top card of the deck and remove it"""
        dealt = self.gameDeck[0]
        self.gameDeck.pop(0)
        # print(dealt)
        return dealt
    

        

def countHand(hand):
    deck = {
        "cA": 11, # Worth 11 by default. game logic will check if it is more value to have it at 1.
        "c2": 2,
        "c3": 3,
        "c4": 4,
        "c5": 5,
        "c6": 6,
        "c7": 7,
        "c8": 8,
        "c9": 9,
        "c10": 10,
        "cJ": 10,
        "cQ": 10,
        "cK": 10,
        "dA": 11,
        "d2": 2,
        "d3": 3,
        "d4": 4,
        "d5": 5,
        "d6": 6,
        "d7": 7,
        "d8": 8,
        "d9": 9,
        "d10": 10,
        "dJ": 10,
        "dQ": 10,
        "dK": 10,
        "hA": 11,
        "h2": 2,
        "h3": 3,
        "h4": 4,
        "h5": 5,
        "h6": 6,
        "h7": 7,
        "h8": 8,
        "h9": 9,
        "h10": 10,
        "hJ": 10,
        "hQ": 10,
        "hK": 10,
        "sA": 11,
        "s2": 2,
        "s3": 3,
        "s4": 4,
        "s5": 5,
        "s6": 6,
        "s7": 7,
        "s8": 8,
        "s9": 9,
        "s10": 10,
        "sJ": 10,
        "sQ": 10,
        "sK": 10
    }
    value = 0
    for card in hand:
        cardValue = deck[card]
        if cardValue == 11 and value + cardValue >= 21:
            value += 1
        else:
            value += deck[card]
    
    return value

if __name__ == "__main__":    
    # quick showcase of how to run the game

    print('setting up game...')
    game = deckOfCards()
    game.shuffleDeck()
    print(f'current number of cards in deck: {game.countDeck()}')
    game.printDeck()
    

    print('\ndrawing 3...')
    myhand = []
    myhand.append(game.dealOne())
    myhand.append(game.dealOne())
    myhand.append(game.dealOne())

    print('\nshowing hand...')
    print(myhand)
    print(f'currernt value: {countHand(myhand)}')
    print(f'current number of cards in deck: {game.countDeck()}')
    game.printDeck()

    print('\nshuffling deck, expected number of cards: 52')
    game.shuffleDeck()
    game.printDeck()
    print(f'current number of cards in deck: {game.countDeck()}')
