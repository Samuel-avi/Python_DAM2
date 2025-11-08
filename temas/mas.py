# -*- coding: utf-8 -*-
"""
APUNTES DE MÉTODOS DE COMPROBACIÓN DE CADENAS EN PYTHON
Incluye: isalpha, isdigit, isdecimal, isnumeric, isalnum, isspace, isprintable.
"""

# =====================================================
# Conversión de números a cadena
# =====================================================
cadenaNum = str(257.53)  # convierte números a string
print("Número convertido a cadena:", cadenaNum)
print("Tipo de dato:", type(cadenaNum))
print("-" * 40)

# =====================================================
# Ejemplo base
# =====================================================
cadena = "hola mundo"
print("Cadena:", repr(cadena))
print("isalpha():", cadena.isalpha())  # Falso porque tiene espacio
print("-" * 40)

# =====================================================
# 1️⃣ .isalpha() → True si solo hay letras
# =====================================================
print("'Hola'.isalpha() =", "Hola".isalpha())        # ✅ True
print("'Hola123'.isalpha() =", "Hola123".isalpha())  # ❌ False
print("'Hola Mundo'.isalpha() =", "Hola Mundo".isalpha())  # ❌ False (espacio)
print("-" * 40)

# =====================================================
# 2️⃣ .isdigit() → True si solo hay dígitos (0–9)
# =====================================================
print("'12345'.isdigit() =", "12345".isdigit())      # ✅ True
print("'12.45'.isdigit() =", "12.45".isdigit())      # ❌ False (punto no es dígito)
print("-" * 40)

# =====================================================
# 3️⃣ .isdecimal() → True si solo hay números decimales base 10
# =====================================================
print("'123'.isdecimal() =", "123".isdecimal())      # ✅ True
print("'½'.isdecimal() =", "½".isdecimal())          # ❌ False
print("-" * 40)

# =====================================================
# 4️⃣ .isnumeric() → True si hay caracteres numéricos (fracciones, romanos, etc.)
# =====================================================
print("'123'.isnumeric() =", "123".isnumeric())      # ✅ True
print("'Ⅻ'.isnumeric() =", "Ⅻ".isnumeric())          # ✅ True (número romano)
print("'½'.isnumeric() =", "½".isnumeric())          # ✅ True (fracción)
print("-" * 40)

# =====================================================
# 5️⃣ .isalnum() → True si hay letras y/o números (sin espacios ni símbolos)
# =====================================================
print("'Hola123'.isalnum() =", "Hola123".isalnum())  # ✅ True
print("'Hola 123'.isalnum() =", "Hola 123".isalnum())# ❌ False (espacio)
print("'Hola_123'.isalnum() =", "Hola_123".isalnum())# ❌ False (guion bajo)
print("-" * 40)

# =====================================================
# 6️⃣ .isspace() → True si solo hay espacios, tabulaciones o saltos de línea
# =====================================================
print("'   '.isspace() =", "   ".isspace())          # ✅ True
print("'Hola'.isspace() =", "Hola".isspace())        # ❌ False
print("'\n\t'.isspace() =", "\n\t".isspace())        # ✅ True
print("-" * 40)

# =====================================================
# 7️⃣ .isprintable() → True si todos los caracteres son imprimibles
# =====================================================
print("'Hola mundo'.isprintable() =", "Hola mundo".isprintable())  # ✅ True
print("'Hola\\nMundo'.isprintable() =", "Hola\nMundo".isprintable()) # ❌ False (salto de línea no imprimible)
print("-" * 40)
