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

    def shuffleDeck(self):
        """Return a set of deck52 in randomized order"""
        deck = self.deck52
        return shuffle(deck)
        
    def printDeck(self):
        print(self.deck52)
    
    def dealOne(self):
        """return the top card of the deck and remove it"""
        dealt = self.deck52[0]
        self.deck52.pop(0)
        # print(dealt)
        return dealt

if __name__ == "__main__":    
    # quick showcase of how to run the game
    game = deckOfCards()
    game.shuffleDeck()
    game.printDeck()

    hand = []
    hand.append(game.dealOne())
    hand.append(game.dealOne())
    hand.append(game.dealOne())

    print(hand)
    game.printDeck()