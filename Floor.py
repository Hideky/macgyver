"""Floor Class"""

class Floor:
    """Representing a floor case"""
    instance = None
    class Floor:
        """Floor innerclass to create instance"""
        def __init__(self):
            self.symbole = ' '
        def __str__(self):
            return self.symbole
    def  __new__(cls):
        if not Floor.instance:
            Floor.instance = Floor.Floor()
        return Floor.instance
