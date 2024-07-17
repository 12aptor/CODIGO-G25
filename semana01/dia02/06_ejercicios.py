"""Crear un juego de adivinanza de números. El programa debe generar un número aleatorio entre 1 y 10
y el programa debe ayudarte con ES MENOR y ES MAYOR"""

import random

def adivinanza():
    numeroAleatorio = random.randint(1, 10)
    numeroIntentos = 0
    print("¡Bienvenido a la adivinanza de números!")
    print("Estoy pensando en un numero entre 1 y 10")

    while True:
        intento = int(input("Adivina el número: "))
        numeroIntentos += 1

        if intento == numeroAleatorio:
            print(f"¡Felicidades! Adivinaste el número en el intento {numeroIntentos}")
            break
        elif intento < numeroAleatorio:
            print("El número es mayor")
        else:
            print("El número es menor")

adivinanza()