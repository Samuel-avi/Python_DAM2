lista = []
lista2 = list()
lista3 = [2,4,5,6,7,12, 6, 6]
lista4 = [23, "hola", False, lista3, [1,2,3]]
#print(lista4)

#for elemento in lista:
#    print(elemento)

#for posicion in range(0,len(lista4)):
#    print(posicion, "-", lista4[posicion])

lista.append("Nuevo elemento")
print(lista)
lista5 = lista + [23,6]
print(lista5)

print(lista3)
print(lista3.pop(3)) # No elimina el elemento, lo extae
print(lista3)

lista3.remove(5) # Elimina el primer valor "5" que encuentra

lista3.sort() #Modifica la lista original, .sort(reverse=True)

# lista3 = lista3 + lista4 >> concatena listas
# lista3.extend(lista4) >> concatena el valor de extend (puede ser otra lista)

lista3.insert(2,10) # iserta el segundo numero en la posicion del primer numero, si el primer número es negativo empieza desde el final

print(lista3.count(6)) # cuantas veces se repite un elemento en una lista

print(lista3.index(6)) # devuelve la posicion del elemento

texto = str(lista3)

texto2 = "hola mundo"

listatexto = list(texto2)

print(listatexto)

matriz = [1, 2, 3], [4, 5, 6], [7, 8, 9]
print(matriz[1][2])

print(lista3[4:5]) #misma sintaxis que x:x ::1 da vuelta la cadena

if 4 in lista3: # no in
    print("esta")











