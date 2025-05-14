from deck52 import deckOfCards, countHand
from time import sleep

game = deckOfCards()
myHand = []

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

        case "show deck":
            game.printDeck()

        case "show hand":
            print(f'{myHand} current value: {countHand(myHand)}')

        case "hit":
            card = game.dealOne()
            myHand.append(card)
            print(f'you drew {card}. current value: {countHand(myHand)}')

        case "hold":
            print(f"\nyou hold at {countHand(myHand)}. The dealer's turn...")
            endGame(dealerHand, myHand)
            

            


            





