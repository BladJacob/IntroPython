"""
    Crear un programa que me pida un numero del 1 al 100 y si es otro numero que no sea entre esos 
    numeros muestre un mensaje que diga numero invalido y si es un numero correcto el numero ingresado
    lo utilizaremos para que nos de un resultado en numero binario while
   """
    
numero = int(input("Ingrese un numero del 1 al 100: "))
if numero < 1 or numero > 100:
    print("Numero invalido")
    numero = int(input("Ingrese un numero del 1 al 100: "))

binario = ""
while numero > 0:
    binario = str(numero % 2) + binario
    numero = numero // 2

print("El numero en binario es:", binario)
