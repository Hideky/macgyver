class Entities(object):
	def __init__(self, x, y):
		self.symbole = ''
		self.x = x
		self.y = y

	def getX(self):
		return self.x

	def getY(self):
		return self.y

	def setX(self, x):
		self.x = x

	def	setY(self, y):	
		self.y = y

	def __str__(self):
		return self.symbole