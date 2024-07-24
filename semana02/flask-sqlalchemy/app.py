from flask import Flask
from db import db
from sqlalchemy import Column, Integer, String

app = Flask(__name__)

# Configuracion de la base de datos
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://username:password@hostname/database_name'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:root@localhost:5432/flask-sqlalchemy'

# Inicializacion de la base de datos
db.init_app(app)


# Definicion de la clase Movies
class Movies(db.Model):
    __tablename__ = 'movies'

    id = Column(Integer, primary_key=True)
    title = Column(String(200))
    director = Column(String(200))
    year = Column(Integer)
    length_minutes = Column(Integer)


@app.route('/')
def index():
    # Creacion de la tabla
    db.create_all()
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True)