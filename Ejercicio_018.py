cantidad = int(input("DIGITE LA CANTIDAD DE NUMEROS EN LA LISTA: "))
lista_numeros = list()
for i in range(cantidad):
    numero = int(input(f"INGRESE EL NUMERO {i+1}: "))
    lista_numeros.append(numero)

lista_sin_repetidos = set(lista_numeros)
numeros_unicos = len(lista_sin_repetidos)
print(lista_sin_repetidos)
print(f"La lista tiene {numeros_unicos} elementos unicos")
