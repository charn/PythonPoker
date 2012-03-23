'''
GameController
Controller of the pokergame.

@author: louhiran
'''

from Poker.Model.Deck import Deck
from Poker.Model.WinChecker import WinChecker
from Poker.Model.Hand import Hand

class GameController(object):
    
    START_MONEY = 100
    START_BET = 1
    GAMESTATES = {
                  1 : "Choose bet and Deal.",
                  2 : "Choose cards you want to hold.",
                  3 : "Round ended.",
                  4 : "Ran out of money. GAME OVER."
                  }
    WINFACTORS = {
                  0 : "Has nothing.",
                  1 : "Has a pair.",
                  2 : "Has two pairs.",
                  3 : "Has three of a kind.",
                  4 : "Has straight.",
                  5 : "Has flush.",
                  6 : "Has full house.",
                  7 : "Has four of a kind.",
                  8 : "Has straight flush."
                  }
    
    def __init__(self, view):
        '''Constructor'''
        self._view = view
        self._winchecker = WinChecker(numberOfJokers = 0)
        self.newGame()
    
    def _drawAFullHand(self):
        '''Draw five cards from the deck to the hand.'''
        self._hand = Hand()
        for x in xrange(5):
            self._hand.add(self._deck.draw())

    def newGame(self):
        '''Set the game to a starting state'''
        self._setGamestate(1)
        self._setBet(self.START_BET)
        self._setMoney(self.START_MONEY)
        
        self._view.enableBetting()
        self._view.setCardsUnactive()
    
    def dealClicked(self):
        '''Things we do when deal -button is clicked. Action depends on the gamestate'''
        
        if self._gamestate == 3:
            self._setGamestate(1)
        
        if self._gamestate == 2:
            self._replaceNotHoldedCards()
            self._setUICards()
            self._view.setCardsUnactive()
            self._setMoney(self._money + self._bet * self._getHandWinFactor(self._hand))
            self._view.enableBetting()
            
            if self._money <= 0:
                #Ran out of money -> GAME OVER
                self._setGamestate(4)
            else:
                self._setGamestate(3)    
            
        elif self._gamestate == 1:
            
            if self._bet > self._money:
                self._setBet(self._money)
            
            self._view.disableBetting()
            self._view.setCardsUnactive()
            
            self._setMoney(self._money - self._bet)
            
            self._deck = Deck(0)
            self._drawAFullHand()
            
            self._setUICards()
            self._setGamestate(2)

    def betUpByOne(self):
        '''Increases the bet by one. Can't be greater than the money you have.'''
        if self._money > self._bet:
            self._setBet(self._bet + 1)
    
    def betDownByOne(self):
        '''Reduces the bet by one. Can't go below one'''
        if self._bet > 1:
            self._setBet(self._bet - 1)

    def _setMoney(self,money):
        '''Updates the money on the user interface and on the controllerobject itself.'''
        self._money = money
        self._view.setMoney(money)
    
    def _setBet(self,bet):
        '''Updates the bet on the user interface and on the controllerobject itself.'''
        self._bet = bet
        self._view.setBet(bet)

    def _replaceNotHoldedCards(self):
        '''Replaces the cards from the hand that are not marked as "held" in the userinterface.'''
        holdedCards = self._view.getHoldedCards()
        notHoldedCards = range(1,6)
        
        for card in holdedCards:
            notHoldedCards.remove(card)
        
        for place in notHoldedCards:
            self._hand.replace(place, self._deck.draw())
        
    def _setGamestate(self,gamestate):
        '''Update the gamestate on the controller and on the statusbar of the userinterface'''
        
        if gamestate > len(self.GAMESTATES) or gamestate < 1:
            raise SyntaxError("No such gamestate")
        
        self._gamestate = gamestate
        
        if gamestate == 1:
            self._view.setStatus(self.GAMESTATES.get(gamestate) )
        else:
            self._view.setStatus(self.GAMESTATES.get(gamestate) + " " +
                                 self.WINFACTORS.get(self._getHandWinFactor(self._hand)) )
    def _setUICards(self):
        '''Update the cards on the userinterface to resemble the cards in the hand.'''
        cardList = []
        
        for card in self._hand:
            cardList.append( str(card.color()) + "\n" + str(card.number()) )
        
        self._view.setCards(cardList)

    def _getHandWinFactor(self,hand):
        '''Check if the hand has winning combination of cards and return a winfactor for that win.'''
        if self._winchecker.hasStraightFlush(hand):
            return 8
        elif self._winchecker.hasFourOfAKind(hand):
            return 7
        elif self._winchecker.hasFullHouse(hand):
            return 6
        elif self._winchecker.hasFlush(hand):
            return 5
        elif self._winchecker.hasStraight(hand):
            return 4
        elif self._winchecker.hasThreeOfAKind(hand):
            return 3
        elif self._winchecker.hasTwoPairs(hand):
            return 2
        elif self._winchecker.hasAPair(hand):
            return 1
        else:
            return 0
