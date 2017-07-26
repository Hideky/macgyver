"""Wall Class"""

class Wall:
    """Representing a wall case"""
    instance = None
    class Wall:
        """Wall innerclass to create instance"""
        def __init__(self):
            self.symbole = '*'
        def __str__(self):
            return self.symbole
    def  __new__(cls):
        if not Wall.instance:
            Wall.instance = Wall.Wall()
        return Wall.instance
