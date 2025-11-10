import re

NIF_NIE = input("Ingresa un NIF o NIE: ")

regexNIF = r"^[0-9]{8}[A-ZÑa-zñ]$"
regexNIE = r"^[XYZxyz]{1}[0-9]{7}[A-ZÑa-zñ]$"

resultadoNIF = re.fullmatch(regexNIF, NIF_NIE)
resultadoNIE = re.fullmatch(regexNIE, NIF_NIE)

es_NIF = "Es un NIF correcto" if resultadoNIF else "El NIF es icorrecto"
es_NIE = "Es un NIE correcto" if resultadoNIE else "El NIE es icorrecto"


if resultadoNIF:
    print(es_NIF)
elif resultadoNIE:
    print(es_NIE)
else:
    print("No es ni un NIE ni un NIF correcto")
