from Entities import Entities

class Guardian(Entities):
	def __init__(self, x, y):
		super(Guardian, self).__init__(x,y)
		self.symbole = 'G'
	def checkMacGyver(self, macGyver):
		return True