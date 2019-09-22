numero1=input("Dime el primer numero: ")
numero2=input("Dime el segundo numero: ")
salida="Numero proporcionaos: {} y {}. {}."

if (numero1==numero2):
    # Esto es si ambos numeros son iguales.
    print(salida.format(numero1, numero2, "Los numeros son iguales"))
else:
    # if dentro de if es una condicional anidada.
    # Si los numeros no son iguales entra aqui.
    if numero1>numero2:
        # Si el primer numero es mayor entonces:
        print(salida.format(numero1, numero2, "El primer numero es mayor que el segundo"))
    else:
        # Si no se cumplen ninguna de las anteriores por ende significa que el segundo numero es el mayor.
        print(salida.format(numero1, numero2, "El segundo numero es el mayor que el primero"))
