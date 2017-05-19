#-*- coding: utf-8 -*-
from poligono import Poligono
from punto import Punto
from arista import Arista
from segmento import Segmento
from grafica import Grafica
from dcel import DCEL
from nube_puntos import NubePosicionGeneral

import math

class Triangulacion():

	
	def __init__(self, poligono):
		self.poligono = poligono.copiar()
		self.triangulacion = Grafica()

	def triangular(self):
		poligono_orejon = self.poligono.copiar()
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

		for a in self.poligono.getAristas():
			self.triangulacion.agregar_arista(a)

		return self.triangulacion

	def por_pasos(self, poligono):
		orejon = poligono
		if len(orejon.getVertices()) <= 3:
			return False
		else:
			oreja = self.get_oreja(orejon)
			if oreja == False:
				print("no se encontraron mas orejas")
				return False
			else:
				orejon = self.remove_oreja(orejon, oreja[2])
				print("vertice oreja:"+oreja[2].toString())
				print("poligono orejon: ")
				print(orejon.toString())
				self.triangulacion.agregar_arista(oreja[1])
				delay(1000)
				return oreja[1]



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
			if poligono.getOrientacion() == 1:
				lado_interior = "der"
			else:
				lado_interior = "izq"

			if s.lado_p(v_j) == lado_interior or s.lado_p(v_j) == "col":
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


	def flip_diagonal(self):
		pass

class TriangulacionPuntos():
	"""Clase TriangulacionPuntos"""

	def __init__(self, nube):
		self.nube = nube
		self.triangulacion = Grafica()
		self.dcel_triangulacion = DCEL()

	def get_nube(self):
		return self.nube

	def get_dcel_triangulacion(self):
		return self.dcel_triangulacion

	def ordena_puntos(self):
		ordenados = sorted(self.nube.get_puntos(), key=lambda punto: punto.x)
		return ordenados

	def add_triangulo(self, v1, v2, v3):
		a1 = Arista(v1, v2)
		a2 = Arista(v2, v3)
		a3 = Arista(v3, v1)

		self.triangulacion.agregar_arista(a1)
		self.triangulacion.agregar_arista(a2)
		self.triangulacion.agregar_arista(a3)

	def triangular(self):
		ordenados = self.ordena_puntos()
		self.add_triangulo(ordenados[0], ordenados[1], ordenados[2])
		visitados = [ordenados[0], ordenados[1], ordenados[2]]
		for i in range(len(ordenados)-3):
			#print("--------------------------------------------")
			#print("punto: "+ordenados[i+3].toString())
			aristas_triang = self.triangulacion.get_aristas()
			for v in visitados:
				#print(self.triangulacion.toString())
				arista = Arista(ordenados[i+3], v)
				interseccion = False
				for a in aristas_triang:
					if arista.intersecta(a):
						#print(arista.toString()+" y "+a.toString()+" se intersectan")
						interseccion = True
					else:
						#print(arista.toString()+" y "+a.toString()+" no se intersectan")
						continue
				if not(interseccion):
					self.triangulacion.agregar_arista(arista)
			visitados.append(ordenados[i+3])

		self.dcel_triangulacion.construir(self.triangulacion)


	def flip_arista(self, a):
		pass






