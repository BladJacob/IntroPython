'''
Crear un programa que pida 5 sueldos agregarlos a una lista e imprimirlos
'''

sueldos=[]

cont=0
while cont<=4:
    tem=float(input("Dame un sueldo"+ str({cont+1})))
    sueldos.append(tem)
    cont+=1

print("Los sueldos son:"+ str(sueldos))

promedio=sum(sueldos)/len(sueldos)
print("El sueldo promedio es:"+ str(promedio))
print("El sueldo mayor es:"+ str(max(sueldos)))
print("El sueldo menor es:"+ str(min(sueldos)))
