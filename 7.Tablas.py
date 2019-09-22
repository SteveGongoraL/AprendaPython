for i in range(1,11):
    encabezado="Tabla del {}"
    print(encabezado.format(i))

    # Si dejas el print en blanco es igual a un salto de linea.
    print()

    # Dentro del for puede ir otro for.
    # Se pone el numero de tablas que deseas +1 en range.
    for j in range(1,11):
        # La i contiene el numero base de la tabla y j el elemento por el que se multiplicara.
        salida="{} x {} = {}"
        print(salida.format(i,j,i*j))
    else:
        # Al concluir se ejecutara este codigo que es un salto de linea.
        print()
