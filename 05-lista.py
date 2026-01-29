'''
una lista es una estructura de datos que permitealmacenar varios valores en una sola variable
Las listas pueden contener datos del mismo o de distinto tipo y son mutables ( se pueden modificar)
'''

lista2=[]
numeros=[1,2,3,4,5]
print(numeros)
nombres=["Ana","Luis","Carlos"]
print(nombres)
mezcla=[10,"Hola",3.5,True]
print(mezcla)

print(nombres[1])
print("-------------------------------------")
print(type(mezcla))
#Agregar elementos a la lista
print(nombres)
nombres[1]="Pedro"
print(nombres)
nombres.append("Juan")
print(nombres)
print(lista2)
lista2.append(1)
lista2.append(5)
lista2.append(7)
print(lista2)
