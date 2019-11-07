import sys
i = int(sys.argv[1])
if i <= 0:
    sys.exit('Error')
if i > 0:
    for j in range(2, i):
        k = i % j
        if k == 0:
            print('no es primo')
        else:
            print('es primo')
        break
