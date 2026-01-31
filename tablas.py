'''
Crear un programa que pida un numero al usuario una ves ingresado imprimir
la tabla de multiplicar de ese numero utilizando un ciclo for
'''

numero = int(input("Ingrese un número para ver su tabla de multiplicar: "))
print("Tabla de multiplicar del {}:".format(numero))
for i in range(1, 11):
    resultado = numero * i
    print("{} x {} = {}".format(numero, i, resultado))
    
