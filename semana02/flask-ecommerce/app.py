from flask import Flask
from db import db
from flask_migrate import Migrate
from routes.rol_router import rol_router
from routes.user_router import user_router
from routes.category_router import category_router
from flask_jwt_extended import JWTManager
from config import Config

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

app.config.from_object(Config)

db.init_app(app)
migrate = Migrate(app, db)
jwt = JWTManager(app)

app.register_blueprint(rol_router, url_prefix='/api/rol')
app.register_blueprint(user_router, url_prefix='/api/user')
app.register_blueprint(category_router, url_prefix='/api/category')

if __name__ == '__main__':
    app.run(debug=True)