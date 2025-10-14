profesorPrimero = {"Ana", "Juan Carlos", "Sancho", "Natalia"} #No admite duplicados
print(profesorPrimero)
profesorSegundo = set(["Agustin", "Ana", "Natalia", "Javier", "José María"])
print(profesorSegundo)

print(profesorPrimero | profesorSegundo)
print(profesorPrimero.union(profesorSegundo))
# Nos muestra los elementos de ambos conjuntos, pero los duplicados solo una vez.
# Es la unión de los dos conjuntos.
# Variante con método: hace exactamente lo mismo que el operador |.
# Variante con método:
#

print(profesorPrimero & profesorSegundo)
print(profesorPrimero.intersection(profesorSegundo))
# Nos muestra los elementos que hay en ambos conjuntos.
# Es la intersección de los conjuntos.
# Variante con método: hace exactamente lo mismo que el operador &.

print(profesorPrimero - profesorSegundo)
print(profesorPrimero.difference(profesorSegundo))
# Nos muestra los elementos que están en profesorPrimero pero no en profesorSegundo.
# Es la diferencia de conjuntos.
# Variante con método: hace exactamente lo mismo que el operador -.


print(profesorPrimero ^ profesorSegundo)
print(profesorPrimero.symmetric_difference(profesorSegundo))
# Nos muestra los elementos que están en uno u otro conjunto, pero no en ambos.
# Es la diferencia simétrica.
# Variante con método: hace exactamente lo mismo que el operador ^.



#if "Ana" in profesorPrimero:
#    print("Ana es profesora de primero")
#if "Sancho" not in profesorSegundo:
#    print("Sancho es no profesor de segundo")

#for elemento in profesorPrimero:
#    print(elemento)

#print(len(profesorPrimero))

#for i in range(len(profesorPrimero)):
#    print(1)

profesorPrimero.add("José María")
#print(profesorPrimero)
profesorPrimero.remove("José María") # .remove provoca excepcion si el elemento no existe . discard no
profesorPrimero.discard("José María")

profe = profesorPrimero.pop()
#print(profe)

profesorPrimero.clear() #borra el set completo
#print(profesorPrimero)

conjunto = set([1,2,3,3,4,5,6])
#print(conjunto)
conjunto2 = set("hola mundo cruel")
#print(conjunto2)

lista = list(profesorPrimero)

tupla = tuple(profesorSegundo)

texto = str(profesorSegundo)
#print(texto)






