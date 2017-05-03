from util_geometry.punto import Punto
import math

p0 = Punto(0,0)
p1 = Punto(-10, 0.1)
p2 = Punto(10,0)

print(math.degrees(p0.angulo(p1, p2)))