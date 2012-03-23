'''
CardTest
Checks that the card is working as it is supposed to.

@author: louhiran
'''
import unittest
from Poker.Model.Card import Card

class CardTest(unittest.TestCase):


    def setUp(self):
        self.card = Card("COLOR",13)


    def tearDown(self):
        del(self.card)


    def test_CardColorIsSetCorrectly(self):
        self.assertEqual(self.card.color(),"COLOR")

    def test_CardNumberIsSetCorrectly(self):
        self.assertEqual(self.card.number(), 13)
        
    def test_CardsAreEqualIfTheyHaveTheSameColorAndNumber(self):
        
        c1 = Card("A",1)
        c2 = Card("B",2)
        
        self.assertNotEqual(c1,c2, "Cards were not the same")
        c2 = Card("B",1)
        self.assertNotEqual(c1,c2, "Cards were not the same")
        c2 = Card("A",2)
        self.assertNotEqual(c1,c2, "Cards were not the same")
        c2 = Card("A",1)
        self.assertEqual(c1,c2, "Cards were the same")
    

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()