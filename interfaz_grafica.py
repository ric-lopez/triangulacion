from util_geometry.grafica import Grafica
from util_geometry.punto import Punto
from util_geometry.poligonoSimple import PoligonoSimple
from util_geometry.triangulacion import Triangulacion

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
			line(u.getX(), self.alto-u.getY(), v.getX(), self.alto-v.getY())


	def draw_linea(self, p1, p2):
		line(p1.getX(), self.alto-p1.getY(), p2.getX(), self.alto-p2.getY())

	def draw_segmento(self, s):
		p1 = s.getP1()
		p2 = s.getP2()
		line(p1.getX(), self.alto-p1.getY(), p2.getX(), self.alto-p2.getY())



p = PoligonoSimple()
g = Grafica()
mi_interfaz = Interfaz(g, 800, 800)
triangulacion = Grafica()
t = Triangulacion(p)

def setup():
	size(mi_interfaz.ancho, mi_interfaz.alto)
	#vertices = [(56.0,357.0),(265.0,284.0),(141.0,207.0),(368.0,148.0),(347.0,266.0),(279.0,371.0),(350.0,490.0),(160.0,510.0),(198.0,382.0),(32.0,486.0)]
	vertices = [(56.0,357.0),(265.0,284.0),(141.0,207.0),(368.0,148.0),(347.0,266.0),(525.0,306.0),(494.0,175.0),(677.0,286.0),(682.0,546.0),(482.0,493.0),(588.0,408.0),(410.0,438.0),(440.0,351.0),(279.0,371.0),(350.0,490.0),(160.0,510.0),(198.0,382.0),(32.0,486.0)]
	# vertices = [(121.0,332.0),
	# 			(168.0,401.0),
	# 			(318.0,402.0),
	# 			(289.0,295.0),
	# 			(417.0,347.0),
	# 			(432.0,424.0),
	# 			(333.0,449.0),
	# 			(419.0,529.0),
	# 			(548.0,489.0),
	# 			(468.0,380.0),
	# 			(612.0,372.0),
	# 			(450.0,306.0),
	# 			(569.0,282.0),
	# 			(200.0,200.0)]

	for v in vertices:
		p.addV(Punto(v[0], v[1]))
	p.cerrar()
	aristas = p.getAristas()
	for a in aristas:
		g.agregar_arista(a)

	mi_interfaz.draw_grafica(g)
	stroke(0,0,255)

	# t = Triangulacion(p)	
	# triangulacion = t.triangular()
	# print("triangulacion:")
	# print(triangulacion.toString())
	# mi_interfaz.draw_grafica(triangulacion)


def draw():
	pass
	diagonal = None
	diagonal = t.por_pasos(p)
	if diagonal:
		mi_interfaz.draw_segmento(diagonal)
		#line(diagonal.getP1().getX(), diagonal.getP1().getY(), diagonal.getP2().getX(), diagonal.getP2().getY())

	
