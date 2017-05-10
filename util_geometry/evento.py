
class Evento:

	def __init__(self, p, t):
		self.punto = p
		self.tipo = t

	def set_punto(self, p):
		self.punto = p

	def set_tipo(self, t):
		self.tipo = t

	def get_punto(self):
		return self.punto

	def get_tipo(self):
		return self.tipo

	def toString(self):
		return "punto: "+self.punto.toString()+", tipo: "+self.tipo+", k: "+str(self.k_i)
