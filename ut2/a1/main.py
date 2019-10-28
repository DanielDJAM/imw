print(x, type(x))
x= int(x)
if x== int(x) and >50:
    a=(x%50)
    b=(x//50)
    if a<50 and a>20:
        c=(a%20)
        d=(a//20)
        if c<20 and c>10:
            e=(c%10)
            f=(c//10)
            if e<10 and e>5:
                g=(e%5)
                h=(e//5)
                if g<5 and g>2:
                    i=(g%2)
                    j=(g//2)
                    if i<1 and i>1:
                        k=(i%1)
                        if k==0:
                            print("Tenemos" b "billetes de 50," d "de 20," f "de 10," h "de 5," j " monedas de 2 y" k "moneda")
                    else:
                        print("Ha ocurrido un error. Vuelve a intentarlo. Error:05")
                else:
                    print("Ha ocurrido un error. Vuelve a intentarlo. Error:04")
            else:
                print("Ha ocurrido un error. Vuelve a intentarlo. Error:03")

        else:
            print("Ha ocurrido un error. Vuelve a intentarlo. Error:02")
    else:
        print("Ha ocurrido un error. Vuelve a intentarlo. Error:01")
else:
    print("Inserta números enteros")
