#Ya estaba bien en el 14
import random

while True:
    n1 = int(input("Dime un número: "))
    n2 = int(input("Dime un número: "))

    if n1 == n2:
        print("No pueden ser el mismo número")
    else: break

if n1 > n2:
    print(random.randint(n2,n1))
else:
    print(random.randint(n1,n2))