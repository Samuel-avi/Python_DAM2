import random

numdados = int(input("Cuantos dados vas a tirar: "))
numcaras = int(input("Cuantas caras tiene el dado: "))

for _ in range(0,numdados):
    print(random.randint(1,numcaras))