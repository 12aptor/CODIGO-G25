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

# adivinanza()


"""Crear un generador de contraseñas seguras. El programa debe pedir al usuario la longitud de la contraseña"""

import string

def generar_password():
    longitud = int(input("Número de caracteres de la contraseña: "))
    # caracteres = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()'
    caracteres = string.ascii_letters + string.digits + string.punctuation
    password = ''
    for i in range(longitud):
        password += random.choice(caracteres)
    
    print(f"Tu contraseña segura es: {password}")


# generar_password()


"""Crear un programa que me muestre posts (CONSUMIENDO UNA API)"""

import requests

def mostrar_posts():
    API_URL = 'https://jsonplaceholder.typicode.com/posts/1'
    respuesta = requests.get(API_URL)
    datos = respuesta.json()
    estado = respuesta.status_code
    if estado == 200:
        print(f"Título: {datos['title']}")
        print(f"Contenido: {datos['body']}")
    else:
        print("No se pudo obtener la información")

mostrar_posts()