# Flask

## Crear un entorno virtual

```bash
python -m venv venv

source venv/Scripts/activate
```

## Instalar Flask

```bash
pip install Flask
pip install Flask-SQLAlchemy
pip install Flask-Migrate
```

## Crear un archivo app.py

```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Bienvenido a mi primera app de Flask 😎'

if __name__ == '__main__':
    app.run(debug=True)
```

## Ejecutar la aplicación

```bash
python app.py
```

## Crear el documento db.py

```python
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
```

## Conección a una base de datos con Flask-SQLAlchemy

```python
from flask import Flask
from db import db

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

db.init_app(app)

class Movies(db.Model):
    __tablename__ = 'movies'

    id = Column(Integer, primary_key=True)
    title = Column(String(200))
    director = Column(String(200))
    year = Column(Integer)
    length_minutes = Column(Integer)

if __name__ == '__main__':
    app.run(debug=True)
```