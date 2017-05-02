import math
import random
from punto import Punto
from arista import Arista
#from avltree import *


class RadialSort():

	def __init__(self):
		#self.centro
		pass

	def get_orden(self, recta_dir, a):
		""" Encapsula el metodo ordenar para regresar los puntos acomodados en el arreglo de la manera esperada """
		puntos_ordenados = self.ordena(recta_dir, a)
		return self.ubica_pto_inicio(recta_dir, puntos_ordenados)

	def ordena(self, recta_dir, a):
		"""Ordena angularmente el arregla de puntos 'a' tomando como referencia la recta 'recta_dir' """
		n = len(a)
		if(n > 1):
			m = (n//2)
			a1 = a[:m]
			a2 = a[m:]
			a1 = self.ordena(recta_dir, a1)
			a2 = self.ordena(recta_dir, a2)
			a = self.merge(recta_dir, a1, a2)
		return a


	def merge(self, recta_dir, a, b):
		""" Dados dos arreglos ordenados regresa un arreglo ordenado con la union de los datos"""
		n1 = len(a)-1
		n2 = len(b)-1
		p1 = 0
		p2 = 0
		r = []
		centro = recta_dir.a
		while(p1<=n1 and p2<=n2):
			#if(p1 <= n1 and a[p1] <= b[p2]):
			if(p1 <= n1 and not(self.less(centro, a[p1], b[p2]))):
				r.append(a[p1])
				p1 = p1 + 1
				if(p1>n1):
					while(p2<=n2):
						r.append(b[p2])
						p2 = p2 + 1
			elif(p2 <= n2 and self.less(centro, a[p1], b[p2])):
				r.append(b[p2])
				p2 = p2 + 1
				if(p2>n2):
					while(p1<=n1):
						r.append(a[p1])
						p1 = p1 + 1
		#print(r)
		return r


	def less(self, center, a, b):
		if (a.getX() - center.getX() >= 0 and b.getX() - center.getX() < 0):
			return True
		if (a.getX() - center.getX() < 0 and b.getX() - center.getX() >= 0):
			return False
		if (a.getX() - center.getX() == 0 and b.getX() - center.getX() == 0):
			if (a.getY() - center.getY() >= 0 or b.getY() - center.getY() >= 0):
				return a.getY() > b.getY()
			return b.getY() > a.getY()


		# compute the cross product of vectors (center -> a) x (center -> b)
		det = (a.getX() - center.getX()) * (b.getY() - center.getY()) - (b.getX() - center.getX()) * (a.getY() - center.getY())
		if (det < 0):
			return True
		if (det > 0):
			return False

		# points a and b are on the same line from the center
		# check which point is closer to the center
		d1 = (a.getX() - center.getX()) * (a.getX() - center.getX()) + (a.getY() - center.getY()) * (a.getY() - center.getY())
		d2 = (b.getX() - center.getX()) * (b.getX() - center.getX()) + (b.getY() - center.getY()) * (b.getY() - center.getY())
		return d1 > d2


	def ubica_pto_inicio(self, recta_dir, lista):
		''' '''
		# se crea una arista con los puntos que definen a recta_dir para utilizar el metodo lado_p_a_arista
		a = Arista(recta_dir.a, recta_dir.b)
		derecha = False
		re_ordenados = []
		i = 0
		for p in lista:
			if(a.lado_p_a_arista(p) == 'izq' and derecha):
				re_ordenados = lista[i:] + re_ordenados
				return re_ordenados
			else:
				if(a.lado_p_a_arista(p) == 'der'):
					derecha = True
				re_ordenados.append(p)
			i += 1
		return re_ordenados


	def arregla_orden(self, a, centro):
		''' Arregla el arreglo de puntos para que el vertice centro quede al inicio de arreglo '''
		for i in range(len(a)):
			if a[i] == centro:
				a.pop(i)
				a.append(centro)
				#b = self.invierte(a)
				#a = a[:0:-1]+[a[0]]

				return a


################################################################################################
## La clase RadiaslSort_Trig utiliza funciones trigonometricas para determinar el orden angular
## de los puntos 
##
## Nota: Utilizar funciones trigonometricas puede causar problemas de exactitud :(
################################################################################################

class RadialSort_Trig:
	
	def calcula_angulo(self, centro, p):
		''' calcula el angulo en radianes determinado por la recta "y = centro" y el segmento de recta determinada por "centro" y "p" '''
		v_r0 = (1,0)
		v_r1 = (p.getX()-centro.getX(), p.getY()-centro.getY())

		cosTheta = abs(v_r0[0]*v_r1[0] + v_r0[1]*v_r1[1]) / (math.sqrt(v_r0[0]*v_r0[0] + v_r0[1]*v_r0[1]) * math.sqrt(v_r1[0]*v_r1[0] + v_r1[1]*v_r1[1]))
		#print(cosTheta)
		return math.acos(cosTheta)


	def angulos(self, centro, puntos):
		''' recibe una lista de puntos y calcula los angulos formados por la recta "y = centro" y cada uno de los elementos de la lista "puntos" '''
		angulos = []
		for punto in puntos:
			angulos.append((self.calcula_angulo(centro, punto), punto))

		return angulos


	def ordena_angulos(self, angulos):
		''' orderna la lista de angulos de menor a mayor '''
		#angulos = sorted(angulos, key = )
		return sorted(angulos, key = lambda angulo: angulo[0])

	def angulos_ordenados(self, centro, puntos):
		''' calcula los angulos determinados por el "centro" y cada uno de los elementos de la lista "puntos", regresa una lista de tuplas (angulo, punto)
		ordenada de menor a mayor con respecto a la magnitud del angulo'''
		angulos = self.angulos(centro, puntos)
		angulos = self.ordenada_angulos(angulos)
		return angulos

	


if __name__=="__main__":
	
	radial = RadialSort()
	#centro = Punto(0,0)
	#punto = Punto(1,1)
	#angulo = radial.calcula_angulo(centro, punto)
	#print(angulo)
	'''
	puntos = []
	for i in range(10):
		puntos.append(Punto(random.random()*100, random.random()*100))

	print("puntos aleatorios")
	for p in puntos:
		print(p.toString())

	print("angulos y puntos")
	angulos = radial.angulos(puntos[0], puntos[1:])
	for a in angulos:
		print(a[0], a[1].toString())

	print("angulos ordernados")
	angulos = radial.ordena_angulos(angulos)
	for a in angulos:
		print(a[0], a[1].toString())
	'''
	#puntos poligono simple
	#puntos = [Punto(1,3), Punto(3,7), Punto(3,1), Punto(1,6), Punto(4,3), Punto(6,4)]
	#puntos poligono ortogonal
	#puntos = [Punto(12,4), Punto(16,4), Punto(16,8), Punto(4,8), Punto(4,4), Punto(8,4), Punto(8,6), Punto(12,6)]
	puntos = [Punto(3,0),Punto(3,3),Punto(0,0),Punto(0,3), Punto(3,2)]
	centro = Punto(2,-1)
	print("orden generado:")
	ordenados = radial.ordena(puntos, centro)
	for p in ordenados:
		print(p.toString())
	
	#print("orden arreglado:")
	#arreglados = radial.arregla_orden(ordenados, centro)
	#for p in arreglados:
	#	print(p.toString())
