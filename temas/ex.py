valor = 2

match valor:
    case 1:
        print("Valor es 1")
    case 2:
        print("Valor es 2")
    case 3 | 4:  # varias opciones
        print("Valor es 3 o 4")
    case _:      # caso por defecto (como else)
        print("Otro valor")
# -*- coding: utf-8 -*-
"""
Ejemplo completo: Modificación y manejo de cadenas en Python
Incluye: mayúsculas/minúsculas, strip, replace, split/join, búsqueda, conteo, comprobaciones, formateo e inversión.
"""

# 1️⃣ Convertir mayúsculas y minúsculas
texto = "Hola Mundo"
print("Original:", texto)
print("Upper:", texto.upper())
print("Lower:", texto.lower())
print("Capitalize:", texto.capitalize())
print("Title:", texto.title())
print("-" * 40)

# 2️⃣ Eliminar espacios
texto_espacios = "   Hola Mundo   "
print("Original con espacios:", repr(texto_espacios))
print("Strip:", repr(texto_espacios.strip()))
print("Lstrip:", repr(texto_espacios.lstrip()))
print("Rstrip:", repr(texto_espacios.rstrip()))
print("-" * 40)

# 3️⃣ Reemplazar partes de la cadena
texto = "hola mundo"
print("Replace 'hola'->'adiós':", texto.replace("hola", "adiós"))
print("-" * 40)

# 4️⃣ Dividir y unir cadenas
texto = "Hola mundo desde Python"
palabras = texto.split()  # divide por espacios
print("Split:", palabras)
csv = "1,2,3,4"
numeros = csv.split(",")
print("Split por ',':", numeros)
print("Join con '-':", "-".join(numeros))
print("-" * 40)

# 5️⃣ Buscar y contar
texto = "hola mundo hola"
print("Find 'mundo':", texto.find("mundo"))
print("Count 'hola':", texto.count("hola"))
print("-" * 40)

# 6️⃣ Comprobar contenido
print("'123'.isdigit():", "123".isdigit())
print("'abc'.isalpha():", "abc".isalpha())
print("'abc123'.isalnum():", "abc123".isalnum())
print("'   '.isspace():", "   ".isspace())
print("-" * 40)

# 7️⃣ Formatear cadenas
nombre = "Ana"
edad = 25
print("f-string:", f"{nombre} tiene {edad} años")
print("format:", "{} tiene {} años".format(nombre, edad))
print("%-format:", "%s tiene %d años" % (nombre, edad))
print("-" * 40)

# 8️⃣ Invertir una cadena
texto = "Python"
print("Cadena invertida:", texto[::-1])
print("-" * 40)

# 9️⃣ Estilo hacker (leet speak)
texto = "hola mundo"
texto_hacker = (texto.replace("a", "4").replace("A", "4")
                       .replace("e", "3").replace("E", "3")
                       .replace("i", "1").replace("I", "1")
                       .replace("o", "0").replace("O", "0"))
print("Estilo hacker:", texto_hacker)
print("-" * 40)

# 1️⃣0️⃣ Contar y eliminar espacios
cadena = "Esto es un ejemplo de cadena"
num_espacios = cadena.count(" ")
cadena_sin_espacios = cadena.replace(" ", "")
print("Texto original:", cadena)
print("Número de espacios eliminados:", num_espacios)
print("Texto sin espacios:", cadena_sin_espacios)
print("-" * 40)

# 1️⃣1️⃣ Invertir palabras de la cadena
cadena = "Hola mundo desde Python"
palabras = cadena.split()
palabras_invertidas = palabras[::-1]
cadena_invertida = " ".join(palabras_invertidas)
print("Cadena original:", cadena)
print("Cadena con palabras invertidas:", cadena_invertida)
