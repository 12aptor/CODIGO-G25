usuarios = ['admin', 'pepe', 'juan']

def mostrar_usuarios():
    for usuario in usuarios:
        print(usuario)

class Mascota:
    def __init__(self) -> None:
        self.nombre = 'Firulais'

    def mostrar_nombre(self):
        print(f" El nombre de la mascota es: {self.nombre}")