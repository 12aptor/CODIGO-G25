# Importamos la clase Flask desde el paquete flask
from flask import Flask, render_template

# Instanciamos la clase Flask
app = Flask(__name__)

# Definimos la ruta de la aplicación
@app.route('/')
def home():
    return 'Bienvenido a mi primera app de Flask 😎'

@app.route('/usuario/<username>')
# @app.route('/usuario/<string:username>')
# @app.route('/usuario/<int:id>')
# @app.route('/usuario/<float:price>')
# @app.route('/usuario/<path:subpath>') # /usuario/este/es/un/ejemplo
# @app.route('/usuario/<uuid:uuid>') # /usuario/123e4567-e89b-12d3-a456-426614174000
def about(username):
    return f'Hola {username}'

@app.route('/sign-in', methods=['POST'])
# @app.route('/sign-in', methods=['GET', 'POST', 'PUT', 'DELETE', 'PATCH', 'OPTIONS'])
def sign_in():
    return 'Iniciando sesión'

# Tambien podemos definir una ruta con un método específico @app.post()
@app.post('/sign-up')
def sign_up():
    return 'Registrando usuario'

# Renderizamos una plantilla HTML
@app.route('/home')
def home_page():
    products = ['Celular', 'Laptop', 'Smartwatch']
    return render_template('home.html', products=products)

# Corremos la aplicación
if __name__ == '__main__':
    app.run(debug=True)