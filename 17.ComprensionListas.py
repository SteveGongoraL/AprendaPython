lista_vacia = list()
otra_lista_vacia = []
separador = ("°°°" * 40) + "\n"

lista_uno= [1, 2, 3, 4]
print(lista_uno)
print(separador)

lista_uno.append (5)  #Agregar un nuevo valor.
print(lista_uno)
print(separador)

#Dentro de un elemento de la lista puede abr otra lista o tupla.
lista_uno.append ((6,7))  #Agregando una tupla dentro de una lista.
print(lista_uno)
print(separador)

#Remover elementos.
lista_uno.remove((6,7)) #Investigar metodo "dell".
print(lista_uno)
print(separador)

# sort() para ordenar.
lista_original1= [3,5,4,6]
print(lista_original1)
print(separador)
lista_original1.sort() #Funciona con letras y numeros.
print(lista_original1)
print(separador)

# sorted() Para conservar tu tupla o lista original.
lista_original2= [23, 20, 39, 4]
lista_ordenada= sorted(lista_original2)
print(f"lista original = {lista_original2} & la lista ordenada= {lista_ordenada}")
print(separador)

# Comprension de listas.
print(f"lista original = {lista_uno}")
print(separador)

# SIN Comprension de listas.
lista_uno_al_doble =[]
for valor in lista_uno:
    lista_uno_al_doble.append(valor*2)
print(f"Lista resultante con cada elemento al doble: {lista_uno_al_doble}")
print(separador)

# CON Comprension de listas.
lista_uno_al_doble = [valor*2 for valor in lista_uno]
print(f"Mismo resultado, pero con comprension de lista: {lista_uno_al_doble}")
print(separador)

# Comprension de listas pero con condición.
lista_valores_pares = [valor for valor in lista_uno if(valor%2 ==0)]
print(f"Solamente se agregaron los elementos con valor par: {lista_valores_pares}")
print(separador)