'''
PokerGladeUI
Loads the useriterface made with glade.
Connects all buttons with appropriate callbacks.

@author: louhiran
'''

import sys
try:
    import pygtk
    pygtk.require('2.0')
    import gtk
    import gtk.glade
except:
    sys.stderr.write("Required GUI classes could not be loaded.")
    sys.exit(1)

class PokerGladeUI(object):
    
    def __init__(self):
        '''Constructor'''
        
        self.gladefile = "Poker/View/PokerUI.glade"
        self.wTree = gtk.glade.XML(self.gladefile)

        self.window = self.wTree.get_widget("PokerUI")
        
        self._buttonBetUp = self.wTree.get_widget("buttonBetUp")
        self._buttonBetDown = self.wTree.get_widget("buttonBetDown")
        
        self._labelMoney = self.wTree.get_widget("labelMoney")
        self._labelBet = self.wTree.get_widget("labelBet")
        
        self._cards = [
                       self.wTree.get_widget("card1"),
                       self.wTree.get_widget("card2"),
                       self.wTree.get_widget("card3"),
                       self.wTree.get_widget("card4"),
                       self.wTree.get_widget("card5")
                       ]
        
        self._statusbar = self.wTree.get_widget("statusbar")
        
        dic = {
               "on_buttonDeal_clicked" : self._buttonDeal_click,
               "on_buttonBetUp_clicked" : self._buttonBetUp_click,
               "on_buttonBetDown_clicked" : self._buttonBetDown_click,
               "on_newGameMenuItem_activate" : self._newGame_click,
               "on_quitMenuItem_activate" : gtk.main_quit,
               "on_PokerUI_destroy" : gtk.main_quit
               }
        
        self.wTree.signal_autoconnect(dic)
        
        if self.window:
            self.window.connect("destroy", gtk.main_quit)
    
    def enableBetting(self):
        '''Enable bet -buttons.'''
        self._buttonBetUp.set_sensitive(True)
        self._buttonBetDown.set_sensitive(True)
    
    def disableBetting(self):
        '''Disable bet -buttons.'''
        self._buttonBetUp.set_sensitive(False)
        self._buttonBetDown.set_sensitive(False)
    
    def setController(self,controller):
        '''Set the controller of the UI.'''
        self._controller = controller
    
    def setMoney(self,money):
        '''Set the value of the moneylabel.'''
        self._labelMoney.set_text("Money: " + str(money) )
    
    def setBet(self,bet):
        '''Set the value of the betlabel.'''
        self._labelBet.set_text("Bet:" + str(bet) )
    
    def setStatus(self,status):
        '''Set the value of the statuslabel.'''
        self._statusbar.pop(1)
        self._statusbar.push(1,status)
        
    def getHoldedCards(self):
        '''Returns the places of cards that were held in list. Values are between 1-5'''
        holdedCards = []
        for x in xrange(5):
            if self._cards[x].get_active():
                holdedCards.append(x+1)
        return holdedCards
    
    def setCards(self,cards):
        '''Set the labels of the cards'''
        for x in xrange(5):
            self._cards[x].set_label(cards[x])
    
    def setCardsUnactive(self):
        '''Releases cards from hold'''
        for card in self._cards:
            card.set_active(False)
    
    def _buttonDeal_click(self, widget):
        '''Callback for dealbutton.''' 
        self._controller.dealClicked()   
    
    def _buttonBetUp_click(self,widget):
        '''Callback for buttonBetUp.'''
        self._controller.betUpByOne()
    
    def _buttonBetDown_click(self,widget):
        '''Callback for buttonBetDown.'''
        self._controller.betDownByOne()
    
    def _newGame_click(self,widget):
        '''Callback for newgame menuitem.'''
        self._controller.newGame()
        
    def main(self):
        gtk.main()
