# int = variable entera como '3'
acomulado=int(0)

# str = es una cadena o string
numero=str("")

# Al colocar 'true' como condicion de while se formara un ciclo infinito que no se rompera hasta que se use break.
while True:
    numero=input("Dame un numero entero: " )
    if numero=="":
        # Si no se pone numero, se reporta y se acaba el ciclo.
        print("Vacio, Salida del programa.")
        break
    else:
     # Si se pone un numero, acomulado = acomulado= numero. Se realiza el calculo usando suma incluyente (+=)
     acomulado+=int(numero)
     salida="Monto acomulado: {} "
     print(salida.format(acomulado))
