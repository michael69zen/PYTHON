#Ejercicio 009
'''Desarrolle un programa que muestre la serie de fibonacci hasta un numero dado'''

# Fibonacci iterativo (hasta un número dado)

valor = int(input("DIGITE HASTA QUE NUMERO SEA LA SERIE DE FIBONACCI: "))

numeros = []

a, b = 0, 1  # primeros dos números

while a <= valor:
    numeros.append(a)
    a, b = b, a + b  # avanzamos en la serie

print(numeros)
