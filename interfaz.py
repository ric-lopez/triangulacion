from util_geometry.poligonoSimple import PoligonoSimple
from util_geometry.punto import Punto

class Interfaz():

	def __init__(self, poligono):
		self.poligono = poligono


	def draw_poligono(self, poligono):
		vertices = poligono.getVertices()

		for v in vertices:
			u = poligono.anterior(v)
			line(u.getX(), u.getY(), v.getX(), v.getY())


p = PoligonoSimple()
def setup():
	size(600, 600)
	vertices = [(330.00000000000000000000, 442.00000000000000000000),
				(227.00000000000000000000, 396.99999999999994315658),
				(144.00000000000000000000, 304.00000000000000000000),
				(218.00000000000002842171, 165.00000000000000000000),
				(358.00000000000000000000, 134.99999999999997157829),
				(512.00000000000000000000, 202.00000000000000000000),
				(560.00000000000000000000, 329.00000000000000000000),
				(478.00000000000000000000, 408.00000000000000000000)]

	#p = Poligono()
	for v in vertices:
		p.addV(Punto(v[0], v[1]))

def draw():

	mi_interfaz = Interfaz(p)
	mi_interfaz.draw_poligono(p)