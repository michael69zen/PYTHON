#Ejercicio 008
'''Desarrolle un programa que imprima numeros primos dado que el usuario ponga el limite'''

def es_primo(num):
    for i in range(2,num):
        if num % i == 0:
            return False
    return True

def primos_hasta(numero):
    primos = list()
    for i in range(2,numero+1):
        resultado = es_primo(i)
        if resultado==True:
            primos.append(i)
    return primos

primates = primos_hasta(98)
print(primates)
        
def es_primo2(n):
    # Un número primo debe ser mayor que 1
    if n <= 1:
        return False

    # Probamos divisores hasta la raíz cuadrada de n
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:   # Si divide exacto
            return False

    return True
