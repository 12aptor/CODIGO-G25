"""Manejo de excepciones"""

# division = 10 / 0

# En el código anterior, se produce un error de división por cero.
# Este error rompe la ejecución del programa.

def main():
    # La finalidad de las excepciones es manejar los errores de forma controlada.
    try:
        # Todo lo que esté dentro de este bloque de código será ejecutado
        # y si se produce un error, se manejará de forma controlada.
        division = 10 / 0
        print("La división se realizó correctamente")

    # En caso de que se produzca un error, se ejecutará el bloque except.
    except:
        print("Se ha producido un error en la división")

    # El bloque finally se ejecutará siempre, independientemente de si se produce un error o no.
    finally:
        print("Este bloque de código se ejecutará siempre")

# main()


def evaluar_edad(edad):
    try:
        if edad < 18:
            raise Exception("El usuario es menor de edad")
        
        print("Usuario autorizado")
    except Exception as error:
        print(error)

evaluar_edad(16)