# Django Rest Framework

## Instalacion

```bash
pip install Django
pip install djangorestframework
pip install python-dotenv
pip install psycopg2-binary
pip install -U drf-yasg

# Si aparece el error: ModuleNotFoundError: No module named 'pkg_resources'
# Ejecutar pip install --upgrade setuptools
```

## Configuración

```python
INSTALLED_APPS = [
    ...,
    'rest_framework',
    'drf_yasg',
    ...
]
```