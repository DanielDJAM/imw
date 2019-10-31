from math import sqrt
import sys

a = float(sys.argv[1])
b = float(sys.argv[2])
c = float(sys.argv[3])
if a == 0:
    x3 = (- c / b)
    print("x = ", x3)
elif ((b ** 2) - 4 * a * c) < 0:
    print("números complejos")
else:
    x1 = (- b + sqrt(b ** 2 - ( 4 * a * c))) / ( 2 * a)
    print("x1 = ", x1)
    x2 = (- b - sqrt(b ** 2 - ( 4 * a * c))) / ( 2 * a)
    print("x2 = ", x2)
