import sys

nota = float(sys.argv[1])

if 0 <= nota < 5:
    print("suspenso")
elif 5 <= nota < 7:
    print("aprobado")
elif 7 <= nota < 9:
    print("notable")
elif 9 <= nota < 10:
    print("sobresaliente")
elif nota == 10:
    print("matrícula de honor")
else:
    print("Error")
