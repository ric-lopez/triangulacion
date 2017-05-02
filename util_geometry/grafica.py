from punto import Punto
from arista import Arista

class Grafica():
	"""Clase Grafica."""

	def __init__(self):
		self.vertices = []
		self.aristas = []

	def get_vertices(self):
		return self.vertices

	def get_aristas(self):
		return self.aristas

	def agregar_arista(self, a):
		if a in self.aristas:
			return
		else:
			self.aristas.append(a)
			if not(a.getP1() in self.vertices):
				self.vertices.append(a.getP1())
			if not(a.getP2() in self.vertices):
				self.vertices.append(a.getP2())

	def toString(self):
		"""Regresa la representacion de una grafica como una cadena."""
		g = "["
		for e in self.aristas:
			g += e.toString()+","
		g += "]"
		return g