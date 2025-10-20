# -*- coding: utf-8 -*-
"""
Resumen de funciones del módulo math en Python
Incluye ejemplos y resultados
Autor: ChatGPT
"""

import math

print("=== Funciones del módulo math ===\n")

# 1️⃣ math.sqrt(x) → raíz cuadrada
x = 16
print(f"math.sqrt({x}) = {math.sqrt(x)}")  # 4.0

# 2️⃣ math.pow(x, y) → potencia x^y
x, y = 2, 3
print(f"math.pow({x}, {y}) = {math.pow(x, y)}")  # 8.0

# 3️⃣ math.factorial(n) → factorial
n = 5
print(f"math.factorial({n}) = {math.factorial(n)}")  # 120

# 4️⃣ math.ceil(x) → redondeo hacia arriba
x = 3.2
print(f"math.ceil({x}) = {math.ceil(x)}")  # 4

# 5️⃣ math.floor(x) → redondeo hacia abajo
x = 3.8
print(f"math.floor({x}) = {math.floor(x)}")  # 3

# 6️⃣ math.fabs(x) → valor absoluto
x = -5.2
print(f"math.fabs({x}) = {math.fabs(x)}")  # 5.2

# 7️⃣ Funciones trigonométricas (radianes)
x = math.pi / 2
print(f"math.sin({x}) = {math.sin(x)}")  # 1.0
print(f"math.cos({x}) = {math.cos(x)}")  # 6.123233995736766e-17 (≈0)
print(f"math.tan({x}) = {math.tan(x)}")  # 1.633123935319537e+16 (≈∞)
