#-*- coding: utf-8 -*-
#import numpy
import math

class Punto:
	"""
	Clase Punto.

	La clase punto ...

	Atributos:
		x: Valor de la coordenada x.
		y: Valor de la coordenada y.
	"""
	def __init__(self, ordenada, abcisa):
		"""Crea un objeto Punto, con los valores de ordenada y abcisa asignados."""	
		self.x = float(ordenada)
		self.y = float(abcisa)
	
	def __eq__(self, p):
		""" Compara si dos objetos punto son iguales."""
		if(not isinstance(p, Punto)):
			return False
		else:
			if((self.x == p.x) and (self.y == p.y)):
				return True
			else:
				return False

	def getX(self):
		"""Regresa la coordenada 'x' del punto."""
		return self.x

	def getY(self):
		"""Regresa la coordenada 'y' del punto."""
		return self.y

	def suma(self, p):
		"""
		Calcula la suma de dos puntos: (x1 + x2, y1 + y2).

		Args:
			p: Punto a sumar.

		Returns:
			Objeto Punto, resultado de la suma de p y el objeto que llama al metodo.
		"""
		return Punto(self.x+p.x, self.y+p.y)

	def resta(self, p):
		"""
		Calcula la resta de dos puntos: (x1 - x2, y1 - y2).

		Args:
			p: Punto a restar.

		Retruns:
			Objeto Punto, resultado de la resta del objeto que llama al metodo y p.
		"""
		return Punto(self.x-p.x, self.y-p.y)

	def distancia(self, p):
		"""Calcula la distacia euclidiana entre el punto que llama al metodo y el punto 'p' que recibe."""
		return math.sqrt(abs(self.x-p.x)**2 + abs(self.y-p.y)**2)

	def compara(self, p):
		"""compara p1 con p2: regresa 0 si p1 = p2, 1 si p1 > p2, -1 si p1 < p2."""
		if self.x < p.x:
			return -1
		elif self.x == p.x and self.y < p.y:
			return  -1
		elif self.x == p.x and self.y == p.y:
			return 0
		else:
			return 1

	def determinante(self, p):
		return (self.x * p.y)-(self.y * p.x)

	def rotar(self, origen, angulo):
		"""Rota el punto que llama al metodo sobre el punto origen"""
		ox = origen.getX()
		oy = origen.getY()
		px = self.getX()
		py = self.getY()
		qx = ox + math.cos(angulo) * (px - ox) - math.sin(angulo) * (py - oy)
		qy = oy + math.sin(angulo) * (px - ox) + math.cos(angulo) * (py - oy)
		return Punto(qx, qy)

	# def angulo(self, p1, p2):
	# 	"""Calcula el angulo formado por el punto que llama el metodo y las puntos p1 y p2"""
	# 	v1 = (p1.x - self.x, p1.y - self.y)
	# 	v2 = (p2.x - self.x, p2.y - self.y)

	# 	coseno = math.fabs(v1[0]*v2[0] + v1[1]*v2[1]) / (math.sqrt(v1[0]*v1[0] + v1[1]*v1[1]) * math.sqrt(v2[0]*v2[0] + v2[1]*v2[1]))
	# 	angulo = math.acos(coseno)
	# 	return angulo

	def toString(self):
		"""Regresa el punto como objeto tipo cadena"""
		return "({:0.2f}, {:0.2f})".format(self.x, self.y)
		#return "("+str(self.x)+","+str(self.y)+")"

	def printPunto(self):
		"""Imprime el punto en la salida estandar"""
		print (self.toString())