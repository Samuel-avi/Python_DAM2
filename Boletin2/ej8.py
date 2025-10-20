num = int(input("Num por teclado:"))
div = list()

for i in range(1, num + 1):
    if num % i == 0:
        div.append(i)

print("Divisores del número", num, ":", *div) # * es desempaquetador
