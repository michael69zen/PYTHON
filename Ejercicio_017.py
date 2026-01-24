frase = input("DIGITE LA FRASE: ")
frase.lower()

contador = 0

vocales = "aeiou"
for i in frase:
    if i in vocales:
        contador += 1

print(f"La frase tiene {contador} vocales")

