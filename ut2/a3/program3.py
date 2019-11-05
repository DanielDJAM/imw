import sys

num1 = int(sys.argv[1])
num2 = int(sys.argv[2])

if num < 0:
    sys.exit("Error. Solo admite números positivos")
else:
    for i in range(num2, num1, -1):
        if num1 > num2:
            
