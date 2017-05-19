from punto import Punto
from arista import Arista
from orden_angular import OrdenAngular

class Vertice():
	"""Clase Vertice"""

	def __init__(self, punto, semiarista):
		self.punto = punto
		self.semiarista = semiarista

	def __eq__(self, v):
		if(not isinstance(v, Vertice)):
			return False
		else:
			return self.punto == v.punto

	def get_punto(self):
		return self.punto

	def get_semiarista(self):
		return self.semiarista

	def get_x(self):
		return self.punto.getX()

	def get_y(self):
		return self.punto.getY()

	def to_string(self):
		return self.punto.toString()


class Cara():
	"""Clase Cara"""

	def __init__(self, etiqueta, c_interior, c_exterior):
		self.etiqueta = etiqueta
		self.c_interior = c_interior
		self.c_exterior = c_exterior
		
	def get_etiqueta(self):
		return self.etiqueta

	def get_c_interior(self):
		pass

	def get_c_exterior(self):
		pass

	def to_string(self):
		if self.c_interior == None:
			return "etiqueta: "+self.etiqueta+" , c_interior: None, c_exterior: "+self.c_exterior.c_string()
		elif self.c_exterior == None:
			return "etiqueta: "+self.etiqueta+" , c_interior: "+self.c_interior.c_string()+"c_exterior: None"



class Semiarista():
	"""Clase Semiarista"""
	
	def __init__(self, inicio, final, cara_incidente, siguiente, anterior):
		self.inicio = inicio
		self.final = final
		self.gemela = None
		self.cara_incidente = cara_incidente
		self.siguiente = siguiente
		self.anterior = anterior

	def __eq__(self, s):
		if(not isinstance(s, Semiarista)):
			return False
		else:
			if((self.inicio == s.inicio) and (self.final == s.final)):
				return True
			else:
				return False

	def get_inicio(self):
		return self.inicio

	def get_final(self):
		return self.final

	def get_siguiente(self):
		return self.siguiente

	def get_anterior(self):
		return self.anterior

	def c_string(self):
		return "["+self.inicio.to_string()+","+self.final.to_string()+"]"

	def to_string(self):
		if self.cara_incidente == None:
			return "semiarista: "+self.c_string()+", gemela: "+self.gemela.c_string()+", cara: None , anterior: "+self.anterior.c_string()+" , siguiente: "+self.siguiente.c_string()
		else:
			return "semiarista: "+self.c_string()+", gemela: "+self.gemela.c_string()+", cara: "+self.cara_incidente.get_etiqueta()+" , anterior: "+self.anterior.c_string()+" , siguiente: "+self.siguiente.c_string()
	

