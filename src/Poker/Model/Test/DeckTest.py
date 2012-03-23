'''
DeckTest
Checks that Deck is behaving as it is supposed to.

@author: louhiran
'''
import unittest
from Poker.Model.Deck import Deck

class DeckTest(unittest.TestCase):

    def setUp(self):
        self.deck = Deck(2)

    def tearDown(self):
        del(self.deck)

    def test_DeckUsesCorrectColors(self):
        CardColors = ["CLUBS","DIAMONDS","HEARTS","SPADES"]
        self.assertEqual(Deck.COLORS, CardColors)

    def test_HasCorrectNumberOfCards(self):
        
        for color in Deck.COLORS:
            number = 0
            for card in self.deck:
                if card.color() == color:
                    number += 1
            self.assertEqual(number, 13)
        
        self.assertEqual(len(self.deck), 54)
        
    def test_DrawingReducesTheNumberOfCardsInTheDeck(self):
        numberOfCards = len(self.deck)
        self.deck.draw()
        self.assertEqual(len(self.deck), numberOfCards - 1)
            
    def test_DeckHasOnlyOneOfEachCard(self):
        self.deck = Deck(0)
        self.assertEqual(len(self.deck), 52)
        
        while len(self.deck):
            card = self.deck.draw()
            self.assertFalse(card in self.deck, "There were two cards that were the same.")

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()