# Django Rest Framework

## Instalacion

```bash
pip install Django
pip install djangorestframework
pip install python-dotenv
pip install psycopg2-binary
pip install -U drf-yasg
pip install django-cors-headers
pip install djangorestframework-simplejwt

# Si aparece el error: ModuleNotFoundError: No module named 'pkg_resources'
# Ejecutar pip install --upgrade setuptools
```

## Configuración

```python
INSTALLED_APPS = [
    ...,
    'rest_framework',
    'drf_yasg',
    'corsheaders',
    'rest_framework_simplejwt',
    ...
]

MIDDLEWARE = [
    ...,
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    ...,
]

REST_FRAMEWORK = {
    # Define los formatos de respuesta
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
    ),
    # Para que mi aplicacion pueda hacer uso de JWT
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    )
}
```

## Info

Ignorar el documento `testCorsHtml.html` Solo se usó para probar los cors de la API
