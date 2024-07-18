# Entornos virtuales 😄

## ¿Qué es un entorno virtual?

Un entorno virtual es una herramienta que nos permite crear un entorno de desarrollo aislado del sistema principal. Esto nos permite instalar las dependencias necesarias para nuestro proyecto sin afectar a otros proyectos que tengamos en el mismo sistema.

## Crear un entorno virtual

```bash
python -m venv nombre_del_entorno
```

## Activar un entorno virtual

```bash
# Windows cmd
nombre_del_entorno\Scripts\activate

# Git Bash
source nombre_del_entorno/Scripts/activate

# MacOS o Linux
source nombre_del_entorno/bin/activate
```