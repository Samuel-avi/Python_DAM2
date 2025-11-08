# -*- coding: utf-8 -*-
"""
APUNTES DE TUPLAS EN PYTHON
Incluye: creación, acceso, conversión, mutabilidad interna, pertenencia y desempaquetado.
"""

import random

# ----------------------------------------
# 1️⃣ Creación de tuplas
# ----------------------------------------
tupla = (1, 2, 3, 4, 5)
tupla2 = ("hola", "mundo")
tupla3 = (23, "hola", False, tupla, [1, 2, 3])
tupla5 = ("uno",)  # tupla de un solo elemento

print("Tupla7 (sin paréntesis):", "hola", tupla6 := tuple(list(tupla)), "mundo") # tupla creada sin paréntesis

# ----------------------------------------
# 2️⃣ Conversión entre tuplas y listas
# ----------------------------------------
lista = list(tupla)
print("Lista a partir de tupla:", lista)

texto = str(tupla2)
print("Tupla convertida a texto:", texto)

tupla6 = tuple(lista)
print("Lista convertida nuevamente a tupla:", tupla6)

# ----------------------------------------
# 3️⃣ Acceso y mutabilidad interna
# ----------------------------------------
print("Lista dentro de tupla3:", tupla3[4])
tupla3[4][2] = 5  # modifica la lista interna
print("Lista modificada dentro de tupla3:", tupla3[4])

# ----------------------------------------
# 4️⃣ Comprobación de pertenencia
# ----------------------------------------
if 4 in tupla:
    print("4 está en la tupla")
if 6 not in tupla:
    print("6 no está en la tupla")

# ----------------------------------------
# 5️⃣ Desempaquetado de tuplas
# ----------------------------------------
profesor = ("José María", "Morales", 57, False, True)
nombre, apellidos, edad, alumno, profe = profesor
print("Nombre y edad del profesor:", nombre, edad)

# ----------------------------------------
# 6️⃣ Elemento aleatorio de tupla
# ----------------------------------------
print("Elemento aleatorio de tupla:", random.choice(tupla))
