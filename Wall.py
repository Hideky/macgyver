# Use of singleton to save memory usage
class Wall:
	instance = None
	class Wall:
		def __init__(self):
			self.symbole = '*'
		def __str__(self):
			return self.symbole
	def  __new__(cls):
		if not Wall.instance:
			Wall.instance = Wall.Wall()
		return Wall.instance