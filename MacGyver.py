from Entities import Entities

class MacGyver(Entities):
	def __init__(self, x, y):
		super(MacGyver, self).__init__(x,y)
		self.symbole = 'M'
		self.backpack = []

	def getBackpack():
		return self.backpack

	def addToBackpack(item):
		self.backpack.append(item)	