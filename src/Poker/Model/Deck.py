'''
Deck

@author: louhiran
'''

import random
from Card import Card

class Deck(object):

    COLORS = ["CLUBS","DIAMONDS","HEARTS","SPADES"]
    NUMBERS = range(1,14)
    JOKER_CARD = Card("JOKER")

    def __init__(self, numberOfJokers = 0):
        self._cards = []
        
        for color in Deck.COLORS:
            for number in Deck.NUMBERS:
                self.add( Card(color,number) )
                
        if numberOfJokers > 0:
            for x in xrange(numberOfJokers):
                self.add(Deck.JOKER_CARD)
        
        self.shuffle()
          
    def __repr__(self):
        cardList = []
        
        for x in self._cards:
            cardList.append(x)
        return cardList
    def __iter__(self):
        '''Deck iterator, returns cards'''
        return iter(self._cards)
    def __contains__(self,card):
        '''Checks if the given card is in the deck'''
        return card in self._cards
    def __len__(self):
        '''Return the number of cards in the deck'''
        return len(self._cards)        

    def __str__(self):
        s = ""
        for card in self._cards:
            s += card.color() + " " + str(card.number()) + "\n"
        return s

    def show(self):
        for x in self._cards:
            print x.color(), x.number()
                      
    def shuffle(self):
        """Shuffle the cards in the deck."""
        random.shuffle(self._cards)

    def draw(self):
        """Draw a card from the deck"""
        return self._cards.pop(0)

    def add(self, card):
        """Add a card to the deck."""
        self._cards.append(card)
