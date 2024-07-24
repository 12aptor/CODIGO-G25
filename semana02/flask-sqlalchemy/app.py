from flask import Flask
from db import db
from sqlalchemy import Column, Integer, String
from flask_migrate import Migrate

app = Flask(__name__)

# Configuracion de la base de datos
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://username:password@hostname/database_name'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:root@localhost:5432/flask-sqlalchemy'

# Inicializacion de la base de datos
db.init_app(app)
migrate = Migrate(app, db)

# Definicion de la clase Movies
class Movies(db.Model):
    __tablename__ = 'movies'

    id = Column(Integer, primary_key=True)
    title = Column(String(200))
    director = Column(String(200))
    year = Column(Integer)
    length_minutes = Column(Integer)


@app.route('/movies')
def index():
    movies = Movies.query.all()
    print(movies)
    return 'Hello World!'

if __name__ == '__main__':
    app.run(debug=True)