#Ejercicio 007
'''Desarrollar un programa donde pida al usuario nombres y edad,
que imprima el nombre del profesor y el asistente siendo el de menor y mayor de edad respectivamente'''

personas = list()

def obtener_personas(cantidad):
    for i in range(cantidad):
        nombre = input(f"Ingrese el nombre de la persona nro {i+1}: ")
        edad = int(input(f"Ingrese la edad de la persona {i+1}: "))
        companiero = (nombre,edad)
        personas.append(companiero)
    
    personas.sort(key=lambda x:x[1])
    mayor = personas[-1][0]
    menor = personas[0][0]
    
    return mayor,menor

profesor, asistente = obtener_personas(6)

print(f"El profesor es {profesor}, y su asistente es: {asistente}")

