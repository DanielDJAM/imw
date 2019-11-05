import sys
i = int(sys.argv[1])
if i <= 0:
    sys.exit("Error")
else:
    for j in range(2, i):
        if j % i == 0:
            print("es primo")
            break
    else:
        print("no es primo")
