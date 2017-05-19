#-*- coding: utf-8 -*-
import random
from recta import *
from punto import Punto

class NubePosicionGeneral:

	def __init__(self):
		''''''
		self.puntos = []
		self.rectas = []

	def get_puntos(self):
		return self.puntos

	def test_pos_general(self, p):
		'''verifica si p esta en posicion general con respecto a los puntos de la nube'''
		if len(self.rectas) == 0:
			return True
		for r in self.rectas:
			if(r.contiene(p)):
				return False
		return True

	def agrega_rectas(self, p):
		''''''
		for pto in self.puntos:
			self.rectas.append(Recta(p, pto))


	def add_punto(self, p):
		''' Agrega el punto p a la nube de puntos'''
		if len(self.puntos) == 0:
			self.puntos.append(p)
			return True
		else:
			if(self.test_pos_general(p)):
				self.agrega_rectas(p)
				self.puntos.append(p)
				return True
			else:
				return False

	def aleatoria(self, n):
		''' Agrega a la nube n puntos aleatorios en posicion general'''
		i = 0
		while(i < n):
			x = random.random()*750
			y = random.random()*600
			if(self.add_punto(Punto(x,y))):
				i += 1
		return self.puntos

	def get_menor(self):
		'''Regresa el punto con la menor coordenada x'''
		p_min = self.puntos[0]
		for p in self.puntos:
			if p.compara(p_min) == -1:
				p_min = p
		return p_min


def main():
	''' '''
	print("Dame el tamaño del conjunto:")
	n = int(input())
	nube = NubePosicionGeneral()
	nube.aleatoria(n) # Se agregan n puntos aleatorios a la nube
	i = 1
	for p in nube.puntos:
		print(str(i)+" "+p.toString())
		i+=1

if __name__ == '__main__':
	main()