import random

d1 = 0
d2 = 1
i = 0

while d1 != d2:
    d1 = random.randint(1,6)
    d2 = random.randint(1, 6)
    i += 1
    print(d1, d2)

print("Los dados han tardado", i, "intentos y ha salido", d1)