
class Evento:

	def __init__(self, p, t, k_i):
		self.punto = p
		self.tipo = t
		self.k_i = k_i

	def set_punto(self, p):
		self.punto = p

	def set_tipo(self, t):
		self.tipo = t

	def set_k_i(self, k_i):
		self.k_i = k_i

	def get_punto(self):
		return self.punto

	def get_tipo(self):
		return self.tipo

	def get_k_i(self):
		return self.k_i

	def toString(self):
		return "punto: "+self.punto.toString()+", tipo: "+self.tipo+", k: "+str(self.k_i)
