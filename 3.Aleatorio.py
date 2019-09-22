# A las librerias en python se les conoce como modulos (module).
# Para utilizar un modulo en un programa, primero debe importarse, usando la instruccion import.
import random

# Se define una variable float, y se le asigna un valor.
# float = variable flotante, con decimal como '6.7'.
numero1=float(10.5)

# Una funcion es un conjunto de instrucciones que procesan una tarea especifica, como una unidad de ejecucion.
# Se declaran con def. Todo el codigo posicionado a la derecha de la definicion, forma parte de la funcion.
def miFuncion():

    # Se convierte a float el numero aleatorio generado por random.randrange().
    # (solo esta disonible si se importa el modulo random).
    # En este ejemplo los numeros aleatorios posibles seran del 1 al 9.
    numero2=float(random.randrange(1,10))

    # Se utiliza esta sustitucion para mostrar resultados.
    # Donde en los primeros {} ira el numero que definiste y en los segundos {} ira el numero aleatorio del 1 al 9.
    mensaje="La suma de {} y {} es {}"
    print(mensaje.format(numero1,numero2,numero1+numero2))

# Se ejecuta la funcion definida en el codigo.
miFuncion()
