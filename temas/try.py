# -*- coding: utf-8 -*-
"""
APUNTES DE MANEJO DE ERRORES EN PYTHON
Incluye: try, except, else, finally y raise
"""

# ========================================
# 1️⃣ Básico: try / except
# ========================================
try:
    a = 10
    b = 0
    resultado = a / b  # Esto genera un ZeroDivisionError
except ZeroDivisionError:
    print("Error: No se puede dividir por cero")
print("-" * 40)

# ========================================
# 2️⃣ Capturar múltiples excepciones
# ========================================
try:
    lista = [1, 2, 3]
    print(lista[5])  # IndexError
    x = 10 / 0      # ZeroDivisionError
except (IndexError, ZeroDivisionError) as e:
    print("Se produjo un error:", e)
print("-" * 40)

# ========================================
# 3️⃣ Usar except genérico
# ========================================
try:
    valor = int("abc")  # ValueError
except Exception as e:
    print("Error genérico:", e)
print("-" * 40)

# ========================================
# 4️⃣ else → se ejecuta si no hay excepción
# ========================================
try:
    a = 10
    b = 2
    resultado = a / b
except ZeroDivisionError:
    print("Error: división por cero")
else:
    print("División correcta:", resultado)
print("-" * 40)

# ========================================
# 5️⃣ finally → se ejecuta siempre
# ========================================
try:
    archivo = open("archivo_inexistente.txt", "r")
except FileNotFoundError:
    print("Archivo no encontrado")
finally:
    print("Esto se ejecuta siempre, haya error o no")
print("-" * 40)

# ========================================
# 6️⃣ Levantar excepciones con raise
# ========================================
def dividir(a, b):
    if b == 0:
        raise ValueError("El divisor no puede ser 0")
    return a / b

try:
    resultado = dividir(10, 0)
except ValueError as e:
    print("Error personalizado:", e)
print("-" * 40)

# ========================================
# 7️⃣ Ejemplo práctico combinado
# ========================================
def pedir_entero():
    while True:
        try:
            valor = int(input("Ingresa un número entero: "))
        except ValueError:
            print("¡Eso no es un número entero! Intenta de nuevo.")
        else:
            print("Número correcto:", valor)
            break
        finally:
            print("Intento finalizado")
# pedir_entero()  # Descomenta para probar
