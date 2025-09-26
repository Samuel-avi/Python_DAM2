n = int(input("Dime un número: "))

print(f"Los divisores de {n} son:")
for i in range(1, n + 1):
    if n % i == 0:
        print(i)

# Un número i es divisor de n si al dividir n entre i el resto es 0