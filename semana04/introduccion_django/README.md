# Django

## Introducción

Django es un framework de aplicaciones web que permite crear aplicaciones web rápidamente.

## Crear un entorno virtual

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Git Bash
source venv/Scripts/activate

# Linux / MacOS
source venv/bin/activate
```

## Instalar Django

```bash
pip install Django
```

## Crear el proyecto

```bash
django-admin startproject nombre-del-proyecto
# django-admin startproject introduccion_django .
```

## Iniciar el servidor

```bash
python manage.py runserver
```

## Ejecutas las migraciones

```bash
python manage.py migrate
```

## Crear un super usuario

```bash
python manage.py createsuperuser
```

## Crear una aplicación
```bash
python manage.py startapp almacen
```

## Migraciones

```bash
python manage.py makemigrations # Para crear las migraciones
# python manage.py makemigrations nombre-de-la-aplicacion
python manage.py migrate # Para ejecutar las migraciones
python manage.py showmigrations # Para ver las migraciones
```