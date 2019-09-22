# Se declara una variable str, con una cadena de digitos.
# El tipo str = es una cadena o string.
numero="1234"

# Se muestra el tipo que tiene la variable. La salida type() no es un str, es un dato type.
print(type(numero))

# Se convierte la cadena a su equivalencia int.
# int = variable entera como '3'.
numero=int(numero)

# Se muestra como el tipo ya cambiado.
print(type(numero))

# Se declara un str con meta sustitucion.
salida="El numero utilizado es {}"

# Se muestra el resultado. Donde esta {} se coloque el valor de numero en este caso '1234'.
print(salida.format(numero))
