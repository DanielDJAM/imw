from math import sqrt
a = int(input("valor de a:"))
b = int(input("valor de b:"))
c = int(input("valor de c:"))

if ((b ** 2) - 4 * a * c) < 0:
    print("números complejos")
else:
    x1 = (- b + sqrt(b ** 2 - ( 4 * a * c))) / ( 2 * a)
    print(x1)
    x2 = (- b - sqrt(b ** 2 - ( 4 * a * c))) / ( 2 * a)
    print(x2)
