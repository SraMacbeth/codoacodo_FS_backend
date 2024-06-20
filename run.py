from flask import Flask
from app.database import init_app
from app.views import *

app = Flask(__name__)

app.route('/', methods=['GET'])(index)

app.route('/api/productos/', methods=['GET'])(get_all_productos)

app.route('/api/productos/<int:producto_id>', methods=['GET'])(get_producto)

app.route('/api/productos/', methods=['POST'])(create_producto)

app.route('/api/productos/<int:producto_id>', methods=['PUT'])(update_producto)

app.route('/api/productos/<int:producto_id>', methods=['DELETE'])(update_producto)

# Inicializar la base de datos con la aplicación Flask
init_app(app)

if __name__ == '__main__':
    app.run(debug=True)