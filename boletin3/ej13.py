import re

Matricula = input("Ingresa una matrícula: ")

regex_matricula = r"^[0-9]{4}[ ]?[A-PR-Z]{3}$"
resultado = re.fullmatch(regex_matricula, Matricula)

print("La matrícula es correcta" if resultado else "La matrícula es icorrecta")