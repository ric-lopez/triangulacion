#-*- coding: utf-8 -*-
from poligono import Poligono
from punto import Punto
from arista import Arista
from grafica import Grafica

import math

class Triangulacion():

	
	def __init__(self, poligono):
		self.poligono = poligono
		self.triangulacion = Grafica()

	def triangular(self):
		poligono_orejon = self.poligono
		vertices = self.poligono.getVertices()
		#triangulacion = Grafica()
		con_orejas = True
		while con_orejas:
			oreja = self.get_oreja(poligono_orejon)
			if oreja == False:
				con_orejas = False
			else:
				self.remove_oreja(poligono_orejon, oreja[2])
				self.triangulacion.agregar_arista(oreja[1])
		return self.triangulacion

	# def triangular(self, poligono):
	# 	if len(poligono.getVertices()) == 3:
	# 		return self.triangulacion

	# 	else:
	# 		oreja = self.get_oreja(poligono)
	# 		if not(oreja):
	# 			print("ocurrio un error al obtener la oreja")
	# 			return self.triangulacion
	# 		self.triangulacion.agregar_arista(oreja[1])
	# 		poligono_orejon = self.remove_oreja(poligono, oreja[2])
	# 		if not(poligono_orejon):
	# 			print("ocurrio un error al remover la oreja")
	# 			return self.triangulacion
	# 		self.triangular(poligono_orejon)


	def get_oreja(self, poligono):
		t = Poligono()
		vertices = poligono.getVertices()
		es_oreja = True
		for v in vertices:
			v_i = poligono.anterior(v)
			v_j = poligono.siguiente(v)
			t.addV(v)
			t.addV(v_i)
			t.addV(v_j)

			if math.degrees(v.angulo(v_i, v_j)) >= 180:
				continue
			else:
				for u in vertices:
					if (u == v) or (u == v_i) or (u == v_j):
						continue

					if t.isInterior(u):
						es_oreja = False

				if es_oreja:
					return (t, Arista(v_i, v_j), v)
		return False


	def remove_oreja(self, poligono, v_oreja):
		print(v_oreja.toString())
		print(poligono.toString())
		poligono.removeV(v_oreja)
		return poligono
		# v_i = poligono.anterior(v_oreja)
		# v_j = poligono.siguiente(v_oreja)
		# d = Arista(v_i, v_j)
		# v = poligono.getVertices()
		# a = poligono.getAristas()
		# if v_oreja in v:
		# 	v = v.remove(v_oreja)
		# 	a = a.remove(d)
		# 	poligono.vertices = v
		# 	poligono.aristas = a
		# 	return poligono
		# else:
		# 	#print(v_oreja.toString())
		# 	#print(poligono.toString())
		# 	return False



