import sys
import re
import random

class Card:
    suits = ("SPADES", "HEARTS", "DIAMONDS", "CLUBS")
    nums = (None, None, "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A")
    def __init__(self, suit, num):
        self.suit = suit
        self.num = num

    def __repr__(self):
        return f"{self.nums[self.num]} of {self.suits[self.suit]}"

class Deck:
    deck_list = []
    def __init__(self):
        for i in range(4):
            for j in range(2, 15):
                self.deck_list.append(Card(i, j))
        random.shuffle(self.deck_list)

d = Deck()
for i in d.deck_list:
    print(i)
    
