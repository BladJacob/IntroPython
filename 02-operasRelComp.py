import math, os
os.system("cls")

print("|----------Grupo ICO201-9, ICO201-14----------|")

num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

suma = num1 + num2
print("La Suma de {} y {} es: {}".format(num1, num2, suma))

resta = num1 - num2
print("La resta de {} y {} es: {}".format(num1, num2, resta))

multiplicacion = num1 * num2
print("La multiplicación de {} y {} es: {}".format(num1, num2, multiplicacion))

division = num1 / num2
print("La división de {} y {} es: {}".format(num1, num2, division))

potencia = num1 ** num2
print("La potencia de {} a la {} es: {}".format(num1, num2, potencia))

print("\nOperaciones básicas: \n1.-Suma\n2.-Resta\n3.-Multiplicación\n4.-División\n")

opcion = input("Ingrese la operación a realizar (1/2/3/4): ")

val1 = 3
val2 = 5

temp = val1 > val2
print("El valor de la comparación es:", temp)

temp = val1 > val2 #False
temp = val1 == val2 #False
temp = val1 < val2 #True
temp = val1 >= val2 #False
temp = val1 <= val2 #True
temp = val1 != val2 #True

temp = not(val1 > val2) #True
print("El valor de la comparación es:", temp)

temp2 = not(val1 > val2) and (val1 < val2) #True
#not(False)        #True


