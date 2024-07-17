usuario = {
    "nombre": "Juan",
    "edad": 25,
    "casado": False,
    "mascotas": [{"nombre": "Rocco"}],
}

"""Constructor"""
otroDiccionario = dict(marca='Toyota', modelo='Corolla')
print(otroDiccionario)

"""Iterar un diccionario"""
for clave in usuario:
    print(clave, usuario[clave])

for clave, valor in usuario.items():
    print(clave, valor)

"""Actualizar un diccionario"""
usuario["nombre"] = "Pepito"

"""Agregar un elemento"""
usuario["email"] = "pepito@gmail.com"

"""Eliminar un elemento"""
del usuario["edad"]
usuario.pop("casado")

"""Métodos"""
# Obtener las claves
print(usuario.keys())

# Obtener los valores
print(usuario.values())

# Obtener los items
print(usuario.items())

# Copiar un diccionario
usuario2 = usuario.copy()

# Limpiar un diccionario
usuario.clear()

# Obtener un valor por clave
print(usuario2.get("nombre"))

# Actualizar un diccionario con otro
print(usuario2.update(otroDiccionario))
