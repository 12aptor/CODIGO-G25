mascotas = ["Firulais", "Jack", "Luna", "Rocco"]

"""Buscar por la posición"""
index = 0
for mascota in mascotas:
    if index == 2:
        print(f"Mi mascota favorita es: {mascota}")

    index += 1

"""Buscar por el valor"""
for mascota in mascotas:
    if mascota == "Rocco":
        print(f"Mi mascota favorita es: {mascota}")


"""While"""

contador = 1
while contador < 6:
    print(contador)
    contador += 1