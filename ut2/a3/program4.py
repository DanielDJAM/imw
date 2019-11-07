import sys

num = int(sys.argv[1])
if num <= 0:
    print('Error. Solo se admiten mayor a 0')
if num > 0:
    for loop1 in range(1, num+1):
        value1 = 1
        for loop2 in range(loop1, 0, -1):
            value1 *= loop2
        print(loop1, '!, = ', value1)
