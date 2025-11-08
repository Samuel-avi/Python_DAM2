# -*- coding: utf-8 -*-
"""
APUNTES DE REGEX EN PYTHON
Incluye: expresiones regulares (regex) con el módulo re
"""

# ========================================
# 1️⃣ Expresiones regulares (regex) con re
# ========================================

import re

# 1️⃣1 Buscar un patrón en una cadena
texto = "Mi correo es ejemplo@gmail.com"
patron = r"\w+@\w+\.\w+"  # patrón para detectar correos
resultado = re.search(patron, texto)
print("Correo encontrado:", resultado.group() if resultado else "No encontrado")
print("-" * 40)

# 1️⃣2 Encontrar todas las coincidencias
texto2 = "Los números son 23, 45, 67 y 89"
patron_num = r"\d+"  # \d+ → uno o más dígitos
numeros = re.findall(patron_num, texto2)
print("Números encontrados:", numeros)
print("-" * 40)

# 1️⃣3 Reemplazar texto usando regex
texto3 = "Mi número es 123-456-789"
nuevo_texto = re.sub(r"\d", "X", texto3)  # reemplaza todos los dígitos por X
print("Texto modificado:", nuevo_texto)
print("-" * 40)

# 1️⃣4 Dividir texto usando un patrón
texto4 = "manzana,pera;naranja uva"
frutas = re.split(r"[,; ]", texto4)  # separa por coma, punto y coma o espacio
print("Lista de frutas:", frutas)
print("-" * 40)

# 1️⃣5 Validar patrones con match
email = "usuario@dominio.com"
if re.fullmatch(r"\w+@\w+\.\w+", email):
    print("Email válido")
else:
    print("Email no válido")
print("-" * 40)

# ========================================
# 1️⃣ Coincidencia de caracteres
# ========================================
texto = "Hola mundo 123"

# [abc] → coincide con cualquiera de los caracteres a, b o c
print(re.findall(r"[Hh]ola", texto))  # ['Hola']

# [0-9] → cualquier dígito
print(re.findall(r"[0-9]", texto))    # ['1', '2', '3']

# [a-z] → cualquier letra minúscula
print(re.findall(r"[a-z]", texto))    # todas las letras minúsculas

# [A-Za-z0-9] → letras y números
print(re.findall(r"[A-Za-z0-9]", texto))
print("-" * 40)

# ========================================
# 2️⃣ Metacaracteres
# ========================================
# . → cualquier carácter excepto salto de línea
print(re.findall(r"H.la", texto))     # ['Hola']

# ^ → inicio de cadena
print(re.findall(r"^Hola", texto))    # ['Hola']

# $ → fin de cadena
print(re.findall(r"123$", texto))     # ['123']

# \d → dígito [0-9]
print(re.findall(r"\d+", texto))      # ['123']

# \D → no dígito
print(re.findall(r"\D+", texto))      # ['Hola mundo ']

# \w → carácter alfanumérico [A-Za-z0-9_]
print(re.findall(r"\w+", texto))      # ['Hola', 'mundo', '123']

# \W → no alfanumérico
print(re.findall(r"\W+", texto))      # [' ', ' ']

# \s → espacio en blanco (espacio, tab, salto de línea)
print(re.findall(r"\s+", texto))      # [' ', ' ']

# \S → no espacio
print(re.findall(r"\S+", texto))      # ['Hola', 'mundo', '123']
print("-" * 40)

# ========================================
# 3️⃣ Cantidad de repeticiones
# ========================================
texto2 = "aa abc aaaa aab"

# * → 0 o más repeticiones
print(re.findall(r"aa*", texto2))     # ['aa', 'aa', 'aaaa', 'aa']

# + → 1 o más repeticiones
print(re.findall(r"aa+", texto2))     # ['aa', 'aa', 'aaaa', 'aa']

# ? → 0 o 1 repetición
print(re.findall(r"aa?", texto2))     # ['aa', 'aa', 'aa', 'aa']

# {n} → exactamente n repeticiones
print(re.findall(r"a{2}", texto2))    # ['aa', 'aa', 'aa', 'aa']

# {n,m} → entre n y m repeticiones
print(re.findall(r"a{2,3}", texto2))  # ['aa', 'aa', 'aaa', 'aa']
print("-" * 40)

# ========================================
# 4️⃣ Patrones especiales útiles
# ========================================
correo = "usuario123@dominio.com"

# Validar email simple
patron_email = r"\w+@\w+\.\w+"
print("Email válido?" , bool(re.fullmatch(patron_email, correo)))

# Teléfono simple (123-456-789)
telefono = "123-456-789"
patron_tel = r"\d{3}-\d{3}-\d{3}"
print("Teléfono válido?", bool(re.fullmatch(patron_tel, telefono)))

# URL simple
url = "https://www.ejemplo.com"
patron_url = r"https?://\w+\.\w+(\.\w+)?"
print("URL válida?", bool(re.fullmatch(patron_url, url)))
print("-" * 40)

# ========================================
# 5️⃣ Grupos y paréntesis
# ========================================
texto3 = "Juan 25, Ana 30, Pedro 28"
patron = r"(\w+) (\d+)"
print(re.findall(patron, texto3))  # [('Juan', '25'), ('Ana', '30'), ('Pedro', '28')]

# Acceder a grupos con search
resultado = re.search(patron, texto3)
print("Primer nombre:", resultado.group(1))
print("Edad:", resultado.group(2))
