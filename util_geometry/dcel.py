from punto import Punto


class Vertice():
	"""Clase Vertice"""

	def __init__(self, punto, semiarista):
		self.punto = punto
		self.semiarista = semiarista

	def get_punto(self):
		return self.punto

	def get_semiarista(self):
		return self.semiarista


class Cara():
	"""Clase Cara"""

	def __init__(self, etiqueta, c_interior, c_exterior):
		self.etiqueta = etiqueta
		self.c_interior = c_interior
		self.c_exterior = c_exterior
		
	def get_etiqueta(self):
		return self.etiqueta

	def get_c_interior(self):
		pass

	def get_c_exterior(self):
		pass


class Semiarista():
	"""Clase Semiarista"""
	
	def __init__(self, inicio, final, cara_incidente, siguiente, anterior):
		self.inicio = inicio
		self.final = final
		self.gemela = None
		self.cara_incidente = cara_incidente
		self.siguiente = siguiente
		self.anterior = anterior

	def get_inicio(self):
		return self.inicio

	def get_final(self):
		return self.final

	def get_siguiente(self):
		return self.siguiente

	def get_anterior(self):
		return self.anterior


class DCEL():
	"""Clase DCEL."""

	def __init__():