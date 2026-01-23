""""
crear un programa que depliegue un menu de opciones para el usuario
    opciones:
    1. Triangulo
    2. Cuadrado
    3. Circulo
    4. pentagono
    5. Salir
    El usuario debe seleccionar una opcion y el programa debe desplegar un mensaje indicando
    la figura seleccionada.
    y pedira los numeros nesesarios para calcular el area de la figura seleccionada
"""
import os
import math
def mostrar_menu():
    print("Menu de figuras:")
    print("1. Triángulo")
    print("2. Cuadrado")
    print("3. Círculo")
    print("4. Pentágono")
    print("5. Salir")
while True:
    os.system("cls")
    mostrar_menu()
    opcion = input("Seleccione una opción (1-5): ")
    if opcion == '5':
        print("Saliendo del programa.")
        break
    elif opcion == '1':
        base = float(input("Ingrese la base del triángulo: "))
        altura = float(input("Ingrese la altura del triángulo: "))
        area = (base * altura) / 2
        print("El área del triángulo es: {}".format(area))
    elif opcion == '2':
        lado = float(input("Ingrese el lado del cuadrado: "))
        area = lado ** 2
        print("El área del cuadrado es: {}".format(area))
    elif opcion == '3':
        radio = float(input("Ingrese el radio del círculo: "))
        area = math.pi * (radio ** 2)
        print("El área del círculo es: {}".format(area))
    elif opcion == '4':
        lado = float(input("Ingrese el lado del pentágono: "))
        area = (5 * lado ** 2) / (4 * math.tan(math.pi / 5))
        print("El área del pentágono es: {}".format(area))
    else:
        print("Opción no válida. Por favor, seleccione una opción del 1 al 5.")
    break