miTupla = ("Manzana", "Pera", "Melocotón")


"""Iterar una tupla"""
for fruta in miTupla:
    print(fruta)

"""Métodos de las tuplas"""
# count() - Devuelve el número de veces que aparece un valor específico en la tupla
print(miTupla.count("Manzana"))

# index() - Busca en la tupla un valor específico y devuelve la posición en la que se encuentra
print(miTupla.index("Pera"))