nota1 = float(input("Primera nota: "))
nota2 = float(input("Segunda nota: "))

if 0 < nota1 < 10 or 0 < nota2 < 10:
    media = (nota1 + nota2) / 2
    round(media, 0)
    print(int(media))
else:
    print("notas no validas")