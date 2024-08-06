from flask import Flask
from db import db
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from config import Config
from flask_cors import CORS

from routes.rol_router import rol_router
from routes.user_router import user_router
from routes.category_router import category_router
from routes.product_router import product_router
from routes.order_router import order_router


app = Flask(__name__)
cors = CORS(app)

app.config.from_object(Config)

db.init_app(app)
migrate = Migrate(app, db)
jwt = JWTManager(app)

app.register_blueprint(rol_router, url_prefix='/api/rol')
app.register_blueprint(user_router, url_prefix='/api/user')
app.register_blueprint(category_router, url_prefix='/api/category')
app.register_blueprint(product_router, url_prefix='/api/product')
app.register_blueprint(order_router, url_prefix='/api/order')

if __name__ == '__main__':
    app.run(debug=True)