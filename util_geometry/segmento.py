#-*- coding: utf-8 -*-
from punto import Punto

class Segmento():

	def __init__(self, pi, pf):
		self.pi = pi
		self.pf = pf

	def __eq__(self, s):
		if(not isinstance(s, Segmento)):
			return False
		else:
			if((self.pi == s.pi) and (self.pf == s.pf)):
				return True
			else:
				return False

	def get_pi(self):
		"""Regresa el elemento 'pi' de la arista"""
		return self.pi

	def get_pf(self):
		"""Regresa el elemento 'pf' de la arista"""
		return self.pf

	def longitud(self):
		"""Calcula la longitud del objeto Segmento que llama al metodo"""
		return self.pi.distancia(self.pf)

	def puntoMedio(self):
 		"""Calcula el punto medio del segmento"""
 		return Punto((self.pi.getX()+self.pf.getX())/2, (self.pi.getY()+self.pf.getY())/2)

	def lado_p(self, p):
		"""Determina de que lado se encuentra el punto 'p' con respecto al segmento"""
		area = (self.pf.getX()-self.pi.getX())*(p.getY()- self.pi.getY())-(p.getX()-self.pi.getX())*(self.pf.getY()-self.pi.getY())
		if (area > 0):
			lado = "izq"
		elif (area < 0):
			lado = "der"
		else:
			lado = "col"
		return lado

	def intersecta(self, s):
		"""Determina si dos aristas se intersectan o no"""
		if (self.lado_p(self.pi, self.pf, s.pi) == "col" or
			self.lado_p(self.pi, self.pf, s.pf) == "col" or
			self.lado_p(s.pi, s.pf, self.pi) == "col" or
			self.lado_p(s.pi, s.pf, self.pf) == "col"):
			return False
		elif (((self.lado_p(self.pi, self.pf, s.pi) == "izq" and
			self.lado_p(self.pi, self.pf, s.pf) == "der") or
 			(self.lado_p(self.pi, self.pf, s.pi) == "der" and
 			self.lado_p(self.pi, self.pf, s.pf) == "izq")) and
 			((self.lado_p(s.pi, s.pf, self.pi) == "der" and
 			self.lado_p(s.pi, s.pf, self.pf) == "izq") or
 			(self.lado_p(s.pi, s.pf, self.pi) == "izq" and
 			self.lado_p(s.pi, s.pf, self.pf) == "der"))):
 			return True
 		else:
 			return False

	def toString(self):
		"""Regresa la representacion de un segmento como una cadena con el formato: [(x1, y1), (x2, y2)]"""
		return "["+self.pi.toString()+","+self.pf.toString()+"]"

