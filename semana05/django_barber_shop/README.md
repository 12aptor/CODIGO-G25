# Testing con Pytest

## Instalar dependencias

```bash
pip install pytest pytest-django pytest-cov
```

## Ejecutar tests

```bash
pytest
```

# Despliegue en Render

## Ficheros necesarios
- .gitignore
- .env
- requirements.txt

## Instalar Whitenoise

```bash
pip install 'whitenoise[brotli]'
pip freeze > requirements.txt
```

```python
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    ...
]
```

## Configurar staticfiles

```python
STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
```

## Instalar uvicorn y gunicorn

```bash
pip install uvicorn gunicorn
pip freeze > requirements.txt
```

