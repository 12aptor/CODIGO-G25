from flask import Flask, request
from db import db
from sqlalchemy import Column, Integer, String
from flask_migrate import Migrate
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app)

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


@app.get('/movies')
def all_movies():
    movies = Movies.query.all()
    
    response = []
    for movie in movies:
        response.append(movie.to_dict())

    return {
        'message': 'Movies found',
        'data': response
    }, 200

@app.get('/movies/<int:id>')
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

@app.post('/movies/create')
def create_movie():
    json = request.json

    movie = Movies(
        title = json['title'],
        director = json['director'],
        year = json['year'],
        length_minutes = json['length_minutes']
    )

    db.session.add(movie)
    db.session.commit()

    return {
        'message': 'Movie created',
        'data': movie.to_dict()
    }, 201

@app.put('/movies/update/<int:id>')
def update_movie(id):
    movie = Movies.query.get(id)

    if movie is None:
        return {
            'message': 'Movie not found'
        }, 404
    
    json = request.json

    movie.title = json['title']
    movie.director = json['director']
    movie.year = json['year']
    movie.length_minutes = json['length_minutes']

    db.session.commit()

    return {
        'message': 'Movie updated',
        'data': movie.to_dict()
    }, 200

@app.delete('/movies/delete/<int:id>')
def delete_movie(id):
    movie = Movies.query.get(id)

    if movie is None:
        return {
            'message': 'Movie not found'
        }, 404
    
    db.session.delete(movie)
    db.session.commit()

    return {
        'message': 'Movie deleted'
    }, 200

if __name__ == '__main__':
    app.run(debug=True)