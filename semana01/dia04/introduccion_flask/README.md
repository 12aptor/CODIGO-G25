# Flask

## Crear un entorno virtual

```bash
python -m venv venv

source venv/Scripts/activate
```

## Instalar Flask

```bash
pip install Flask
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