"""Items Class"""
from Entities import Entities

class Items(Entities):
    """Items Entity"""
    def __init__(self, x, y, symbole):
        super(Items, self).__init__(x, y)
        self.symbole = symbole
        