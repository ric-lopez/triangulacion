#-*- coding: utf-8 -*-
def epsilon():
	"""Calcula el numero x positivo mas pequenio tal que 1 + x puede represtarse de forma precisa en la computadora"""
	x = 1.0
	n = 0
	while(1.0 + (x * 0.5) > 1.0):
		n += 1
		x *= 0.5
	return x