import os
os.system("cls")

print("1: +\n2: -\n3: *\n4: /\nElija un numero distinto para salir")

opcion = int(input("\nElija una opcion: "))
if opcion !=1 and opcion !=2 and opcion !=3 and opcion !=4:
    print("\nSaliendo del programa...")
else:
    num1 = float(input("\nIngrese el primer numero: "))
    num2 = float(input("Ingrese el segundo numero: "))

    if opcion == 1:
        resultado = num1 + num2
        print(f"\nEl resultado de la suma es: {resultado}")
    elif opcion == 2:
        resultado = num1 - num2
        print(f"\nEl resultado de la resta es: {resultado}")
    elif opcion == 3:
        resultado = num1 * num2
        print(f"\nEl resultado de la multiplicacion es: {resultado}")
    elif opcion == 4:
        if num2 != 0:
            resultado = num1 / num2
            print(f"\nEl resultado de la division es: {resultado}")
        else:
            print("\nError: No se puede dividir entre cero.")


