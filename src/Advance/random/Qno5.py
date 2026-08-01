"""
Qno5 - Card Shuffling
Difficult words:
- shuffle: mix in random order
- deck: set of playing cards
"""

import random

suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
ranks = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

deck = [f"{rank} of {suit}" for suit in suits for rank in ranks]
random.shuffle(deck)

print("Top 5 cards after shuffle:")
for card in deck[:5]:
    print(card)
