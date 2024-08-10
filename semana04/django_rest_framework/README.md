# Django Rest Framework

## Instalacion

```bash
pip install Django
pip install djangorestframework
pip install python-dotenv
pip install psycopg2-binary
pip install -U drf-yasg
pip install django-cors-headers

# Si aparece el error: ModuleNotFoundError: No module named 'pkg_resources'
# Ejecutar pip install --upgrade setuptools
```

## Configuración

```python
INSTALLED_APPS = [
    ...,
    'rest_framework',
    'drf_yasg',
    "corsheaders",
    ...
]

MIDDLEWARE = [
    ...,
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    ...,
]
```

## Info

Ignorar el documento `testCorsHtml.html` Solo se usó para probar los cors de la API