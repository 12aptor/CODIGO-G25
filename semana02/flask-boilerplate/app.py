from flask import Flask
from flask_cors import CORS
from routes.user_router import user_router

app = Flask(__name__)
cors = CORS(app)

app.register_blueprint(user_router, url_prefix='/api/user')

if __name__ == '__main__':
    app.run(debug=True)