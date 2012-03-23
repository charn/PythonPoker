'''
WinChecker
Checks that WinChecker is behaving as it is supposed to.

@author: louhiran
'''
import unittest
from Poker.Model.WinChecker import WinChecker
from Poker.Model.Hand import Hand
from Poker.Model.Card import Card

class WinCheckerTest(unittest.TestCase):

    def setUp(self):
        self.hand = Hand()
        self.winchecker = WinChecker(0)  

    def tearDown(self):
        del self.hand
        del self.winchecker


    def test_hasAPair(self):
        self.hand.add( Card("X",1) )
        self.hand.add( Card("Y",1) )
        self.hand.add( Card("Z",5) )
        self.hand.add( Card("X",7) )
        self.hand.add( Card("Y",9) )
        
        self.assertTrue( self.winchecker.hasAPair(self.hand) )

    def test_hasNotAPair(self):
        self.hand.add( Card("X",1) )
        self.hand.add( Card("Y",3) )
        self.hand.add( Card("Z",5) )
        self.hand.add( Card("X",7) )
        self.hand.add( Card("Y",9) )
        
        self.assertFalse( self.winchecker.hasAPair(self.hand) )

    def test_hasTwoPairs(self):
        self.hand.add( Card("X",1) )
        self.hand.add( Card("Y",5) )
        self.hand.add( Card("Z",3) )
        self.hand.add( Card("Z",5) )
        self.hand.add( Card("Z",1) )
        
        self.assertTrue( self.winchecker.hasTwoPairs(self.hand))
    
    def test_hasNotTwoPairs(self):
        self.hand.add( Card("X",1) )
        self.hand.add( Card("Y",1) )
        self.hand.add( Card("Z",5) )
        self.hand.add( Card("X",7) )
        self.hand.add( Card("Y",9) )
        
        self.assertFalse( self.winchecker.hasTwoPairs(self.hand) )
    
    def test_hasThreeOfAKind(self):
        self.hand.add( Card("X",13) )
        self.hand.add( Card("Y",1) )
        self.hand.add( Card("Z",5) )
        self.hand.add( Card("Y",13) )
        self.hand.add( Card("Z",13) )
        
        self.assertTrue( self.winchecker.hasThreeOfAKind(self.hand))

    def test_hasNotThreeOfAKind(self):
        self.hand.add( Card("X",1) )
        self.hand.add( Card("Y",1) )
        self.hand.add( Card("Z",5) )
        self.hand.add( Card("X",7) )
        self.hand.add( Card("Y",9) )
        
        self.assertFalse( self.winchecker.hasThreeOfAKind(self.hand) )
        
    def test_hasStraight(self):
        self.hand.add( Card("X",6) )
        self.hand.add( Card("Y",4) )
        self.hand.add( Card("Z",5) )
        self.hand.add( Card("Y",3) )
        self.hand.add( Card("Z",2) )
        
        self.assertTrue( self.winchecker.hasStraight(self.hand))

    def test_hasNotStraight(self):
        self.hand.add( Card("X",6) )
        self.hand.add( Card("Y",4) )
        self.hand.add( Card("Z",5) )
        self.hand.add( Card("Y",10) )
        self.hand.add( Card("Z",2) )
        
        self.assertFalse( self.winchecker.hasStraight(self.hand))

    def test_hasFlush(self):
        self.hand.add( Card("X",6) )
        self.hand.add( Card("X",4) )
        self.hand.add( Card("X",5) )
        self.hand.add( Card("X",10) )
        self.hand.add( Card("X",2) )
        
        self.assertTrue( self.winchecker.hasFlush(self.hand))

    def test_hasNotFlush(self):
        self.hand.add( Card("X",6) )
        self.hand.add( Card("X",4) )
        self.hand.add( Card("Y",5) )
        self.hand.add( Card("X",10) )
        self.hand.add( Card("X",2) )
        
        self.assertFalse( self.winchecker.hasFlush(self.hand))
        
    def test_hasFullHouse(self):
        self.hand.add( Card("X",3) )
        self.hand.add( Card("Y",6) )
        self.hand.add( Card("Z",3) )
        self.hand.add( Card("Y",6) )
        self.hand.add( Card("X",3) )
        
        self.assertTrue( self.winchecker.hasFullHouse(self.hand))

    def test_hasNotFullHouse(self):
        self.hand.add( Card("X",3) )
        self.hand.add( Card("Y",7) )
        self.hand.add( Card("Z",3) )
        self.hand.add( Card("Y",6) )
        self.hand.add( Card("X",3) )
        
        self.assertFalse( self.winchecker.hasFullHouse(self.hand))
        
    def test_hasFourOfAKind(self):
        self.hand.add( Card("X",3) )
        self.hand.add( Card("Y",6) )
        self.hand.add( Card("Z",3) )
        self.hand.add( Card("V",3) )
        self.hand.add( Card("X",3) )
        
        self.assertTrue( self.winchecker.hasFourOfAKind(self.hand))
    
    def test_hasNotFourOfAKind(self):
        self.hand.add( Card("X",3) )
        self.hand.add( Card("Y",6) )
        self.hand.add( Card("Z",3) )
        self.hand.add( Card("V",6) )
        self.hand.add( Card("X",3) )
        
        self.assertFalse( self.winchecker.hasFourOfAKind(self.hand))
        
    def test_hasStraightFlush(self):
        self.hand.add( Card("X",6) )
        self.hand.add( Card("X",4) )
        self.hand.add( Card("X",5) )
        self.hand.add( Card("X",3) )
        self.hand.add( Card("X",2) )
        
        self.assertTrue( self.winchecker.hasStraightFlush(self.hand))

    def test_hasNotStraightFlush_NotFlush(self):
        self.hand.add( Card("X",6) )
        self.hand.add( Card("X",4) )
        self.hand.add( Card("X",5) )
        self.hand.add( Card("Y",3) )
        self.hand.add( Card("X",2) )
        
        self.assertFalse( self.winchecker.hasStraightFlush(self.hand))

    def test_hasNotStraightFlush_NotStraight(self):
        self.hand.add( Card("X",6) )
        self.hand.add( Card("X",4) )
        self.hand.add( Card("X",10) )
        self.hand.add( Card("X",3) )
        self.hand.add( Card("X",2) )
        
        self.assertFalse( self.winchecker.hasStraightFlush(self.hand))


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()