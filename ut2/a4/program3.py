import sys

size_in = int(sys.argv[1])
chain_string = sys.argv[2]
count = 0
if size_in < 0:
    print('Error.Saliendo del programa...')
else:
    chain_list = chain_string.split()
    for word in chain_list:
        size_out = len(word)
        if size_in == size_out:
            count += 1
    print(f'Hay {count} palabras con {size_in} caracteres')
