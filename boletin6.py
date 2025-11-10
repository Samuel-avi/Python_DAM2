import re

# 1️⃣ Código postal de Madrid (28XXX)
def validar_cp_madrid(cadena):
    return bool(re.fullmatch(r"28\d{3}", cadena))

# 2️⃣ Número de teléfono (8 dígitos)
def validar_telefono(cadena):
    return bool(re.fullmatch(r"\d{8}", cadena))

# 3️⃣ Teléfono móvil (empieza por 6, 7 u 8 y 9 dígitos)
def validar_movil(cadena):
    return bool(re.fullmatch(r"[678]\d{8}", cadena))

# 4️⃣ Teléfono con prefijo internacional (+NN <espacio> número)
def validar_tel_internacional(cadena):
    return bool(re.fullmatch(r"\+\d{2}\s\d{8,12}", cadena))

# 5️⃣ Dos palabras con mayúscula inicial separadas por espacio
def validar_dos_palabras(cadena):
    return bool(re.fullmatch(r"[A-Z][a-zA-Z]*\s[A-Z][a-zA-Z]*", cadena))

# 6️⃣ Clave formato XX00-xxX-00
def validar_clave(cadena):
    return bool(re.fullmatch(r"[A-Z]{2}\d{2}-[a-z]{2}[A-Z]-\d{2}", cadena))

# 7️⃣ Tarjeta de crédito con fecha (MM/YY)
def validar_tarjeta_credito(cadena):
    return bool(re.fullmatch(r"(\d{4}\s){3}\d{4}\s(0[1-9]|1[0-2])/\d{2}", cadena))

# 8️⃣ IBAN español (ES + dígitos con espacios)
def validar_iban_es(cadena):
    return bool(re.fullmatch(r"ES\d{2}(?:\s?\d{4}){4,5}", cadena))

# 9️⃣ Número de 4 a 8 cifras
def validar_numero_4a8(cadena):
    return bool(re.fullmatch(r"\d{4,8}", cadena))

# 🔟 IP clase C pública (192.168.X.X)
def validar_ip_clase_c(cadena):
    return bool(re.fullmatch(r"192\.168\.(?:[0-9]{1,3})\.(?:[0-9]{1,3})", cadena))


# --- Ejemplos de prueba ---
pruebas = {
    "CP Madrid": "28032",
    "Teléfono": "91345566",
    "Móvil": "655776655",
    "Tel. Internacional": "+34 912233444",
    "Dos palabras": "Hola Mundo",
    "Clave": "AB12-xyZ-75",
    "Tarjeta crédito": "1234 5678 9012 3456 03/25",
    "IBAN": "ES61 1234 3456 42 0456323532",
    "Número 4-8 cifras": "12345",
    "IP clase C": "192.168.30.30"
}

funciones = [
    validar_cp_madrid,
    validar_telefono,
    validar_movil,
    validar_tel_internacional,
    validar_dos_palabras,
    validar_clave,
    validar_tarjeta_credito,
    validar_iban_es,
    validar_numero_4a8,
    validar_ip_clase_c
]

print("Resultados de validación:")
for (nombre, valor), f in zip(pruebas.items(), funciones):
    print(f"{nombre:20}: {valor:25} → {f(valor)}")
