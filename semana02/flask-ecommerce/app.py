from flask import Flask
from db import db
from flask_migrate import Migrate
from routes.rol_router import rol_router
from routes.user_router import user_router

from models import (
    category_model,
    order_detail_model,
    order_model,
    product_model,
    rol_model,
    update_product_log_model,
    user_model
)

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:root@localhost:5432/flask-ecommerce'

db.init_app(app)
migrate = Migrate(app, db)

app.register_blueprint(rol_router, url_prefix='/api/rol')
app.register_blueprint(user_router, url_prefix='/api/user')

if __name__ == '__main__':
    app.run(debug=True)