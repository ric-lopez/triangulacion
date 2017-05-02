#-*- coding: utf-8 -*-
from punto import Punto
from arista import Arista
from recta import Recta

class Poligono():
	"""Clase Poligono"""

	def __init__(self):
		'''constructor vacio de la clase Poligono, inicializa las listas de vertices y aristas como listas vacias'''
		self.vertices = []
		self.aristas = []
		self.cerrado = False
		self.orientacion = None

	def siguiente(self, v):
		if v in self.vertices:
			indice = self.vertices.index(v)
			if indice == len(self.vertices)-1:
				return self.vertices[0]
			else:
				return self.vertices[indice+1]
		else:
			return False

	def anterior(self, v):
		if v in self.vertices:
			indice = self.vertices.index(v)
			if indice == 0:
				return self.vertices[-1]
			else:
				return self.vertices[indice-1]
		else:
			return False

	def arista_siguiente(self, a):
		if a in self.aristas:
			indice = self.getAristas().index(a)
			if indice == len(self.aristas)-1:
				return self.aristas[0]
			else:
				return self.aristas[indice+1]
		else:
			return False

	def arista_anterior(self, a):
		if a in self.aristas:
			indice = self.getAristas().index(a)
			if indice == 0:
				return self.aristas[-1]
			else:
				return self.aristas[indice-1]
		else:
			return False

	def getAristasIncidentes(self, v):
		'''Regresa las aristas que incide el vertice v '''
		a = (Arista(self.anterior(v), v), Arista(v, self.siguiente(v)))
		return a


	def getPuntoL(self, v):
		u = self.anterior(v)
		v = self.siguiente(v)

		distancia = 1000

		deltaX1 = u.getX() - p.getX()
		deltaY1 = u.getY() - p.getY()

		deltaX2 = v.getX() - p.getX()
		deltaY2 = v.getY() - p.getY()


	def esVacio(self):
		'''checa si el poligono es vacio, si la lista de vertices es vacia'''
		if self.vertices == []:
			return True
		else:
			return False	

	def aristasEsVacio(self):
		'''checa si la lista de aristas es vacia'''
		if self.aristas == []:
			return True
		else:
			return False		
		
	def getAristas(self):
		'''regresa la lista de aristas del poligono'''
		return self.aristas

	def getVertices(self):
		'''regresa la lista de vertices del poligono'''
		return self.vertices

	def toString(self):
		'''regresa la lista de vertices como una cadena'''
		poligono = "["
		for v in self.vertices:
			if isinstance(v, Punto):
				poligono = poligono + v.toString()
			else:
				poligono = poligono + str(v)
		poligono = poligono + "]"
		return poligono

	def aristasToString(self):
		'''regresa la lista de aristas como una cadena'''
		poligono = "["
		for a in self.aristas:
			poligono = poligono + a.toString()
		poligono = poligono + "]"

		return poligono		

	def aplanaVertices(self):
		'''Regresa la lista de vertices como una lista plana'''
		verticesAplanados = []
		for v in self.vertices:
			verticesAplanados = verticesAplanados + [v.getX(), v.getY()]
		return verticesAplanados

	def limpiaPoligono(self):
		self.vertices = []
		self.aristas = []
		self.cerrado = False

	def checaInterseccion(self, v):
		'''checa si la nueva arista construida con el vertice v intersecta a las aristas ya definidas'''
		if self.esVacio():
			return False
		else:
			b = Arista(self.vertices[-1], v)
			for a in self.aristas:
				if a.intersecta(b):
					print("interseccion")
					return True
			return False

	def checaInterseccionArista(self, a):
		'''checa si la nueva arista 'a' intersecta a las aristas ya definidas'''
		if self.aristasEsVacio():
			return False
		else:
			for arista in self.aristas:
				if arista.intersecta(a):
					print("interseccion")
					return True
			return False

	def addV(self, v):
		'''Inserta un vertice en el poligono sin hacer ninguna verificacion'''
		if self.esVacio():
			self.vertices = self.vertices + [v]
		else:	
			self.aristas = self.aristas + [Arista(self.vertices[-1],v)]
			self.vertices = self.vertices + [v]

	def removeV(self, v):
		siguiente = self.siguiente(v)
		anterior = self.anterior(v)
		self.vertices.remove(v)
		#if self.orientacion == 1:
		self.aristas.remove(Arista(v, siguiente))
		self.aristas.remove(Arista(anterior, v))
		self.aristas.append(Arista(anterior, siguiente))

	def pop(self):
		'''Elimina el ultimo vertice agregado y la arista que incide'''
		#u = self.vertices[-1]
		self.vertices = self.vertices[:-1]
		self.aristas = self.aristas[:-1]

	def cerrar(self):
		'''Cierra el poligono uniendo el primer y el ultimo vertice'''
		self.aristas = self.aristas + [Arista(self.vertices[-1],self.vertices[0])]
		self.cerrado = True
		self.calculaOrientacion()

	def cierraPoligono(self, v):
		'''verifica el vertice v cierra el poligono'''
		if len(self.vertices) < 3:
			return False

		v_i = self.vertices[0]
		x1 = v_i.getX()-20
		x2 = v_i.getX()+20
		y1 = v_i.getY()-20
		y2 = v_i.getY()+20
		
		if (v.getX() >= x1) and (v.getX() <= x2) and (v.getY() >= y1) and (v.getY() <=y2):
			self.cerrado = True
			self.calculaOrientacion()
			return True
		else:
			return False

	def esMonotono(self, v_izq, v_der):
		"""Verifica si el poligono es Monotono con respecto al eje 'X' """
		v_aux = v_izq
		while v_aux != v_der:
			if(v_aux.getX() > self.siguiente(v_aux)):
				return False
		v_aux = v_der
		while v_aux != v_izq:
			if(v_aux.getX() > self.siguiente(v_aux)):
				return False
		return True

	def getVConvexo(self):
		'''Determina un vertice convexo en P, un vertice convexo es aquel cuyo angulo interior es menor o igual a 180 grados'''
		
		for v in self.vertices:
			u = self.siguiente(v)
			w = self.anterior(v)
			a = Arista(w, v)
			if a.lado_p_arista(u) == 'der':
				return v

		return False


	def calculaOrientacion(self):
		'''Determina la orientacion del poligono, asigna el valor de 1 si es postiva (antihorario) o -1 si es negativa (horario)
		al atributo orientacion'''
		if self.cerrado:
			area = 0
			for v in self.vertices:
				u = self.siguiente(v)
				area += ((u.getX()-v.getX())*(u.getY()+v.getY()))
			if area > 0:
				self.orientacion = -1
				#return -1
			elif area < 0:
				self.orientacion = 1
				#return 1
			else:
				self.orientacion = 0
				#return 0

	def getOrientacion(self):
		'''Regresa el valor del atributo orientacion'''
		return self.orientacion

	def isInterior(self, p):
		'''Determina si el punto p se encuentra en el interior del poligono que llama al metodo '''
		aristas = self.getAristas()
		r = Recta(p, Punto(p.getX()+1, p.getY()))
		count = 0
		for arista in aristas:
			p_i = r.interseccion_segm(arista)
			if(p_i != False):
				if(p_i.getX() >= p.getX()):
					#print("se cuenta interseccion con: "+arista.toString())
					count +=1
		#print("count: "+str(count))
		if (count % 2) == 0:
			return False
		else:
			return True 


	def getCajaContenedora(self):
		'''Calcula el rectangulo ortogonal que contiene al poligono'''
		p_x_min = self.vertices[0]
		p_x_max = self.vertices[0] 
		p_y_min = self.vertices[0]
		p_y_max = self.vertices[0]

		for p in self.vertices:
			if(p_x_min.getX() > p.getX()):
				p_x_min = p
			if(p_x_max.getX() < p.getX()):
				p_x_max = p
			if(p_y_min.getY() > p.getY()):
				p_y_min = p
			if(p_y_max.getY() < p.getY()):
				p_y_max = p

		#eps = epsilon()
		p_ar_i = Punto(p_x_min.getX()-10, p_y_max.getY()+10)
		p_ar_d = Punto(p_x_max.getX()+10, p_y_max.getY()+10)
		p_ab_i = Punto(p_x_min.getX()-10, p_y_min.getY()-10)
		p_ab_d = Punto(p_x_max.getX()+10, p_y_min.getY()-10)

		caja = Poligono()
		caja.addV(p_ab_i)
		caja.addV(p_ab_d)
		caja.addV(p_ar_d)
		caja.addV(p_ar_i)
		caja.cerrar()

		return caja



