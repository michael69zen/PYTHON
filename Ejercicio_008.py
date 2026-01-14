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
        
