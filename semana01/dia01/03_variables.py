"""Ejemplos"""
numero = 10
texto = "Hola Mundo"

"""Cambiar el valor de una variable"""
nombreUsuario = "Juan"
nombreUsuario = 10

"""Obtener el tipo de una variable"""
print(type(nombreUsuario))

"""Casting"""
nuevoNumero = str(numero) # Convertir a string => "10"
entero = int(nuevoNumero) # Convertir a entero => 10
flotante = float(entero) # Convertir a flotante => 10.0

"""Nombre de las variables"""
nombreUsuario = "Juan"
nombre_usuario = "Pedro"
_nombreUsuario = "Maria"
NOMBREUSUARIO = "Luis"
nombreUsuario2 = "Carlos"

"""Asignar multiples valores"""
a, b, c = 1, 2, 3
a = b = c = 1
letras = ["a", "b", "c"]
d, e, f = letras
print(d, e, f)
