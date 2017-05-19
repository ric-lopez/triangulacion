from util_geometry.grafica import Grafica
from util_geometry.punto import Punto
from util_geometry.arista import Arista
from util_geometry.poligonoSimple import PoligonoSimple
from util_geometry.triangulacion import Triangulacion, TriangulacionPuntos
from util_geometry.nube_puntos import NubePosicionGeneral

from util_geometry.dcel import DCEL

class Interfaz():

	def __init__(self, grafica, ancho, alto):
		self.grafica = grafica
		self.ancho = ancho
		self.alto = alto

	def draw_grafica(self, grafica):
		aristas = grafica.get_aristas()
		for a in aristas:
			u = a.getP1()
			v = a.getP2()
			f = createFont("Arial",16,True)
			textFont(f)
			text(u.toString(), u.getX(), self.alto-u.getY())
			line(u.getX(), self.alto-u.getY(), v.getX(), self.alto-v.getY())

	def draw_linea(self, p1, p2):
		line(p1.getX(), self.alto-p1.getY(), p2.getX(), self.alto-p2.getY())

	def draw_segmento(self, s):
		p1 = s.getP1()
		p2 = s.getP2()
		line(p1.getX(), self.alto-p1.getY(), p2.getX(), self.alto-p2.getY())



g = Grafica()
mi_interfaz = Interfaz(g, 800, 800)
nube = NubePosicionGeneral()
nube.aleatoria(10)
#aristas = [[(114.83, 329.21),(393.97, 105.68)],[(393.97, 105.68),(529.89, 471.87)],[(529.89, 471.87),(114.83, 329.21)],[(564.74, 93.13),(393.97, 105.68)],[(564.74, 93.13),(529.89, 471.87)]]
def setup():
	size(mi_interfaz.ancho, mi_interfaz.alto)
	#vertices = [(56.0,357.0),(265.0,284.0),(141.0,207.0),(368.0,148.0),(347.0,266.0),(279.0,371.0),(350.0,490.0),(160.0,510.0),(198.0,382.0),(32.0,486.0)]
	t = TriangulacionPuntos(nube)
	t.triangular()
	mi_interfaz.grafica = t.triangulacion
	mi_interfaz.draw_grafica(t.triangulacion)
	print(t.get_dcel_triangulacion().to_string())

	#for a in aristas:
	#	g.agregar_arista(Arista(Punto(a[0][0], a[0][1]), Punto(a[1][0], a[1][1])))
	#print(g.toString())

	
	#mi_dcel = DCEL()
	#mi_dcel.construir(g)
	#print(mi_dcel.to_string())

	#mi_interfaz.draw_grafica(g)



def draw():
	pass

	