class DCEL():
	"""Clase DCEL."""

	def __init__(self):
		self.vertices = []
		self.semiaristas = []
		self.caras = []
		self.num_cara = 1

	def get_vertices(self):
		return self.vertices

	def get_semiaristas(self):
		return self.semiaristas

	def get_caras(self):
		return self.caras

	def limpiar(self):
		self.vertices = []
		self.semiaristas = []
		self.caras = []

	def es_vacia(self):
		return (len(self.vertices) == 0) and (len(self.semiaristas) == 0) and (len(self.caras) == 0)

	def add_vertice(self, v):
		if isinstance(v, Vertice):
			self.vertices.append(v)
			return True
		else:
			return False

	def add_semiarista(self, a):
		if isinstance(a, Semiarista):
			self.semiaristas.append(a)
			return True
		else:
			return False

	def add_cara(self, cara):
		if isinstance(cara, Cara):
			self.caras.append(cara)
			return True
		else:
			return False

	def remove_vertice(self, v):
		if v in self.vertices:
			self.vertices.remove(v)

	def remove_semiarista(self, a):
		if a in self.semiaristas:
			self.semiaristas.remove(a)

	def remove_cara(self, cara):
		if c in self.caras:
			self.caras.remove(cara)

	def is_in_vertices(self, v):
		punto = v.get_punto()
		for u in self.vertices:
			if punto == u.get_punto():
				return True
		return False


	def construir(self, grafica):
		# se cosntruyen las semiaristas y los vertices para la DCEL
		self.construye_semiaristas(grafica.get_aristas())

		# se construyen las caras de la DCEL
		self.construye_caras()


	def construye_semiaristas(self, aristas):
		
		for a in aristas:
			v_inicio = Vertice(a.getP1(), None)
			v_final = Vertice(a.getP2(), None)
			semi_a = Semiarista(v_inicio, v_final, None, None, None)
			if not(self.is_in_vertices(v_inicio)):
				self.add_vertice(v_inicio)
			
			twin_semi_a = Semiarista(v_final, v_inicio, None, None, None)
			if not(self.is_in_vertices(v_final)):
				self.add_vertice(v_final)

			semi_a.gemela = twin_semi_a
			twin_semi_a.gemela = semi_a
			self.add_semiarista(semi_a)
			self.add_semiarista(twin_semi_a)

		for a in self.semiaristas:
			self.ordena_semiaristas(a.get_inicio())


	def ordena_semiaristas(self, v_inicio):
		indicentes = []
		for a in self.semiaristas:
			if a.get_inicio().get_punto() == v_inicio.get_punto():
				indicentes.append(a)

		merge_sort = OrdenAngular()
		indicentes =  merge_sort.ordena(indicentes[0], indicentes)

		if len(indicentes) == 1:
			indicentes[i].gemela.siguiente = indicentes[i]
			indicentes[i].anterior = indicentes[i].gemela
		else:

			for i in range(len(indicentes)-1):
				indicentes[i].gemela.siguiente = indicentes[i+1]
				indicentes[i+1].anterior = indicentes[i].gemela

			indicentes[-1].gemela.siguiente = indicentes[0]
			indicentes[0].anterior = indicentes[-1].gemela

		v_inicio.semiarista = indicentes[0]

	#def get_semiaristas_incidentes(self, v):


	def construye_caras(self):
		semi_aristas = self.semiaristas[:]

		while semi_aristas:
			a = semi_aristas[0]
			a_cara = self.get_cara(a)
			orientacion = self.get_orientacion(a_cara)
			if orientacion == -1:
				cara = Cara(str(self.num_cara), None, a_cara[0])
				self.caras.append(cara)
				self.num_cara += 1
				for a in a_cara:
					a.cara_incidente = cara
					semi_aristas.remove(a)
			elif orientacion == 1:
				cara = Cara(str(self.num_cara), a_cara[0], None)
				self.caras.append(cara)
				self.num_cara += 1
				for a in a_cara:
					a.cara_incidente = cara
					semi_aristas.remove(a)

	def get_cara(self, a):
		inicio = a
		sig = a.get_siguiente()
		a_cara = [a]
		while inicio.get_inicio() != sig.get_inicio():
			a_cara.append(sig)
			sig = sig.get_siguiente()
			
		return a_cara

	def get_orientacion(self, aristas_cara):
		area = 0
		for a in aristas_cara:
			v = a.get_inicio()
			u = a.get_final()
			area += ((u.get_x()-v.get_x())*(u.get_y()+v.get_y()))
		if area > 0:
			return -1
		elif area < 0:
			return 1
		else:
			return 0


	def to_string(self):
		cadena = "Semiaristas: \n"
		for s in self.semiaristas:
			cadena += s.to_string()+"\n"

		cadena += "Caras: \n"
		for f in self.caras:
			cadena += f.to_string()+"\n"

		return cadena


# Alg: Construccion de una DCEL
# For each endpoint, 
# 	create a vertex. 

# For each input segment, 
# 	create two half-edges 
# 	and assign their tail vertices 
# 	and twins. 

# For each endpoint, 
# 	sort the half-edges whose tail vertex is that endpoint in clockwise order. 

	# 	For every pair of half-edges e1, e2 in clockwise order, 
	# 	assign e1->twin->next = e2 
	# 	and e2->prev = e1->twin. 
	# 	Pick one of the half-edges and assign it as the representative for the endpoint. 
	# 	(Degenerate case: if there's only one half-edge e in the sorted list, set e->twin->next = e and e->prev = e->twin. If you do things right, this won't require extra code.) 
	# 	The next pointers are a permutation on half-edges. 

# For every cycle, 
# 	allocate and assign a face structure.











