edad = 22
if edad == 60:
    print("Ya deberías estar jubilado")
elif edad == 20:
    print("A trabajar!!!")
else:
    pass
print("Fin del programa")

for d in range(0, 50, 8):
    print(d,)

for n in range(0,5):
    print(n,)

for ne in range(0,50,5):
    print(ne,)


for c in "Hola mundo":
    print(c, end=" ")

i = 0
while i < 10:
    print(i)
    i+=1

# for c in texto

texto = "hola mundo"
for i in range (0,len(texto)):
    print(i, " - ", texto[i])

print(texto[3:8]) # :8 --> desde la primera hasta la 7, 3: ---> desde la tercera hasta la última

print(texto[-2]) # empieza a contar desde el final de la cadena

#clase String

print(texto.upper())
print(texto.lower())
print(texto.swapcase())
print(texto[2:].find("o"))
print(texto.count("o"))
print(texto.replace("mun", "MUN"))

#tex = texto.__reversed__()
#print(tex)

opcion = input("P para jugac C para cofigurar o X para dsalir: ")

match opcion:
    case "P" | "p":
        print("Has elegido jugar")
    case "C" | "c":
        print("Has elegido configurar")
    case "X" | "x":
        print("Has elegido salir")
    case _:
        print("Opcion no valida")
print("Fin del menú")



























