def conteoPalabras(frase):
    palabras=frase.split(" ")
    conteo={}
    
    for palabra in palabras:
        if palabra in conteo:
            conteo[palabra] += 1
        else:
            conteo[palabra] = 1
    
    return conteo
            
oracion = conteoPalabras("hola devzen saludos a todos los cibernautas que estan en el desarrollo de apps hola a otros devzen")
print(oracion)

