#-*- coding: utf-8 -*-
from punto import Punto
from arista import Arista
from poligono import Poligono

class PoligonoSimple(Poligono):
	"""Poligonos simples: Poligonos que no permiten intersecciones en sus aristas"""

	def addVertice(self, v):
		'''agrega un vertice nuevo a la lista de vertices del poligono'''
		if self.checaInterseccion(v):
			return False
		else:
			if self.esVacio():
				self.vertices = self.vertices + [v]
			else:	
				self.aristas = self.aristas + [Arista(self.vertices[-1],v)]
				self.vertices = self.vertices + [v]
			return True

	def addVertice_XY(self, x1, y1):
		'''agrega un vertice nuevo, a partir de sus coordenadas x, y, a la lista de vertices del poligono'''
		v = Punto(x1, y1)
		if self.checaInterseccion(v):
			return False
		else:		
			if self.esVacio():
				self.vertices = self.vertices + [Punto(x1, y1)]
			elif self.cierraPoligono(v):
				self.aristas = self.aristas + [Arista(self.vertices[-1], self.vertices[0])]
			else:	
				self.aristas = self.aristas + [Arista(self.vertices[-1], Punto(x1, y1))]
				self.vertices = self.vertices + [Punto(x1, y1)]
			return True

	def addVertice_i(self, x, y, i):
		"""Sobreescribe el vertice en la posicion i por el creado con las coordenadas x, y """
		if i >= len(self.vertices) or i<0:
			return False
		v = Punto(x, y)
		print(i)

		if self.cerrado:
			if i == 0:
				a1 = Arista(self.vertices[-1], v)
				a2 = Arista(v, self.vertices[1])
			elif i == len(self.vertices)-1:
				a1 = Arista(self.vertices[i-1], v)
				a2 = Arista(v, self.vertices[0])
			else:
				a1 = Arista(self.vertices[i-1], v)
				a2 = Arista(v, self.vertices[i+1])
			aristas_tmp = self.aristas[:]
			self.aristas[i-1] = a1
			self.aristas[i] = a2
		
			if self.checaInterseccionArista(a1) or self.checaInterseccionArista(a2):
				self.aristas = aristas_tmp
				return False
			else:
				self.vertices[i] = v
				return True
		else:
			aristas_tmp = self.aristas[:]
			if i == 0:
				#a1 = Arista(self.vertices[-1], v)
				a = Arista(v, self.vertices[1])
				self.aristas[i] = a
				if self.checaInterseccionArista(a):
					self.aristas = aristas_tmp
					return False
				else:
					self.vertices[i] = v
					return True

			elif i == len(self.vertices)-1:
				a = Arista(self.vertices[i-1], v)
				self.aristas[-1] = a
				if self.checaInterseccionArista(a):
					self.aristas = aristas_tmp
					return False
				else:
					self.vertices[-1] = v
					return True
			else:
				a1 = Arista(self.vertices[i-1], v)
				a2 = Arista(v, self.vertices[i+1])
			
				self.aristas[i-1] = a1
				self.aristas[i] = a2
		
				if self.checaInterseccionArista(a1) or self.checaInterseccionArista(a2):
					self.aristas = aristas_tmp
					return False
				else:
					self.vertices[i] = v
					return True



	def area(self):
		'''calcula el area del poligono'''
		pass

	def interseccion(self, p):
		'''calcula la interseccion de dos poligos'''
		pass