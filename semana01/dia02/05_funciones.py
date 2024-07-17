def suma(a: int, b: int) -> int:
    return a + b

"""Uso de la función suma"""
resultado = suma(2, 5)
# print(resultado)

"""Función con argumentos arbitrarios"""
def mi_funcion(*args: str) -> None:
    print(args)
    print(args[0])

mi_funcion("Pepito", "Pablito", "Fulanito")


"""Función con argumentos con clave"""
def mi_funcion2(nombre: str, apellido: str) -> None:
    print(nombre, apellido)

mi_funcion2(nombre="Pepito", apellido="Perez")


"""Función con argumentos con clave arbitrarios"""
def mi_funcion3(**kwargs) -> None:
    print(kwargs["edad"])

mi_funcion3(nombre="Pepito", apellido="Perez", edad=25)