import random

tablero = [
[0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0]
]
contador = 0

while contador !=5:
    f = random.randint(0,4)
    c = random.randint(0,4)

    if tablero[f][c] == 0:
        tablero[f][c] = 1
        contador += 1

for fila in tablero:
    for elemento in fila:
        print(elemento, end=" ")
    print()
