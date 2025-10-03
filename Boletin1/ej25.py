num = float(input("Escribe un número: "))

while num >= 1:
    if num.is_integer():
        print(round(int(num)))
    else:
        print(round(num, 2))
    num = num/2