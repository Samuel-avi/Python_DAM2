# -*- coding: utf-8 -*-
"""
APUNTES DE LISTAS EN PYTHON
Incluye: creación, acceso, recorrido, métodos, concatenación y listas anidadas.
"""

# ========================================
# 1️⃣ Creación de listas
# ========================================
lista = []                 # Lista vacía
lista2 = list()            # Otra forma de crear lista vacía
lista3 = [2, 4, 5, 6, 7, 12, 6, 6]
lista4 = [23, "hola", False, lista3, [1, 2, 3]]

print("Lista 3:", lista3)
print("Lista 4 (mixta):", lista4)
print("-" * 40)

# ========================================
# 2️⃣ Agregar y concatenar elementos
# ========================================
lista.append("Nuevo elemento")
print("Lista después de append:", lista)

lista5 = lista + [23, 6]  # concatenación
print("Lista concatenada:", lista5)
print("-" * 40)

# ========================================
# 3️⃣ Métodos de eliminación y extracción
# ========================================
print("Lista3 original:", lista3)
valor_extraido = lista3.pop(3)  # extrae el elemento en índice 3
print("Elemento extraído:", valor_extraido)
print("Lista3 después de pop:", lista3)

lista3.remove(5)  # elimina el primer valor "5" que encuentra
print("Después de remove(5):", lista3)
print("-" * 40)

# ========================================
# 4️⃣ Ordenar y modificar elementos
# ========================================
lista3.sort()  # ordena la lista (ascendente)
print("Lista ordenada:", lista3)

# lista3.sort(reverse=True)  # orden descendente (opcional)
lista3.insert(2, 10)  # inserta el valor 10 en la posición 2
print("Lista con insert:", lista3)
print("-" * 40)

# ========================================
# 5️⃣ Otras operaciones útiles
# ========================================
print("Cantidad de veces que aparece el 6:", lista3.count(6))
print("Primera posición del 6:", lista3.index(6))

# concatenar con otra lista
# lista3.extend(lista4)
# print("Lista extendida:", lista3)

texto = str(lista3)
print("Lista convertida a texto:", texto)
print("-" * 40)

# ========================================
# 6️⃣ Convertir texto a lista de caracteres
# ========================================
texto2 = "hola mundo"
listatexto = list(texto2)
print("Texto convertido en lista de caracteres:", listatexto)
print("-" * 40)

# ========================================
# 7️⃣ Listas anidadas (matriz)
# ========================================
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print("Elemento en fila 2, columna 3:", matriz[1][2])
print("-" * 40)

# ========================================
# 8️⃣ Slicing y comprobación de pertenencia
# ========================================
print("Sublista [4:5]:", lista3[4:5])  # slicing
if 4 in lista3:  # también se puede usar "not in"
    print("El número 4 está en la lista")
else:
    print("El número 4 no está en la lista")
print("-" * 40)

# ========================================
# 9️⃣ Recorrido de listas (ejemplos adicionales)
# ========================================
print("Recorrido de lista3:")
for elemento in lista3:
    print(" -", elemento)

print("\nRecorrido con índice:")
for i in range(len(lista3)):
    print(i, "-", lista3[i])

# También podrías convertir la lista en cadena separada por espacios:
cadena = " ".join(map(str, lista3))
print("\nLista convertida a cadena:", cadena)
