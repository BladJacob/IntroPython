#Crear un programa que le pida al usuario 5 calificaciones, despues de pedirlas voy a imprimir promedio de las calificaciones usando un sicclo while
suma = 0
cali = 0
while cali < 5:
    calificacion = int(input("Ingrese la calificación {}: ".format(cali + 1)))
    suma += calificacion
    cali += 1
promedio = suma / 5
print("El promedio de las calificaciones es: {}".format(promedio))
 
