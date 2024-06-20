from flask import Flask
from app.database import init_app
from app.views import *

app = Flask(__name__)

app.route('/', methods=['GET'])(index)

# Inicializar la base de datos con la aplicación Flask
init_app(app)

if __name__ == '__main__':
    app.run(debug=True)