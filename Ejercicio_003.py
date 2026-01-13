#Ejercicio 003
'''Desarrollar un programa que resuelva la ecuacion de segundo grado'''

print("ax^2 + bx + c = 0")

a = int(input("Digite el valor de a: "))
b = int(input("Digite el valor de b: "))
c = int(input("Digite el valor de c: "))

discriminante = b**2 - 4*a*c

if discriminante < 0:
    print("No existe solucion en los numeros reales.")

else:
    x1 = (-b + discriminante**0.5)/(2*a)
    x2 = (-b - discriminante**0.5)/(2*a)
    print(f"Las soluciones de la ecuacion son x1 = {x1} y x2 = {x2}")
