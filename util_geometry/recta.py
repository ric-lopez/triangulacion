#-*- coding: utf-8 -*-
from punto import Punto
from arista import Arista
from utilidades import epsilon

class Recta:
	""" Recta que pasa por dos puntos"""

	def __init__(self, a, b):
		self.a = a
		self.b = b

	def punto_pendiente(self):
		if((self.a.getX() - self.b.getX()) == 0):
			m = 'infinito'
			b = self.a.getX()
		else:
			m = (self.a.getY() - self.b.getY())/(self.a.getX() - self.b.getX())
			b = self.a.getY()-(m*self.a.getX())
		return (m, b)

	def general(self):
		a = self.b.getY()-self.a.getY()
		b = self.b.getX()-self.a.getX()
		c = self.a.getY()(self.b.getX()-selfepsilon.a.getX()) - self.a.getX()(self.b.getY()-self.a.getY())
		return (a,b,c)

	def interseccion_pp(self, l):
		l1 = self.punto_pendiente()
		#print("l1: m="+str(l1[0])+", b="+str(l1[1]))
		l2 = l.punto_pendiente()
		#print("l2: m="+str(l2[0])+", b="+str(l2[1]))
		if(l1[0] == l2[0]):
			if(l1[1] == l2[1]):
				return 'iguales'
			else:
				return False
		else:
			if(l1[0] == 'infinito'):
				x = l1[1]
				y = (l2[0]*x)+l2[1]
				return Punto(x, y)
			elif(l2[0] == 'infinito'):
				x = l2[1]
				y = (l1[0]*x)+l1[1]
				return Punto(x, y)
			elif(l1[1] == l2[1]):
				x = 0
				y = (l1[0]*x)+l1[1]
				return Punto(x, y)
			else:
				x = (l2[1]-l1[1])/(l1[0]-l2[0])
				y = (l1[0]*x)+l1[1]
				#print("interseccion: " + str(x) + "," + str(y))
				return Punto(x, y)

	def interseccion_segm(self, s):
		a = s.getP1()
		b = s.getP2()
		l_s=Recta(a, b)
		if(self.a == a or self.b == a):
			return a
		elif(self.a == b or self.b == b):
			return b

		p_int = self.interseccion_pp(l_s)
		if(p_int == 'iguales'):
			return s
		if(p_int == False):
			return False

		minX = min(a.getX(), b.getX())
		maxX = max(a.getX(), b.getX())
		minY = min(a.getY(), b.getY())
		maxY = max(a.getY(), b.getY())

		ep = epsilon()

		if(minY == maxY):
			if(minX <= p_int.getX() and maxX >= p_int.getX()):
				return p_int
		elif(minX == maxX):
			if(minY <= p_int.getY() and maxY >= p_int.getY()):
				return p_int
		'''
		print("minX:"+str(minX)+", maxX:"+"{:.20f}".format(maxX)+", minY:"+str(minY)+", maxY:"+str(maxY))
		print("punto interseccion: "+"{:.120f}".format(p_int.getX())+", "+str(p_int.getY()))
		print(minX - (ep+ep) <= p_int.getX())
		print(maxX + (ep+ep) >= p_int.getX())
		print(minY - (ep+ep) <= p_int.getY())
		print(maxY + (ep+ep) >= p_int.getY())
		'''
		#se da un epsilon de error para determinar las intersecciones
		tolerancia = 2
		minX -= (ep*tolerancia)
		maxX += (ep*tolerancia)
		minY -= (ep*tolerancia)
		maxY += (ep*tolerancia)
		#print("[{:.20f}".format(minX)+", {:20f}".format(maxX)+"] : [{:.20f}".format(minY)+", {:20f}".format(maxY)+"]")
		if((minX <= p_int.getX() and maxX >= p_int.getX()) and (minY <= p_int.getY() and maxY >= p_int.getY())):
		#if(((min(a.getX(), b.getX()) <= p_int.getX()) and (max(a.getX(), b.getX()) >= p_int.getX())) and ((min(a.getY(), b.getY()) <= p_int.getY()) and (max(a.getY(), b.getY()) >= p_int.getY()))):
			return p_int
		else:
			#print("la interseccion no esta dentro del segmento o arista: "+s.toString())
			return False

	def interseccion_semirrecta_segm(self, s):
		''' Determina la interseccion entre la semirecta semi_r y s
		semi_r es un objeto Recta, para esta funcion se toma como punto origen de la semirecta el atributo a de semi_r '''
		inter = self.interseccion_segm(s)
		if(inter == False):
			return False
		else:
			#cuadrante = None
			origen = self.a
			direccion = self.b
			if(direccion.getX() > origen.getX() and direccion.getY() >= origen.getY()):
				#cuadrante = "I"
				if(inter.getX() >= origen.getX() and inter.getY() >= origen.getY()):
					return inter
				else:
					return False
			elif(direccion.getX() <= origen.getX() and direccion.getY() > origen.getY()):
				#cuadrante = "II"
				if(inter.getX() <= origen.getX() and inter.getY() >= origen.getY()):
					return inter
				else:
					return False
			elif(direccion.getX() < origen.getX() and direccion.getY() <= origen.getY()):
				#cuadrante = "III"
				if(inter.getX() <= origen.getX() and inter.getY() <= origen.getY()):
					return inter
				else:
					return False
			elif(direccion.getX() >= origen.getX() and direccion.getY() < origen.getY()):
				#cuadrante = "IV"
				if(inter.getX() >= origen.getX() and inter.getY() <= origen.getY()):
					return inter
				else:
					return False
			

	def contiene(self, p):
		'''Determina si la recta que llama al metodo contiene a p'''
		l = self.punto_pendiente()
		return p.getY() == l[0]*p.getX() + l[1]


	def toString(self):
		return "("+self.a.toString()+","+self.b.toString()+")"
		

	#def lado_r_segmento(self, s):
	#	s_r = Arista(self.a, self.b)
	#	l_a = s_r.lado_p_arista(s.getP1())
	#	l_b = s_r.lado_p_arista(s.getP2())
	#	if(l_a == 'der')


