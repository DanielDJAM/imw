import sys

num = int(sys.argv[1])
sequence=0
if num < 0:
    sys.exit('Error. Solo admite números positivos')
else:
    for loop1 in range(1, num+1):
            value1 = loop1 ** 2
            sequence = sequence + value1
    print(sequence)
