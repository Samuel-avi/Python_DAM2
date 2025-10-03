n1 = int(input("Escribe el primer número: "))
n2 = int(input("Escribe el segundo número: "))

a, b = min(n1, n2), max(n1, n2)

for num in range(a, b):
    if num == 1:
        continue
    elif num == 2:
        print(num)
    else:
        es_primo = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                es_primo = False
                break
        if es_primo:
            print(num)