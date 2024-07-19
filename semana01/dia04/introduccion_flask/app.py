# Importamos la clase Flask desde el paquete flask
from flask import Flask

# Instanciamos la clase Flask
app = Flask(__name__)

# Definimos la ruta de la aplicación
@app.route('/')
def home():
    return 'Bienvenido a mi primera app de Flask 😎'

@app.route('/about')
def about():
    return 'Acerca de mi'

# Corremos la aplicación
if __name__ == '__main__':
    app.run(debug=True)