class Card(object):

    def __init__(self, color, number = 0):
        self._color = color
        self._number = number

    def __repr__(self):
        return (self._color, self._number)

    def __str__(self):
        return self._color + ":" + str(self._number)
    
    def __cmp__(self, other):
        '''Comparison is first made to the color and then to the number of the card'''
        
        if self.color() < other.color():
            return -1
        
        elif self.color() == other.color():
        
            if self.number() < other.number():
                return -1
            elif self.number() == other.number():
                return 0
            else:
                return 1
        else:
            return 1

    def color(self):
        return self._color

    def number(self):
        return self._number