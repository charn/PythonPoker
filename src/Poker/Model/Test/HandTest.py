'''
HandTest
Checks that Hand is behaving as it is supposed to.

@author: louhiran
'''
import unittest
from Poker.Model.Hand import Hand
from Poker.Model.Deck import Deck

class HandTest(unittest.TestCase):


    def setUp(self):
        self.hand = Hand()
        self.deck = Deck()


    def tearDown(self):
        del self.hand
        del self.deck

    def test_NewHandIsEmpty(self):
        self.assertEqual(self.hand.getCards(), [])

    def test_CanAddFiveCardToTheHand(self):
        for i in xrange(5):
            self.hand.add(self.deck.draw())
            
    def test_AddingSixCardsCausesException(self):
        for i in xrange(5):
            self.hand.add(self.deck.draw())
        self.assertRaises(Exception,self.hand.add,self.deck.draw())
        
    def test_HandContainsTheCardThatWasAdded(self):
        card = self.deck.draw()
        self.hand.add(card)
        self.assertTrue(card in self.hand)
        
    def test_getCards(self):
        cards = []
        for i in xrange(5):
            cards.append(self.deck.draw())
        
        for card in cards:
            self.hand.add(card)
        
        for card in cards:
            self.assertTrue(card in self.hand.getCards())
            
        self.assertEqual(len(self.hand.getCards()), 5)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()