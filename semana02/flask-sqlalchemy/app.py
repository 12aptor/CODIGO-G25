from flask import Flask, jsonify
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

    def __str__(self):
        return f'{self.title}'
    
    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'director': self.director,
            'year': self.year,
            'length_minutes': self.length_minutes
        }


@app.route('/movies')
def index():
    movies = Movies.query.all()
    
    response = []
    for movie in movies:
        response.append(movie.to_dict())

    return {
        'message': 'Movies found',
        'data': response
    }, 200

@app.route('/movies/<int:id>')
def movie_by_id(id):
    movie = Movies.query.get(id)

    if movie is None:
        return {
            'message': 'Movie not found'
        }, 404

    return {
        'message': 'Movie found',
        'data': movie.to_dict()
    }, 200

if __name__ == '__main__':
    app.run(debug=True)