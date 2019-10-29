value1 = int(input("¿Cantidad?:" ))
if value1 > 0:
    if value1 >= 50:
        coc1 = (value1 % 50)
        resto = (value1 // 50)
        if resto >= 1:
            print(resto , "billete(s) de 50")
    if coc1 >= 20 or value1 >= 20:
        coc2 = (coc1 % 20)
        resto2 = (coc1 // 20)
        if resto2 >= 1:
            print(resto2, "billete(s) de 20")
    if coc2 >= 10 or coc1 >= 10 or value1 >= 10:
        coc3 = (coc2 % 10)
        resto3 = (coc2 // 10)
        if resto3 >= 1:
            print(resto3, "billete(s) de 10")
    if coc3 >= 5 or coc2 >= 5 or coc1 >= 5 or value1 >= 5:
        coc4 = (coc3 % 5)
        resto4 = (coc3 // 5)
        if resto4 >=1:
            print(resto4, "billete(s) de 5")
    if coc4 >= 2 or coc3 >= 2 or coc2 >= 2 or coc1 >= 2 or value1 >= 2:
        coc5 = (coc4 % 2)
        resto5 = (coc4 // 2)
        if resto5 >= 1:
            print(resto5, "moneda(s) de 2")
    if coc5 >= 1 or coc4 >= 1 or coc3 >= 1 or coc2 >= 1 or coc1 >= 1 or value1 >= 1:
        resto6 = (coc5 // 1)
        if resto6 >=1:
            print(resto6, "moneda de 1")
if value1 <= 0:
    print("justo en la pobreza")
