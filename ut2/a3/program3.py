import sys

num1 = int(sys.argv[1])
num2 = int(sys.argv[2])

if num1 <= 0 or num2 <= 0:
    sys.exit('Error. Solo admite números positivos's)
if num1 < num2:
    num1, num2 = num2, num1
if num1 > num2:
    for loop1 in range(num1, 0, -1):
        coc1 = num1 % loop1
        coc2 = num2 % loop1
        if coc1 == 0 and coc2 == 0:
            print(loop1)
            break
