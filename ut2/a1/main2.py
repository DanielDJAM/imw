importe = int(input('Ingresar importe a desglosar: '))



# importes de los billetes y monedas con su tipo en singular

tipos = (

    (50,"billete"),

    (20,"billete"),

    (10,"billete"),

    (5,"billete"),

    (2,"moneda"),

    (1,"moneda")

)



for tipo in tipos:

    valor=tipo[0]

    descripcion=tipo[1]



    # funcion para mostrar la s del plural si es necesario

    s=lambda valor,text: valor > 1 and text+"s" or text



    if importe/valor>0:

        print ("%d %s de %d" % ((importe / valor), s((importe / valor),descripcion), valor))

        # cogemos el resto de la division

        importe = importe % valor
