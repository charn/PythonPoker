'''
Pokergame

@author: louhiran
'''

from Poker.Controller.GameController import GameController
from Poker.View.PokerPyGtkUI import PokerGladeUI

def main():
    view = PokerGladeUI()
    controller = GameController(view)
    view.setController(controller)
    view.main()

if __name__ == '__main__':
    main()