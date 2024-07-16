"""Strings"""
texto = "Hola Mundo"
otroTexto = """Hola amiguitos
de la escuela
de la vida. Saludos!"""

"""Manipular strings"""
# Iterar sobre un string
for letra in texto:
    print(letra)

# Concatenar strings
texto += "!"
# print(texto)

# Multiplicar strings
texto *= 3

# Formatear strings
nombre = "Juan"
edad = 25
saludo = "Hola, soy {} y tengo {} años".format(nombre, edad)
segundoSaludo = f"Hola, soy {nombre} y tengo {edad} años"

"""Buscar en strings"""
print("Mundo" in texto)
if "Mundo" in texto:
    print("Mundo encontrado")

if "Mundo" not in texto:
    print("Mundo no encontrado")

"""Métodos de strings"""
# Mayúsculas y minúsculas
print(texto.upper())

# Minúsculas (lower)
print(texto.lower())

# Capitalizar (primera letra en mayúscula)
print(texto.capitalize())

# Contar ocurrencias
print(texto.count("o"))

# Encontrar posición
print(texto.find("o"))

# Reemplazar
print(texto.replace("o", "0"))

# Separar "Hola mundo".split(" ") -> ["Hola", "mundo"]
print(texto.split(" "))

# Eliminar espacios
print("  Hola mundo  ".strip())

# Comprobar si es un número
print("123".isdigit())

# Comprobar si es alfabético
print("Hola".isalpha())
