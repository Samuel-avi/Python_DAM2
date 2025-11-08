# ========================================
# APUNTES SOBRE CONJUNTOS (SETS) EN PYTHON
# ========================================

# Los conjuntos son colecciones SIN orden y SIN elementos duplicados.

# --- Definición de conjuntos ---
profesorPrimero = {"Ana", "Juan Carlos", "Sancho", "Natalia"}
print("Profesores de primero:", profesorPrimero)

profesorSegundo = set(["Agustin", "Ana", "Natalia", "Javier", "José María"])
print("Profesores de segundo:", profesorSegundo)

# --- Unión de conjuntos ---
print("\n--- UNIÓN ---")
print(profesorPrimero | profesorSegundo)
print(profesorPrimero.union(profesorSegundo))
# Muestra los elementos de ambos conjuntos sin duplicados.

# --- Intersección de conjuntos ---
print("\n--- INTERSECCIÓN ---")
print(profesorPrimero & profesorSegundo)
print(profesorPrimero.intersection(profesorSegundo))
# Muestra los elementos que están en ambos conjuntos.

# --- Diferencia de conjuntos ---
print("\n--- DIFERENCIA ---")
print(profesorPrimero - profesorSegundo)
print(profesorPrimero.difference(profesorSegundo))
# Muestra los elementos que están en profesorPrimero pero no en profesorSegundo.

# --- Diferencia simétrica ---
print("\n--- DIFERENCIA SIMÉTRICA ---")
print(profesorPrimero ^ profesorSegundo)
print(profesorPrimero.symmetric_difference(profesorSegundo))
# Muestra los elementos que están en uno u otro conjunto, pero no en ambos.

# --- Comprobación de pertenencia ---
if "Ana" in profesorPrimero:
    print("\nAna es profesora de primero.")
if "Sancho" not in profesorSegundo:
    print("Sancho no es profesor de segundo.")

# --- Recorrer un conjunto ---
print("\n--- RECORRER ELEMENTOS ---")
for elemento in profesorPrimero:
    print(elemento)

# --- Tamaño del conjunto ---
print("\nCantidad de profesores en primero:", len(profesorPrimero))

# --- Métodos de modificación ---
print("\n--- MODIFICACIÓN DE CONJUNTOS ---")

profesorPrimero.add("José María")
print("Añadido 'José María':", profesorPrimero)

profesorPrimero.remove("José María")  # Lanza error si no existe
profesorPrimero.discard("José María")  # No lanza error
print("Después de eliminar 'José María':", profesorPrimero)

profe = profesorPrimero.pop()  # Elimina y devuelve un elemento aleatorio
print("Se eliminó:", profe)

profesorPrimero.clear()  # Borra todos los elementos
print("Set vacío:", profesorPrimero)

# --- Otros ejemplos ---
print("\n--- OTROS EJEMPLOS ---")
conjunto = set([1, 2, 3, 3, 4, 5, 6])
print("Conjunto sin duplicados:", conjunto)

conjunto2 = set("hola mundo cruel")
print("Conjunto a partir de texto:", conjunto2)

# --- Conversiones ---
profesorPrimero = {"Ana", "Juan Carlos", "Sancho", "Natalia"}  # restauramos

lista = list(profesorPrimero)
print("\nConvertido a lista:", lista)

tupla = tuple(profesorSegundo)
print("Convertido a tupla:", tupla)

texto = str(profesorSegundo)
print("Convertido a texto:", texto)
