#Ejerccicio 006
'''Desarrolle un programa que cree una contraseña ramdon dado un numero entero'''

def crear_contrasenia(num):
    letras = "aeioumcrys"
    num_entero = str(num)
    num = int(num_entero[0])
    c1 = num - 2
    c2 = num
    c3 = num + 1
    contrasenia = f"{letras[c1]}{letras[c2]}{letras[c3]}{num*3}"
    return contrasenia

numero = int(input("DIGITE UN NUMERO PARA CREAR TU CONTRASENIA: "))
password = crear_contrasenia(numero)
frase = f"Sr. Usuario tu contrasenia es: {password}"
print(frase)
    