if __name__ ==  '__main__':

	a = Punto(2,4)
	b = Punto(5,2)

	c = Punto(5,1)
	d = Punto(7,3)

	u = Punto(2,2)
	v = Punto(4,4)
 
 	l1 = Recta(v, u)
	l2 = Recta(c, d)

	s = Arista(a, b)

	print("Intersccion debe ser verdadera")
	print("Recta l1"+l1.toString())
	i_1 = l1.interseccion_segm(s)
	print(i_1)

	print("Interseccion debe ser falsa")
	print("Recta l2 ="+l2.toString())
	i_2 = l2.interseccion_segm(s)
	print(i_2)

	print("punto pendiente:")
	print(Recta(Punto(3,7), Punto(6,4)).punto_pendiente())


	l3 = Recta(Punto(4,3), Punto(1,6))
	l4 = Recta(Punto(3,1), Punto(3,7))
	print("interseccion :")
	print(l4.interseccion_segm(Arista(Punto(4,3), Punto(1,6))).toString())



	print("ejemplo que da False en poligono de visibilidad:")
	print("segmento= [(4.17, 3.6), (5.86, 4.76)]")
	print("recta = [(4.02, 2.28), (4.17, 3.6)] ")
	ab = Arista(Punto(4.17, 3.6), Punto(5.86, 4.76))
	r_barrido = Recta(Punto(4.02, 2.28), Punto(4.17, 3.6))
	print("el resultado de la interseccion es:")
	print(r_barrido.interseccion_segm(ab).toString())

	epsi = epsilon() 
	print("epsilon de la computadora: {:.52f}".format(epsi))






