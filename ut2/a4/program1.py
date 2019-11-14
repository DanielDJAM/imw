import sys

num = int(sys.argv[1])

if len(str(num)) == 8:
    value1 = num % 23
    DNI = 'TRWAGMYFPDXBNJZSQVHLCKE'
    print(f'{num}{DNI[value1]}')
    
else:
    print('Introduzca 8 dígitos')
