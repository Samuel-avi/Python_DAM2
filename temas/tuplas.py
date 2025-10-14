tupla = (1,2,3,4,5)

tupla2 = ("hola", "mundo")

tupla3 = (23, "hola", False, tupla, [1,2,3])

tupla5 = ("uno",) # sin , no lo reconoce como tupla

lista = list(tupla)

texto = str(tupla2)

tupla6 = tuple(lista)

tupla7 = "hola", tupla6, "mundo" #sin parentesis crea tupla funciona con () tambien

print(tupla7)

print(tupla3[4])
tupla3[4][2] = 5 #no se modifica la tupla, se modifica la lista
print(tupla3[4])

if 4 in tupla:
    print("si")
if 6 not in tupla:
    print("no")

profesor = ("José María", "Morales", 57, False, True)
nombre, apellidos, edad, alumno, profe = profesor

print(nombre, edad)

import random




