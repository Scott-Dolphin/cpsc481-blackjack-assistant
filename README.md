# cpsc481-blackjack-assistant
A Python-based command-line Blackjack game with real-time strategy recommendations based on Basic Strategy.
This project helps Blackjack players make optimal decisions while playing by providing live recommendations (Hit or Stay) based on the player's hand and the dealer's visible card.
It is designed to help players learn and apply Basic Strategy, improving their decision-making and overall win rate.

## Running the game:
`python3 blackjack.py`

## How to play:
Type shuffle to start a new game.

After seeing your hand and the dealer’s upcard, check the recommendation printed before each move.
Type one of the following commands:

hit – Draw another card.

stay – Hold your current hand.

exit – Exit the game.

You can control the game by typing it into the command line like so
```
Starting game...
>>> shuffle
deck shuffled!
['c10', 'c2'] currentValue: 12
Dealer shows: h7
Recommendation: Hit
>>> hit
you drew h4. current value: 16
Recommendation: Hit
>>> hit
you drew h6. current value: 22
you busted with 22. Dealer wins...
>>> shuffle
deck shuffled!
['cJ', 'cQ'] currentValue: 20
Dealer shows: hA
Recommendation: Stay
>>> stay

you stay at 20. The dealer's turn...
the dealer drew c8. current value: 14
the dealer drew d7. current value: 21
your hand: 20
dealer's hand: 21
the dealer wins...
>>> exit
```
