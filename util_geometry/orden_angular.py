import math
import random
from punto import Punto
from arista import Arista
#from avltree import *


class OrdenAngular():

	def __init__(self):
		#self.centro
		pass


	def ordena(self, s_direccion, s):
		"""Ordena angularmente el arregla de puntos 'a' tomando como referencia la recta 'recta_dir' """
		n = len(s)
		if(n > 1):
			m = (n//2)
			s1 = s[:m]
			s2 = s[m:]
			s1 = self.ordena(s_direccion, s1)
			s2 = self.ordena(s_direccion, s2)
			s = self.merge(s_direccion, s1, s2)
		return s


	def merge(self, s_direccion, a, b):
		""" Dados dos arreglos ordenados regresa un arreglo ordenado con la union de los datos"""
		n1 = len(a)-1
		n2 = len(b)-1
		p1 = 0
		p2 = 0
		r = []
		centro = s_direccion.get_inicio()
		while(p1<=n1 and p2<=n2):
			#if(p1 <= n1 and a[p1] <= b[p2]):
			if(p1 <= n1 and not(self.less(centro, a[p1].get_final(), b[p2].get_final()))):
				r.append(a[p1])
				p1 = p1 + 1
				if(p1>n1):
					while(p2<=n2):
						r.append(b[p2])
						p2 = p2 + 1
			elif(p2 <= n2 and self.less(centro, a[p1].get_final(), b[p2].get_final())):
				r.append(b[p2])
				p2 = p2 + 1
				if(p2>n2):
					while(p1<=n1):
						r.append(a[p1])
						p1 = p1 + 1
		#print(r)
		return r


	def less(self, center, a, b):
		if (a.get_x() - center.get_x() >= 0 and b.get_x() - center.get_x() < 0):
			return True
		if (a.get_x() - center.get_x() < 0 and b.get_x() - center.get_x() >= 0):
			return False
		if (a.get_x() - center.get_x() == 0 and b.get_x() - center.get_x() == 0):
			if (a.get_y() - center.get_y() >= 0 or b.get_y() - center.get_y() >= 0):
				return a.get_y() > b.get_y()
			return b.get_y() > a.get_y()


		# compute the cross product of vectors (center -> a) x (center -> b)
		det = (a.get_x() - center.get_x()) * (b.get_y() - center.get_y()) - (b.get_x() - center.get_x()) * (a.get_y() - center.get_y())
		if (det < 0):
			return True
		if (det > 0):
			return False

		# points a and b are on the same line from the center
		# check which point is closer to the center
		d1 = (a.get_x() - center.get_x()) * (a.get_x() - center.get_x()) + (a.get_y() - center.get_y()) * (a.get_y() - center.get_y())
		d2 = (b.get_x() - center.get_x()) * (b.get_x() - center.get_x()) + (b.get_y() - center.get_y()) * (b.get_y() - center.get_y())
		return d1 > d2
