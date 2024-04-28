temperatura=float(input("Dime tu temperatura: "))
#temperatura=float(temperatura)
salida="Usted se encuentra con {} "

if (temperatura>36.5 and temperatura<37.5):
    print(salida.format("temperatura normal "))
else:
    if (temperatura<35.0):
        print(salida.format("hipotermia"))
    else:
        if (temperatura>35.0 and temperatura<36.5):
            print(salida.format( "frio "))
        else:
            print(salida.format("fiebre "))
