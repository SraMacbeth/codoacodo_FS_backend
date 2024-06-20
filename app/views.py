from flask import Flask, jsonify

app = Flask(__name__)

def index():
    return jsonify({'message': 'Hello World API Productos'})