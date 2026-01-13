#Ejercicio 002
'''Desarrollar un programa que diga si estas bien economicamente segun los siguientes criterios: ingreso mensual, gastos mensuales.'''

ingreso_mensual = int(input("DIGITE SU INGRESO MENSUAL EN $: "))
gastos_mensuales = int(input("DIGITE SUS GASTOS MENSUALES EN $: "))

if ingreso_mensual >= 10000:
    if ingreso_mensual - gastos_mensuales < 0:
        print("Ud esta en deficit.")
    elif ingreso_mensual - gastos_mensuales > 3000:
        print("Ud esta bien economicamente en el mundo.")
    else:
        print("Estas gastando demasiado. No te alcanza para sobrevivir en el primermundo.")
elif ingreso_mensual > 3000:
    if ingreso_mensual - gastos_mensuales < 0:
        print("Ud esta en deficit.")
    elif ingreso_mensual - gastos_mensuales > 1500:
        print("Ud esta bien economicamente en latinoamerica.")
    else:
        print("Estas gastando demasiado.No te alcanza para sobrevivir en latinoamerica.")
elif ingreso_mensual > 1500:
    if ingreso_mensual - gastos_mensuales < 0:
        print("Ud esta en deficit.")
    elif ingreso_mensual - gastos_mensuales > 700:
        print("Ud esta bien economicamente en su pais.")
    else:
        print("Estas gastando demasiado.No te alcanza para sobrevivir en su pais.")
elif ingreso_mensual > 500:
    if ingreso_mensual - gastos_mensuales < 0:
        print("Ud esta en deficit.")
    elif ingreso_mensual - gastos_mensuales > 300:
        print("Ud esta bien economicamente en venezuela.")
    else:
        print("Estas gastando demasiado.No te alcanza para sobrevivir en venezuela.")
else:
    print("Ud esta muy mal economicamente.")
