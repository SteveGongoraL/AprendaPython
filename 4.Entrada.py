entrada=input()
print(type(entrada))

# La variable booleana contiene el resultado de verificar si lo capturado es digito, y si no se encuentra un punto.
# En lo capturado. Si find retorna -1 quiere decir que lo buscado,
# En este caso un punto decimal no se encontro. Si esEntero es True, lo capturado es entero.
esEntero=(entrada.isdigit() and entrada.find(".") ==-1)

if (esEntero):
    # Si la condicion es verdadera:
    print("Dato entero. Muy bien!!")
else:
    # Si la condicion es falsa:
    print("Dato no es entero. Intente nuevamente.")
