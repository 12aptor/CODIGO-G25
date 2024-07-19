# Importamos la clase Flask desde el paquete flask
from flask import Flask, render_template, request, make_response

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
    # json = request.json
    json = request.get_json()

    # path
    path = request.path
    
    # method
    method = request.method

    return 'Iniciando sesión'

# Tambien podemos definir una ruta con un método específico @app.post()
@app.post('/sign-up')
def sign_up():
    return 'Registrando usuario', 201

# Renderizamos una plantilla HTML
@app.route('/home')
def home_page():
    products = ['Celular', 'Laptop', 'Smartwatch']
    return render_template('home.html', products=products)

@app.post('/product/create')
def create_product():
    image = request.files['image']
    print(image)

    # El request.form['key'] siempre devuelve un string
    name = request.form['name']
    print(name)
    price = request.form['price']
    print(type(price))
    return 'Creando producto'

@app.get('/secure')
def secure():
    # Recuperamos headers
    # headers = request.headers
    # jwt = headers['Authorization']

    # Recuperar cookies
    cookies = request.cookies.get('secure')
    print(cookies)
    return 'Página segura'

@app.get('/send-cookies')
def send_cookies():
    response = make_response({
        'message': 'Cookies enviadas'
    }, 200)
    response.set_cookie('secure', '123456')
    return response

@app.errorhandler(404)
def page_not_found(error):
    return 'Página no encontrada', 404

# Corremos la aplicación
if __name__ == '__main__':
    app.run(debug=True)