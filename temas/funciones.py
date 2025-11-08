# -*- coding: utf-8 -*-
"""
APUNTES DE FUNCIONES EN PYTHON
Incluye: definición, argumentos, retorno de valores, parámetros por defecto, args, kwargs, funciones lambda y alcance de variables.
"""

# ========================================
# 1️⃣ Definición básica de función
# ========================================

def saludar():
    """Función que imprime un saludo"""
    print("¡Hola mundo!")

saludar()  # Llamada a la función
print("-" * 40)

# ========================================
# 2️⃣ Función con parámetros
# ========================================

def saludar_persona(nombre):
    """Saluda a la persona cuyo nombre se recibe como parámetro"""
    print(f"¡Hola {nombre}!")

saludar_persona("Ana")
saludar_persona("Juan")
print("-" * 40)

# ========================================
# 3️⃣ Función con retorno de valores
# ========================================

def sumar(a, b):
    """Devuelve la suma de dos números"""
    return a + b

resultado = sumar(5, 7)
print("Suma:", resultado)
print("-" * 40)

# ========================================
# 4️⃣ Parámetros por defecto
# ========================================

def saludar_persona2(nombre="Amigo"):
    """Saluda a la persona, usando un valor por defecto"""
    print(f"¡Hola {nombre}!")

saludar_persona2("Luis")
saludar_persona2()  # usa el valor por defecto
print("-" * 40)

# ========================================
# 5️⃣ Funciones con *args (argumentos variables)
# ========================================

def sumar_todos(*numeros):
    """Suma cualquier cantidad de números"""
    total = 0
    for num in numeros:
        total += num
    return total

print("Suma de varios números:", sumar_todos(1, 2, 3, 4, 5))
print("-" * 40)

# ========================================
# 6️⃣ Funciones con **kwargs (argumentos con nombre)
# ========================================

def mostrar_info(**info):
    """Muestra información pasada con nombre"""
    for clave, valor in info.items():
        print(f"{clave}: {valor}")

mostrar_info(nombre="Ana", edad=25, ciudad="Madrid")
print("-" * 40)

# ========================================
# 7️⃣ Funciones anidadas
# ========================================

def externa():
    print("Función externa")
    def interna():
        print("Función interna")
    interna()

externa()
print("-" * 40)

# ========================================
# 8️⃣ Funciones lambda (funciones anónimas)
# ========================================

# Función lambda que suma dos números
sumar_lambda = lambda a, b: a + b
print("Suma con lambda:", sumar_lambda(10, 15))

# Lambda en combinación con map
numeros = [1, 2, 3, 4, 5]
cuadrados = list(map(lambda x: x**2, numeros))
print("Cuadrados usando lambda + map:", cuadrados)
print("-" * 40)

# ========================================
# 9️⃣ Alcance de variables (scope)
# ========================================

x = 10  # variable global

def funcion_scope():
    x = 5  # variable local
    print("Variable local x:", x)

funcion_scope()
print("Variable global x:", x)
print("-" * 40)

# ========================================
# 🔟 Función con return múltiple
# ========================================

def operaciones(a, b):
    """Devuelve suma, resta, multiplicación y división"""
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b if b != 0 else None
    return suma, resta, multiplicacion, division

res = operaciones(10, 2)
print("Resultados de operaciones:", res)

# Desempaquetado
suma, resta, multi, div = operaciones(20, 5)
print("Suma:", suma, "Resta:", resta, "Multiplicación:", multi, "División:", div)
