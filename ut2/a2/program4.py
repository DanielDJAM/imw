from math import pi
from math import sqrt
import sys

r = float(sys.argv[1])

d = 2 * r
p = 2 * pi * r
a = pi * r **2

soluciones = input ("Elige una de las siguientes soluciones (diámetro(d), perímetro(p), área(a) o salir(s): ")
if soluciones == "diámetro" or soluciones == "diametro" or soluciones == "d":
    print(d)
if soluciones == "perímetro" or soluciones == "perimetro" or soluciones == "p":
    print(p)
if soluciones == "área" or soluciones == "area" or soluciones == "a":
    print(a)
if soluciones == "salir" or soluciones == "s":
    print("Saliendo del programa...")
