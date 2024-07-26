# Ecommerce-API

## Dependencias

```bash
pip install Flask
pip install Flask-SQLAlchemy
pip install Flask-Migrate
pip install Flask-Cors
pip install psycopg2-binary
pip install pydantic
pip install bcrypt
pip install bcrypt[email]
```

## Convertir json a objeto

```python
# json = {
    # name: 'Admin',
    # status: true,
    # created_at: '2021-09-01 00:00:00',
# }
# ** Convert json to object
# validated_rol = RolSchema(name='Admin', status=True, created_at='2021-09-01 00:00:00')
```