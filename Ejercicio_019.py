contrasenia = input("DIGITE SU PASSWORD: ")

mayusculas = False
minusculas = False
numeros = False
caracteres = False

for i in contrasenia:
    if i.islower():
        minusculas = True
    elif i.isupper():
        mayusculas = True
    elif i.isdigit():
        numeros = True
    else:
        caracteres = True

if len(contrasenia) >= 8 and mayusculas and minusculas and numeros and caracteres:
    print("Password seguro")
else:
    print("Password invalido")
