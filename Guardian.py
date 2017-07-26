"""Guardian Class"""
from Entities import Entities

class Guardian(Entities):
    """Guardian entity"""
    def __init__(self, x, y):
        super(Guardian, self).__init__(x, y)
        self.symbole = 'G'

    @classmethod
    def check_macgyver(cls, macgyver):
        """Check if MacGyver got 3 items"""
        if len(macgyver.get_backpack()) == 3:
            return True
        return False
