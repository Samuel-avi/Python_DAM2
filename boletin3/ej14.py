import re

NIF = input("Ingresa un NIF: ")

num = ""
letras = "TRWAGMYFPDXBNJZSQVHLCKE"

regexNIF = r"^[0-9]{8}[A-ZÑa-zñ]$"

resultado = re.fullmatch(regexNIF, NIF)

if resultado:
    num = NIF[:8]
    letra = NIF[-1]

letra_correcta = letras[int(num) % 23]


if letra.capitalize() == letra_correcta:
    print("La letra del NIF es la correcta")
else:
    print("La letra del NIF es incorrecta")
