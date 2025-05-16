from deck52 import deckOfCards, countHand
from time import sleep

game = deckOfCards()
myHand = []
dealerHand = []
def endGame(dHand, pHand):
    sleep(1)
    dHand.append(game.dealOne())
    dHand.append(game.dealOne())
    print(f'{dHand} currentValue: {countHand(dHand)}')
    
    while countHand(dHand) <= 17:
        sleep(0.5)
        card = game.dealOne()
        dHand.append(card)
        print(f'the dealer drew {card}. current value: {countHand(dHand)}')
    sleep(1)
    playerValue = countHand(pHand)
    dealerValue = countHand(dHand)
    print(f'your hand: {playerValue}')
    print(f"dealer's hand: {dealerValue}")
    if playerValue > dealerValue:
        print('You Win!')
    elif playerValue == dealerValue:
        print("It's a tie...")
    else:
        print("the dealer wins...")
    
    #Reset game after round ends
    myHand.clear()
    dHand.clear()

print("Starting game...")

# game CLI interface
while True:
    ans = input(">>> ").lower()
    match ans:
        case "exit":
            break

        case "shuffle":
            game.shuffleDeck()
            print('deck shuffled!')
            myHand = []
            dealerHand = []
            myHand.append(game.dealOne())
            myHand.append(game.dealOne())
            print(f'{myHand} currentValue: {countHand(myHand)}')

            #Dealer draws 2 cards at start of game
            dealerHand.append(game.dealOne())
            dealerHand.append(game.dealOne())
            print(f"Dealer shows: {dealerHand[0]}")

        case "show deck":
            game.printDeck()

        case "show hand":
            print(f'{myHand} current value: {countHand(myHand)}')

        case "hit":
            #Check if game started
            if not myHand:
                print("Start a new game with 'shuffle' first.")
                continue

            card = game.dealOne()
            myHand.append(card)
            print(f'you drew {card}. current value: {countHand(myHand)}')

            #Bust Detection
            if countHand(myHand) > 21:
                print(f'you busted with {countHand(myHand)}. Dealer wins...')
                myHand = []
                dealerHand = []

        case "stay":
            if not myHand:
                print("Start a new game with 'shuffle' first.")
                continue

            print(f"\nyou stay at {countHand(myHand)}. The dealer's turn...")
            endGame(dealerHand, myHand)
            

            


            





