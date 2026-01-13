#Ejercicio 001
'''desarrollar un programa que solicite al usuario ingresar su edad y luego imprima un mensaje indicando si es mayor de edad o menor de edad.'''

edad = int(input("DIGITE SU EDAD: "))

if edad < 0 or edad > 122:
    print("Edad no valida. Ud no ha nacido o ya ha fallecido.")
elif edad >= 18:
    print("Ud es mayor de edad, puede pasar al evento.")
else:
    print("Ud es menor de edad, no puede pasar al evento.")
    
print("GRACIAS POR SU VISITA")
