numero= input("Escoje un numero del 1 al 9:  ")

# int = variable entera como '3'.
numero=int(numero)

# for ejecuta un loque de codigo un numero determinado de veces. En range se pone un numero mas del que deseas.
# En este ejemplo seria del 1 al 10 entonces en range se pone 1,11.
for i in range(1,11):
    # i ira variando
    salida="{} x {} = {}"
    print(salida.format(numero,i,i*numero))
