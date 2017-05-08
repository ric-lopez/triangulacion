#-*- coding: utf-8 -*-
from poligono import Poligono
from punto import Punto
from arista import Arista
from segmento import Segmento
from grafica import Grafica

import math

class Triangulacion():

	
	def __init__(self, poligono):
		self.poligono = poligono
		self.triangulacion = Grafica()

	def triangular(self):
		poligono_orejon = self.poligono
		print("poligono: "+poligono_orejon.toString())
		con_orejas = True
		while con_orejas and len(poligono_orejon.getVertices()) > 3:
			oreja = self.get_oreja(poligono_orejon)
			if oreja == False:
				print("no se encontraron mas orejas")
				con_orejas = False
			else:
				poligono_orejon = self.remove_oreja(poligono_orejon, oreja[2])
				print("vertice oreja:"+oreja[2].toString())
				print("poligono orejon: ")
				print(poligono_orejon.toString())
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
			t.limpiaPoligono()
			print("-------------------------------------------------------")
			print("analizando el vertice "+v.toString())
			v_i = poligono.anterior(v)
			v_j = poligono.siguiente(v)
			t.addV(v)
			t.addV(v_i)
			t.addV(v_j)
			t.cerrar()
			#print("v: "+v.toString()+" v_i: "+v_i.toString()+" v_j: "+v_j.toString())
			s = Segmento(v_i, v)
			if s.lado_p(v_j) == "der" or s.lado_p(v_j) == "col":
				continue
			else:
				v_restantes = vertices[:]
				v_restantes.remove(v)
				v_restantes.remove(v_i)
				v_restantes.remove(v_j)
				es_oreja = True
				for u in v_restantes:
					print(t.isInterior(u))
					if t.isInterior(u):
						print("el punto "+u.toString()+" esta en el interior interior del triangulo: "+t.toString()+"   :(")
						es_oreja = False

				if es_oreja:
					return (t, Arista(v_i, v_j), v)
		return False


	def remove_oreja(self, poligono, v_oreja):
 		poligono.removeV(v_oreja)
 		return poligono

