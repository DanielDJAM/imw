from math import sqrt
import sys

x1, y1 = float(sys.argv[1]), float(sys.argv[2])
x2, y2 = float(sys.argv[3]), float(sys.argv[4])
x3, y3 = float(sys.argv[5]), float(sys.argv[6])

d1 = sqrt( ((x1 - x2) ** 2) + ((y1 - y2) ** 2) )
d2 = sqrt( ((x1 - x3) ** 2) + ((y1 - y3) ** 2) )

if d1 < d2:
    print("El punto más cercano es (", x2, ",", y2, ") a distancia ", d1)
if d1 > d2:
    print("El punto más cercano es (", x3, ",", y3, ") a distancia ", d2)
