'''
Crear un programa que me permita multiplicar a por b sin usar multiplicaciones utilizando un
siclo while y pedir 2 números al usuario
'''


a = int(input("Ingrese el valor de A: "))
b = int(input("Ingrese el valor de B: "))
resultado = 0
contador = 0
while contador < b:
    resultado += a
    contador += 1
print("El resultado de {} por {} es: {}".format(a, b, resultado))

