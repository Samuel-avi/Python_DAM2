p1 = input("Escribe la primera palabra: ")
p2 = input("Escribe la segunda palabra: ")
p3 = input("Escribe la tercera palabra: ")

lista = [p1,p2,p3]
lista.sort(key = str.lower) # type: ignore

print("Palabras ordenadas = ", ", ".join(lista.__reversed__()))