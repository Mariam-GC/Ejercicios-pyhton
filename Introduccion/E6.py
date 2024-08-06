#Escribir un programa que lea un entero positivo, n, introducido por el usuario y después muestre en pantalla la suma de todos los enteros desde 1 hasta n . La suma de los primeros n enteros positivos puede ser calculada de la siguiente forma: n(n+1)/2
n = int(input("escriba un número entero positivo: "))
suma = (n*(n+1)/2)
print("la suma de los números desde el 1 hasta el " + str(n) + " es: " + str(suma))