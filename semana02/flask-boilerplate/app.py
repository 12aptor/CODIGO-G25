from flask import Flask
from routes.user_router import user_router

app = Flask(__name__)

app.register_blueprint(user_router, url_prefix='/api/user')

if __name__ == '__main__':
    app.run(debug=True)