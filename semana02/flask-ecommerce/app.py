from flask import Flask
from db import db
from flask_migrate import Migrate
from routes.rol_router import rol_router

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:root@localhost:5432/flask-ecommerce'

db.init_app(app)
migrate = Migrate(app, db)

app.register_blueprint(rol_router, url_prefix='/api/rol')

if __name__ == '__main__':
    app.run(debug=True)