'''
Realizar un programa que le pueda al usuario un número y el programa
deberá imprimir la pirámide de asteriscos según el número ingresado.
'''

num = int(input("Ingrese un número para la pirámide de asteriscos: "))
for i in range(1, num + 1):
    print('*' * i)
    
    