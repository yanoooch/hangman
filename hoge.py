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

    def __lt__(self, c2):
        if self.num < c2.num:
            return True
        elif self.num == c2.num and self.suit < c2.suit:
            return True
        else:
            return False
    
    def __gt__(self, c2):
        if self.num > c2.num:
            return True
        elif self.num == c2.num and self.suit > c2.suit:
            return True
        else:
            return False

class Deck:
    deck_list = []
    def __init__(self):
        for i in range(4):
            for j in range(2, 15):
                self.deck_list.append(Card(i, j))
        random.shuffle(self.deck_list)
    
    def __repr__(self):
        return str(self.deck_list)

c1 = Card(2, 13)
c2 = Card(1, 13)
print(c1 < c2)