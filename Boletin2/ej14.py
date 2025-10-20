import random
import sys

rn = random.randint(1, 50)
guess = int()
cont = 1
jugar = True
while jugar:
    while guess != rn:
        guess = int(input("elije un numero: "))
        if cont == 5:
            print("perdiste, el numero era", rn)
            break
        if guess == rn:
            print("acertaste!!!")
        else:
            cont += 1
            if rn > guess:
                print("el numero es mayor")
            else:
                print("el numero es menor")
    while True:
        otra = input("Quieres jugar de nuevo? si/no\n> ")
        if otra != "si" and otra != "no":
            print("opcion invalida")
            continue
        if otra == "si":
            cont = 1
            break
        if otra == "no":
            sys.exit()
