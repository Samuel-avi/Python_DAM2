import random

rn = random.randint(1, 50)
guess = int()
cont = 1
while guess != rn:
    guess= int(input("elije un numero: "))
    if cont == 5:
        print("perdiste, el numero era", rn)
        break
    if guess == rn:
        print("acertaste!!!")
    else:
        cont += 1
        if rn > guess:
            print("el numero era mayor")
        else:
            print("el numero era menor")



