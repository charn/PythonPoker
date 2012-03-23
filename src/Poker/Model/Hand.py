'''
Hand

@author: louhiran
'''

class Hand(object):
    
    MAX_CARDS_IN_HAND = 5
    
    def __init__(self):
        self._cardsInHand = []

    def __str__(self):
        s = ""
        for card in self._cardsInHand:
            s += card.color() + " " + str(card.number()) + "\n"
        return s
    def __len__(self):
        '''How many cards are currently in hand.'''
        return len(self._cardsInHand)
    
    def __iter__(self):
        '''Hand iterator'''
        return iter(self._cardsInHand)
    
    def __contains__(self,card):
        return card in self._cardsInHand

    def add(self, card):
        '''Add a card to the hand'''
        
        if len(self._cardsInHand) >= Hand.MAX_CARDS_IN_HAND:
            raise Exception
        
        self._cardsInHand.append(card)
        self._cardsInHand.sort()
    
    def replace(self,place,card):
        '''replace the card in "place" with the card "card". Place is between 1-5 '''
        self._cardsInHand[place-1] = card
        
    def getCards(self):
        return self._cardsInHand
