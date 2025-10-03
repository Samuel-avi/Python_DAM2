import random

while True:
    num = random.randint(10000000, 50000000)
    if num < 2:
        print("No es primo")
    elif num == 2:
        print(num)
        break
    else:
        es_primo = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                es_primo = False
                break
        if es_primo:
            print(num)
            break