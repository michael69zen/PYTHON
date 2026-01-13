#Ejercicio 004
'''Desarrollar un programa que pida al usuario una frase y calcular en cuanto tiempo las puede decir
suponiendo que una persona promedio habla a 2 palabras por segundo. calcular el numero de palabras si
se tarda mas de 1 minuto decirle al usuario que tampoco escribir una novela. calcular en cuanto
tiempo te tardarias si fueras un 30% mas rapido que una persona promedio.'''

frase = input("DIGITE UNA FRASE: ")

lista_palabras = frase.split(" ")
palabras = len(lista_palabras)

tiempo = palabras/2

if tiempo > 60:
    print("No escriba una novela")
else:
    print(f"El numero de palabras es: {palabras}")
    print(f"El tiempo que se tarda en decir la frase es: {tiempo} segundos")
    tiempo_yo = tiempo*0.7
    print(f"El tiempo que yo me tardaria en decir la frase es: {tiempo_yo} segundos")
