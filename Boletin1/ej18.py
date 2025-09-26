import random

i = 0
while True:
    n = random.randint(1,1000)
    print(n)
    i += 1
    if n == 666:
        break
print("¡Faltan", i, "días para que se acabe todo! ")