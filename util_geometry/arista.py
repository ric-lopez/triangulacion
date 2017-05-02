#-*- coding: utf-8 -*-
import math
from punto import Punto

class Arista:
	"""Clase Arista"""
	def __init__(self, p1, p2):
		self.p1 = p1
		self.p2 = p2

	def __eq__(self, a):
		if(not isinstance(a, Arista)):
			return False
		else:
			if((self.p1 == a.p1) and (self.p2 == a.p2)):
				return True
			else:
				return False
	
	def getP1(self):
		"""Regresa el elemento 'p1' de la arista"""
		return self.p1

	def getP2(self):
		"""Regresa el elemento 'p2' de la arista"""
		return self.p2

	def longitud(self):
		"""Calcula la longitud del objeto Arista que llama al metodo"""
		return self.p1.distancia(self.p2)

	def menor(self):
		"""Regresa el menor de los vertices que forman la arista, utiliza el metodo compara de la clase Punto"""
		if(self.p1.compara(self.p2) == 1):
			return self.p2
		else:
			return self.p1

	def mayor(self):
		"""Regresa el mayor de los vertices que forman la arista, utiliza el metodo compara de la clase Punto"""
		if(self.p1.compara(self.p2) == -1):
			return self.p2
		else:
			return self.p1		

	def lado_p_a_segmento(self, v1, v2, p):
		"""Determina de que lado se encuentra el punto 'p' con respecto a la arista (v1, v2)"""
		area = (v2.getX()-v1.getX())*(p.getY()- v1.getY())-(p.getX()-v1.getX())*(v2.getY()-v1.getY())
		if (area > 0):
			lado = "izq"
		elif (area < 0):
			lado = "der"
		else:
			lado = "col"
		return lado

	def lado_p_a_arista(self, p):
		"""Determina de que lado se encuentra el punto 'p' con respecto a la arista que usa el metodo, la arista
		se toma como un segmento dirigido p1 -> p2 """
		area = (self.p2.getX()-self.p1.getX())*(p.getY()- self.p1.getY())-(p.getX()-self.p1.getX())*(self.p2.getY()-self.p1.getY())
		if (area > 0):
			lado = "izq"
		elif (area < 0):
			lado = "der"
		else:
			lado = "col"
		return lado

	def intersecta(self, a):
		"""Determina si dos aristas se intersectan o no"""
		if (self.lado_p_a_segmento(self.p1, self.p2, a.p1) == "col" or
			self.lado_p_a_segmento(self.p1, self.p2, a.p2) == "col" or
			self.lado_p_a_segmento(a.p1, a.p2, self.p1) == "col" or
			self.lado_p_a_segmento(a.p1, a.p2, self.p2) == "col"):
			return False
		elif (((self.lado_p_a_segmento(self.p1, self.p2, a.p1) == "izq" and
			self.lado_p_a_segmento(self.p1, self.p2, a.p2) == "der") or
 			(self.lado_p_a_segmento(self.p1, self.p2, a.p1) == "der" and
 			self.lado_p_a_segmento(self.p1, self.p2, a.p2) == "izq")) and
 			((self.lado_p_a_segmento(a.p1, a.p2, self.p1) == "der" and
 			self.lado_p_a_segmento(a.p1, a.p2, self.p2) == "izq") or
 			(self.lado_p_a_segmento(a.p1, a.p2, self.p1) == "izq" and
 			self.lado_p_a_segmento(a.p1, a.p2, self.p2) == "der"))):
 			return True
 		else:
 			return False

 	def puntoMedio(self):
 		"""Calcula el punto medio de la arista"""
 		return Punto((self.p1.getX()+self.p2.getX())/2, (self.p1.getY()+self.p2.getY())/2)

 	def swap_puntos(self):
 		"""Invierte el orden de los puntos que forman la arista (p1, p2) => (p2, p1)"""
 		return Arista(self.p2, self.p1)

 	def puntoEnArista(self, p):
 		""" Determina si el punto 'p' esta contenido en la arista que llama al metodo"""
 		pass

 	def toString(self):
		"""Regresa la representacion de una arista como una cadena con el formato: [(x1, y1), (x2, y2)]"""
		return "["+self.p1.toString()+","+self.p2.toString()+"]"

	def printArista(self):
		"""Imprime en la salida estandar el objeto Arista que llama al metodo"""
		print self.toString()