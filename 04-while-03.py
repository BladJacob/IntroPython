#crear un programa que nos de un menu donde las opciones sean suma resta muktiplicacion division y la ultima sea salir y que cada opcion nos pida ingresar 2 valores y nos de el resultado de la operacion seleccionada hasta que elijamos salir

def mostrar_menu():
    print("Menu de opciones:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Salir")
    
while True:
    os.system("cls")
    mostrar_menu()
    opcion = input("Seleccione una opción (1-5): ")
    
    if opcion == '5':
        print("Saliendo del programa.")
        break
    
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    
    if opcion == '1':
        resultado = num1 + num2
        print("El resultado de la suma es: {}".format(resultado))
    elif opcion == '2':
        resultado = num1 - num2
        print("El resultado de la resta es: {}".format(resultado))
    elif opcion == '3':
        resultado = num1 * num2
        print("El resultado de la multiplicación es: {}".format(resultado))
    elif opcion == '4':
            resultado = num1 / num2
            print("El resultado de la división es: {}".format(resultado))
    else:
        print("Opción no válida. Por favor, seleccione una opción del 1 al 5.")
        break
    