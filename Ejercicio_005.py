#Ejercicio 005
'''Desarrolla un programa donde imprima un saludo dependiendo si es mujer, varon o lgbtq+'''

def saludo(nombre, sexo):
    sexo = sexo.lower()
    if sexo == "varon":
        adjetivo = "Rey"
        print(f"Hola {nombre} mi {adjetivo}, sigue siendo el mejor.")
    elif sexo == "mujer":
        adjetivo = "Reina"
        print(f"Hola {nombre} mi {adjetivo}, sigue siendo la mejor.")
    else:
        adjetivo = "mienbro lgtbq+"
        print(f"Hole {nombre} mi {adjetivo}, sigue siendo tu.")
        
saludo("Michael","VARon")
saludo("Mirian","muJER")
saludo("Tonta Queen","no binario")
