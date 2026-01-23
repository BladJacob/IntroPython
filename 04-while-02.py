#crear un programa que pida al usuario ingresar numeros el programa debe terminar cuando el usuario ingrese el numero 0 al finalizar el programa imprimir la suma total de los numeros ingresados utilizando un ciclo while


suma = 0
numero = int(input("Ingrese un número (0 para terminar): "))

while numero != 0:
    suma += numero
    numero = int(input("Ingrese un número (0 para terminar): "))

print("La suma total de los números ingresados es: {}".format(suma))
