lista = ["Hola", "Mundo", "Python", "2021"]

# lista = ["Hola", 2, False, 3.14, [1, 2, 3]]

"""Acceso a elementos"""

# Acceso a un elemento
print(lista[0])

# Acceso a un rango de elementos
print(lista[0:2])

# Acceso a un rango de elementos con saltos
print(lista[0:4:2])

# Acceso a un elemento desde el final
print(lista[-1])

# Acceso a un rango de elementos desde el final
print(lista[-3:-1])

"""Metodos de las listas"""
# Agregar un elemento al final de la lista
lista.append("Nuevo elemento")

# Agregar un elemento en una posicion especifica
lista.insert(2, "Nuevo elemento")

# Eliminar un elemento de la lista
lista.remove("Nuevo elemento")

# Eliminar un elemento de la lista por su indice
lista.pop(2)

# Eliminar un rango de elementos
del lista[0:2]

# Eliminar todos los elementos de la lista
lista.clear()

# Copiar una lista
lista2 = lista.copy()

# Contar cuantas veces se repite un elemento
print(lista2.count("Hola"))

# Obtener el indice de un elemento
print(lista2.index("Hola"))

# Invertir la lista
lista2.reverse()

# Ordenar la lista
lista2.sort()
