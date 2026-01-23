"""
   pedir al usuarios un sualdo de una persona y calcular el impuesto a pagar segun las siguientes reglas:
    - si el sueldo es menor a 1000, no paga impuesto
    - si el sueldo es entre 1000 y 2000, paga el 10% de impuesto
    - si el sueldo es mayor a 2000, paga el 20% de impuesto
    mostrar el sueldo neto despues de descontar el impuesto
"""
sueldo = float(input("Ingrese su sueldo: "))
if sueldo < 1000:
    impuesto = 0
elif 1000 <= sueldo <= 2000:
    impuesto = sueldo * 0.10
else:
    impuesto = sueldo * 0.20
sueldo_neto = sueldo - impuesto
print("El sueldo neto después de descontar el impuesto es: {:.2f}".format(sueldo_neto))
