from flask import Flask
from flask_cors import CORS
from app.database import init_app
from app.views import *

app = Flask(__name__)

app.route('/', methods=['GET'])(index)

app.route('/api/productos/', methods=['GET'])(get_all_productos)

app.route('/api/productos/<int:producto_id>', methods=['GET'])(get_producto)

app.route('/api/productos/', methods=['POST'])(create_producto)

app.route('/api/productos/<int:producto_id>', methods=['PUT'])(update_producto)

app.route('/api/productos/<int:producto_id>', methods=['DELETE'])(delete_producto)

app.route('/api/productos/<nombre>', methods=['GET'])(filtrar_nombre)

app.route('/api/marcas/<marca>', methods=['GET'])(filtrar_marca)

app.route('/api/precio/<int:precio>', methods=['GET'])(filtrar_precio)

app.route('/api/cantidad/<int:cantidad>', methods=['GET'])(filtrar_cantidad)

# Inicializar la base de datos con la aplicación Flask
init_app(app)

#permitir solicitudes desde cualquier origen
CORS(app)

if __name__ == '__main__':
    app.run(debug=True)
