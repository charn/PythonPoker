'''
WinChecker
Can check a hand if it has a winning combination of cards.

@author: louhiran
'''

from Poker.Model.Deck import Deck

class WinChecker(object):   
   
    def __init__(self, numberOfJokers):
        if numberOfJokers > 0:
            raise NotImplementedError("No support for Joker -cards")
    
    def hasAPair(self,hand):
        '''Hand has a pair in it.'''
        numList = []
        for card in hand:
            if card.number() in numList:
                return True
            numList.append(card.number())
        return False
    
    def hasTwoPairs(self,hand):
        '''Hand has two pairs in it.'''
        numList = []
        pairs = 0
        for card in hand:
            if card.number() in numList:
                pairs += 1
            if pairs == 2:
                return True
            numList.append(card.number())
        return False
    
    def hasThreeOfAKind(self,hand):
        '''Hand has three of a king in it.'''
        numList = self._cardNumbersToList(hand)

        for i in xrange(1,14):
            if numList.count(i) == 3:
                return True
        return False
    
    def hasStraight(self,hand):
        '''Hand has straight in it.'''
        numList = self._cardNumbersToList(hand)
        numList.sort()
        
        lastNumber = numList[0]
        
        for x in numList[1:]:
            if x != lastNumber + 1:
                return False
            lastNumber = x
        
        return True
    
    def hasFlush(self,hand):
        '''Hand has flush in it.'''
        colorList = self._cardColorsToList(hand)
        
        for color in colorList:
            if colorList.count(color) == 5:
                return True
        return False
    
    def hasFullHouse(self,hand):
        '''Hand has full house in it.'''
        numList = self._cardNumbersToList(hand)
        hasThreeOfAKind = False
        hasPair = False
        
        for number in numList:
            if numList.count(number) == 3:
                hasThreeOfAKind = True
            if numList.count(number) == 2:
                hasPair = True
        
        if hasThreeOfAKind and hasPair:
            return True
        
        return False
    
    def hasFourOfAKind(self,hand):
        '''Hand has four of a kind in it.'''
        numList = self._cardNumbersToList(hand)
        
        for number in numList:
            if numList.count(number) == 4:
                return True    
        return False
    
    def hasStraightFlush(self,hand):
        '''Hand has straight flush in it.'''
        if self.hasStraight(hand) and self.hasFlush(hand):
            return True
        return False
    
    def hasFiveOfAKind(self,hand):
        '''Hand has five of a kind in it.'''
        raise NotImplementedError("No support for Joker -cards")
    
    def _hasJoker(self,hand):
        '''Hand has one joker -card in it.'''
        if hand._countJokers() == 1:
            return True
        return False
    
    def _hasTwoJokers(self,hand):
        '''Hand has two joker -cards in it.'''
        if hand._countJokers() == 2:
            return True
        return False
        
    def _countJokers(self,hand):
        '''Count how many joker cards are in the hand.'''
        jokers = 0
        for card in hand:
            if card == Deck.JOKER_CARD:
                jokers += 1
        return jokers
    
    def _cardNumbersToList(self,hand):
        '''Put cards numbers to a list.'''
        numList = []
        for card in hand:
            numList.append(card.number())
        return numList
    
    def _cardColorsToList(self,hand):
        '''Put cards colors to a list.'''
        colorList = []
        for card in hand:
            colorList.append(card.color())
        return colorList