# ====================================================
# APUNTES DE CONDICIONALES, BUCLES Y CADENAS EN PYTHON
# ====================================================

# --- Condicionales ---
edad = 22

if edad == 60:
    print("Ya deberías estar jubilado")
elif edad == 20:
    print("A trabajar!!!")
else:
    print("Edad no contemplada")

print("Fin del programa\n")

# --- Bucles for con range() ---

# range(inicio, fin, paso)
for d in range(0, 50, 8):
    print(d)
print()  # salto de línea

for n in range(5):  # range(0, 5) es equivalente
    print(n)
print()

for numero in range(0, 50, 5):
    print(numero)
print()

# --- Recorrer una cadena ---
for caracter in "Hola mundo":
    print(caracter, end=" ")
print("\n")

# --- Bucle while ---
i = 0
while i < 10:
    print(i)
    i += 1
print()

# --- Ejemplo: recorrer un texto por índice ---
texto = "hola mundo"

for i in range(len(texto)):
    print(i, "-", texto[i])
print()

# --- Slicing de cadenas ---
print(texto[3:8])   # desde el índice 3 hasta el 7
print(texto[-2])    # segundo carácter desde el final
print()

# --- Métodos de clase String ---
print(texto.upper())              # mayúsculas
print(texto.lower())              # minúsculas
print(texto.swapcase())           # invierte mayúsculas/minúsculas
print(texto[2:].find("o"))        # busca "o" desde el índice 2
print(texto.count("o"))           # cuenta cuántas "o" hay
print(texto.replace("mun", "MUN"))  # reemplaza subcadena
print()

# --- Bucle anidado (ejemplo adicional) ---
for fila in range(3):
    for columna in range(2):
        print(f"Fila {fila}, Columna {columna}")
print()

# --- Ejemplo de control de flujo con continue y break ---
for i in range(6):
    if i == 3:
        continue  # salta el número 3
    if i == 5:
        break     # termina el bucle al llegar a 5
    print(i)
print()

# --- Estructura match-case (Python 3.10+) ---
opcion = input("P para jugar, C para configurar o X para salir: ")

match opcion.lower():  # convierte a minúsculas para simplificar
    case "p":
        print("Has elegido jugar")
    case "c":
        print("Has elegido configurar")
    case "x":
        print("Has elegido salir")
    case _:
        print("Opción no válida")

print("Fin del menú")
