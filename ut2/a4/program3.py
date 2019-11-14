import sys

num = int(sys.argv[1])
Chain_String = str(sys.argv[2])

if num < 0:
    print('Error.Saliendo del programa...')
else:
    for i in Chain_String:
        Chain_List = Chain_String.split()
        size = len(Chain_List)
        result = Chain_List[num]
        print(result)
