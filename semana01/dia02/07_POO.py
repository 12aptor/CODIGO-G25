"""Programación Orientada a Objetos"""

# Clases

class Persona:
    # Constructor
    def __init__(self, nombre: str, edad: int, casado: bool) -> None:
        self.nombre = nombre
        self.edad = edad
        self.casado = casado
        self.__atributo_privado = "Soy un atributo privado"

    # Métodos
    def saludar(self) -> None:
        self.__metodo_privado()
        print(f"Hola, soy {self.nombre}")

    # Métodos privados (no se pueden acceder desde fuera de la clase)
    def __metodo_privado(self) -> None:
        print("Soy un método privado")


# Instanciar la clase
persona = Persona("Pedro", 30, False)

# Acceder a los atributos
print(persona.nombre)
# print(persona.__atributo_privado)  # Error

# Acceder a los métodos
persona.saludar()
# persona.__metodo_privado()  # Error