from flask import Flask, request, jsonify
from app.models import Producto

app = Flask(__name__)

#index
def index():
    return jsonify({'message': 'Hello World API Productos'})

#traer todos los productos
def get_all_productos():
    productos = Producto.get_all()
    return jsonify([producto.serialize() for producto in productos])

#traer un producto
def get_producto(producto_id):
    producto = Producto.get_by_id(producto_id)
    if not producto:
        return jsonify({'message': 'Product not found'}), 404
    return jsonify(producto.serialize())

#crear un producto
def create_producto():
    data = request.json
    new_producto = Producto(nombre=data['nombre'], marca=data['marca'], precio=data['precio'], cantidad=data['cantidad'])
    new_producto.save()
    return jsonify({'message': 'Product created successfully'}), 201

#actualizar un producto
def update_producto(producto_id):
    producto = Producto.get_by_id(producto_id)
    if not producto:
        return jsonify({'message': 'Product not found'}), 404
    data = request.json
    producto.nombre = data['nombre']
    producto.marca = data['marca']
    producto.precio = data['precio']
    producto.cantidad = data['cantidad']
    producto.save()
    return jsonify({'message': 'Product updated successfully'})

#eliminar un producto
def delete_producto(producto_id):
    producto = Producto.get_by_id(producto_id)
    if not producto:
        return jsonify({'message': 'Product not found'}), 404
    producto.delete()
    return jsonify({'message': 'Product deleted successfully'})

#filtrar productos por nombre
def filtrar_nombre(nombre):
    productos = Producto.get_by_nombre(nombre)
    if not productos:
        return jsonify([]), 200
    return jsonify([producto.serialize() for producto in productos]), 200

#filtrar productos por marca
def filtrar_marca(marca):
    productos = Producto.get_by_marca(marca)
    if not productos:
        return jsonify([]), 200
    return jsonify([producto.serialize() for producto in productos]), 200

#filtrar productos por precio
def filtrar_precio(precio):
    productos = Producto.get_by_precio(precio)
    if not productos:return jsonify([]), 200
    return jsonify([producto.serialize() for producto in productos]), 200

#filtrar productos por cantidad
def filtrar_cantidad(cantidad):
    productos = Producto.get_by_cantidad(cantidad)
    if not productos:
        return jsonify([]), 200
    return jsonify([producto.serialize() for producto in productos]), 200   