#Escribir un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora. Después debe mostrar por pantalla la paga que le corresponde.

horas_Trabajadas= float(input("Número de horas trabajadas:"))
pago_hora = float(input("Precio de paga por hora trabajada:"))
salario = horas_Trabajadas * pago_hora
print ("Su salario corresponiente es: ", salario)
