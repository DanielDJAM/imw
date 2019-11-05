import sys

num = int(sys.argv[1])
secuencia=0
if num < 0:
    sys.exit("Error. Solo admite números positivos")
else:
    for bucle in range(1, num+1):
            var1 = bucle ** 2
            secuencia = secuencia + var1
    print(secuencia)
