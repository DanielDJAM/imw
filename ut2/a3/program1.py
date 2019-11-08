import sys
num = int(sys.argv[1])
if num <= 0:
    sys.exit('Error')
if num == 1 or num == 2 or num == 3:
    print('es primo')
if num > 4:
    for loop in range(4, num):
        value1 = num % loop
        if value1 == 0:
            print('no es primo')
        else:
            print('es primo')
        break
