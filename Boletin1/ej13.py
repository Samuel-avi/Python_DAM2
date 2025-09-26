import random

numdados = int(input("Cuantos dados vas a tirar: "))

while True:

    numcaras = int(input("Cuantas caras tiene el dado: "))

    if  numcaras%2 == 0:
        break
    else:
        print("El número de caras no puede ser impar")

for _ in range(0,numdados):
    print(random.randint(1,numcaras))