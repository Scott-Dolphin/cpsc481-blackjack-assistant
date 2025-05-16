from deck52 import deckOfCards, countHand
from time import sleep

game = deckOfCards()
myHand = []
dealerHand = []
strategy_chart = {
    ("11 or less", 2): "Hit", ("11 or less", 3): "Hit", ("11 or less", 4): "Hit", ("11 or less", 5): "Hit",
    ("11 or less", 6): "Hit", ("11 or less", 7): "Hit", ("11 or less", 8): "Hit", ("11 or less", 9): "Hit",
    ("11 or less", 10): "Hit", ("11 or less", 11): "Hit",

    ("12", 2): "Hit", ("12", 3): "Hit", ("12", 4): "Stay", ("12", 5): "Stay", ("12", 6): "Stay",
    ("12", 7): "Hit", ("12", 8): "Hit", ("12", 9): "Hit", ("12", 10): "Hit", ("12", 11): "Hit",

    ("13", 2): "Stay", ("13", 3): "Stay", ("13", 4): "Stay", ("13", 5): "Stay", ("13", 6): "Stay",
    ("13", 7): "Hit", ("13", 8): "Hit", ("13", 9): "Hit", ("13", 10): "Hit", ("13", 11): "Hit",

    ("14", 2): "Stay", ("14", 3): "Stay", ("14", 4): "Stay", ("14", 5): "Stay", ("14", 6): "Stay",
    ("14", 7): "Hit", ("14", 8): "Hit", ("14", 9): "Hit", ("14", 10): "Hit", ("14", 11): "Hit",

    ("15", 2): "Stay", ("15", 3): "Stay", ("15", 4): "Stay", ("15", 5): "Stay", ("15", 6): "Stay",
    ("15", 7): "Hit", ("15", 8): "Hit", ("15", 9): "Hit", ("15", 10): "Hit", ("15", 11): "Hit",

    ("16", 2): "Stay", ("16", 3): "Stay", ("16", 4): "Stay", ("16", 5): "Stay", ("16", 6): "Stay",
    ("16", 7): "Hit", ("16", 8): "Hit", ("16", 9): "Hit", ("16", 10): "Hit", ("16", 11): "Hit",

    ("17+", 2): "Stay", ("17+", 3): "Stay", ("17+", 4): "Stay", ("17+", 5): "Stay", ("17+", 6): "Stay",
    ("17+", 7): "Stay", ("17+", 8): "Stay", ("17+", 9): "Stay", ("17+", 10): "Stay", ("17+", 11): "Stay",
}

def get_hand_label(hand):
    value = countHand(hand)
    if value <= 11:
        return "11 or less"
    elif value >= 17:
        return "17+"
    else:
        return str(value)

def map_dealer_card_value(dealer_card):
    val = dealer_card[-1]
    if val in ['J', 'Q', 'K', '0']:
        return 10
    elif val == 'A':
        return 11
    else:
        return int(val)

def recommendMove(playerHand, dealerCard):
    hand_label = get_hand_label(playerHand)
    dealer_value = map_dealer_card_value(dealerCard)
    return strategy_chart.get((hand_label, dealer_value), "No recommendation")

def endGame(dHand, pHand):
    sleep(1)
    playerValue = countHand(pHand)
    dealerValue = countHand(dHand)

    while dealerValue < 17 or (dealerValue < playerValue and dealerValue <= 21):
        sleep(0.5)
        card = game.dealOne()
        dHand.append(card)
        dealerValue = countHand(dHand)
        print(f'the dealer drew {card}. current value: {dealerValue}')

    sleep(1)
    print(f'your hand: {playerValue}')
    print(f"dealer's hand: {dealerValue}")

    if dealerValue > 21:
        print("Dealer busted! You win!")
    elif playerValue > dealerValue:
        print('You Win!')
    elif playerValue == dealerValue:
        print("It's a tie...")
    else:
        print("the dealer wins...")

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

            # Dealer draws 2 cards at start of game
            dealerHand.append(game.dealOne())
            dealerHand.append(game.dealOne())
            print(f"Dealer shows: {dealerHand[0]}")

        case "show deck":
            game.printDeck()

        case "show hand":
            print(f'{myHand} current value: {countHand(myHand)}')

        case "hit":
            if not myHand:
                print("Start a new game with 'shuffle' first.")
                continue

            print("Recommendation:", recommendMove(myHand, dealerHand[0]))

            card = game.dealOne()
            myHand.append(card)
            print(f'you drew {card}. current value: {countHand(myHand)}')

            if countHand(myHand) > 21:
                print(f'you busted with {countHand(myHand)}. Dealer wins...')
                myHand = []
                dealerHand = []

        case "stay":
            if not myHand:
                print("Start a new game with 'shuffle' first.")
                continue

            print("Recommendation:", recommendMove(myHand, dealerHand[0]))
            print(f"\nyou stay at {countHand(myHand)}. The dealer's turn...")
            endGame(dealerHand, myHand)

            

            


            





