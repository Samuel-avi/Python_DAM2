fecha = input("Dame una fecha: ")

valor = fecha.split("/")
bisiesto = False

valor_mes = [30, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


if len(valor) == 3 and all(v.isdigit() for v in valor):
    dia = int(valor[0])
    mes = int(valor[1])
    year = int(valor[2])

    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        bisiesto = True
        valor_mes[1] = 29

    esbisiesto = "Es bisiesto" if bisiesto else "No es bisiesto"

    if 1 <= mes <= 12:
        if 0 <= dia <= (valor_mes[mes-1]):
            print("La fecha", fecha, "es correcta y el año", year, esbisiesto)
        else:
            print("La fecha no es correcta")
    else:
        print("La fecha no es correcta")
else:
    print("La fecha no es correcta")
