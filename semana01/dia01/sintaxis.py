"""
Comentarios en python
de varias líneas
"""

# Comentario en una sola línea

"""Imprimir en pantalla"""
print("Hola Mundo")

"""Variables"""
numero = 10

"""Identación"""
def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

"""Condicionales"""
if numero > 10:
    print("Mayor a 10")
elif numero == 10:
    print("Igual a 10")
else:
    print("Menor a 10")

"""Condicionales con operadores lógicos"""
if numero > 10 and numero < 20:
    print("Mayor a 10 y menor a 20")

if numero > 10 or numero < 20:
    print("Mayor a 10 o menor a 20")
