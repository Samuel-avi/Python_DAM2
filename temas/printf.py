# -*- coding: utf-8 -*-
"""
APUNTES DE PRINTF EN PYTHON
Incluye: formateo de cadenas al estilo printf
"""

# ========================================
# 2️⃣ Formateo tipo printf
# ========================================

# %s → cadena
# %d → entero
# %f → flotante
# %.2f → flotante con 2 decimales
# %% → símbolo de porcentaje

nombre = "Ana"
edad = 25
altura = 1.732

print("Hola %s, tienes %d años y mides %.2f metros" % (nombre, edad, altura))
print("Porcentaje completado: %.1f%%" % 75.5)
print("-" * 40)

# 2️⃣1 Alternativa moderna: str.format()
print("Hola {}, tienes {} años y mides {:.2f} metros".format(nombre, edad, altura))

# 2️⃣2 F-strings (Python 3.6+)
print(f"Hola {nombre}, tienes {edad} años y mides {altura:.2f} metros")
print("-" * 40)

# 2️⃣3 Formateo de alineación
print("Nombre: %-10s Edad: %03d" % (nombre, edad))  # izquierda, entero con ceros a la izquierda
print("Nombre: {:<10} Edad: {:03}".format(nombre, edad))  # con format
print(f"Nombre: {nombre:<10} Edad: {edad:03}")          # con f-string
