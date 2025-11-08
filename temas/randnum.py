import random

# ----------------------------------------
# 1️⃣ Número entero aleatorio
# ----------------------------------------
azar = random.randint(1, 10)
print("Número aleatorio entre 1 y 10:", azar)

# ----------------------------------------
# 2️⃣ Elegir un elemento aleatorio de una lista
# ----------------------------------------
lista = [1, 2, 3, 4, 5, 6]
print("Elemento aleatorio:", random.choice(lista))

# ----------------------------------------
# 3️⃣ Elegir varios elementos distintos
# ----------------------------------------
print("3 elementos distintos:", random.sample(lista, 3))

# ----------------------------------------
# 4️⃣ Desordenar la lista
# ----------------------------------------
print("Lista antes de shuffle:", lista)
random.shuffle(lista)
print("Lista después de shuffle:", lista)

# ----------------------------------------
# 5️⃣ Números decimales aleatorios
# ----------------------------------------
print("Número decimal aleatorio [0,1):", random.random())
print("Número decimal aleatorio entre 10 y 20:", random.uniform(10, 20))

# ----------------------------------------
# 6️⃣ Usar seed para reproducibilidad
# ----------------------------------------
random.seed(42)
print("Número con semilla 42:", random.randint(1, 100))
