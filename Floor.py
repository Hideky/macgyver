# Use of singleton to save memory usage
class Floor:
	instance = None
	class Floor:
		def __init__(self):
			self.symbole = ' '
		def __str__(self):
			return self.symbole
	def  __new__(cls):
		if not Floor.instance:
			Floor.instance = Floor.Floor()
		return Floor.instance