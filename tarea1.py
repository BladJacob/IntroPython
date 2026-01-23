
#Crear un programa que permita comparar las edades de dos personas, pidiendo las edades al usuario sin utilizar elif ni switch.

edad1 = int(input("Ingrese la edad de la primera persona: "))
edad2 = int(input("Ingrese la edad de la segunda persona: "))

if edad1 > edad2:
    print("La primera persona es mayor que la segunda.")
if edad1 < edad2:
    print("La segunda persona es mayor que la primera.")
if edad1 == edad2:
    print("Ambas personas tienen la misma edad.")