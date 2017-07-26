"""MacGyver Class"""
from Entities import Entities

class MacGyver(Entities):
    """MacGyver entity"""
    def __init__(self, x, y):
        super(MacGyver, self).__init__(x, y)
        self.symbole = 'M'
        self.backpack = []

    def get_backpack(self):
        """Return backpack attribute"""
        return self.backpack

    def add_to_backpack(self, item):
        """Add item to the backpack attribute"""
        self.backpack.append(item)
