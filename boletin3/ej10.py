import re

NIF = input("Ingresa un NIF: ")

regexNIF = r"^[0-9]{8}[A-ZÑa-zñ]$"

resultado = re.fullmatch(regexNIF, NIF)

print("El NIF es correcto" if resultado else "El NIF es icorrecto")

