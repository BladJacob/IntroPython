
# Crear un programa que permita determinar si una calificación es aprobatoria o reprobatoria, pidiendo la calificación al usuario y si es mayor que 9 es excelente

calificacion = int(input("Ingrese la calificación: "))
if calificacion >= 7:
    print("Aprobado")
    if calificacion > 9:
        print("Excelente")
else:
    print("Reprobado")
    
    
    
    
    