from app.database import get_db

#Implementacion de la clase Producto
class Producto:
    def __init__(self, id_producto=None, nombre=None, marca=None, precio=None, cantidad=None):
        self.id_producto = id_producto
        self.nombre = nombre
        self.marca = marca
        self.precio = precio
        self.cantidad = cantidad

    #Metodo para traer el listado de productos
    @staticmethod
    def get_all():
        db = get_db()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM productos")
        rows = cursor.fetchall()
        productos = [Producto(id_producto=row[0], nombre=row[1], marca=row[2], precio=row[3], cantidad=row[4])
        for row in rows]
        cursor.close()
        return productos

    #Metodo para traer un producto
    @staticmethod
    def get_by_id(producto_id):
        db = get_db()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM productos WHERE id_producto = %s", (producto_id,))
        row = cursor.fetchone()
        cursor.close()
        if row:
            return Producto(id_producto=row[0], nombre=row[1], marca=row[2], precio=row[3], cantidad=row[4])
        return None
    
    #Método para guardar/actualizar un producto
    def save(self):
        db = get_db()
        cursor = db.cursor()
        if self.id_producto:
            cursor.execute("""
            UPDATE productos SET nombre = %s, marca = %s, precio = %s, cantidad = %s
            WHERE id_producto = %s
            """, (self.nombre, self.marca, self.precio, self.cantidad, self.id_producto))
        else:
            cursor.execute("""
            INSERT INTO productos (nombre, marca, precio, cantidad) VALUES (%s, %s, %s, %s)
            """, (self.nombre, self.marca, self.precio, self.cantidad))
            self.id_producto = cursor.lastrowid
        db.commit()
        cursor.close()

    #Método para eliminar un producto
    def delete(self):
        db = get_db()
        cursor = db.cursor()
        cursor.execute("DELETE FROM productos WHERE id_producto = %s", (self.id_producto,))
        db.commit()
        cursor.close()

    #Método serializador de un producto
    def serialize(self):
        return {
        'id_producto': self.id_producto,
        'nombre': self.nombre,
        'marca': self.marca,
        'precio': self.precio,
        'cantidad': self.cantidad
        }
    
    #Método para filtrar los productos por nombre
    def get_by_nombre(nombre):
        db = get_db()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM productos WHERE nombre = %s", (nombre,))
        rows = cursor.fetchall()
        productos = [Producto(id_producto=row[0], nombre=row[1], marca=row[2], precio=row[3], cantidad=row[4])
        for row in rows]
        cursor.close()
        return productos
    
    #Método para filtrar los productos por marca
    def get_by_marca(marca):
        db = get_db()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM productos WHERE marca = %s", (marca,))
        rows = cursor.fetchall()
        productos = [Producto(id_producto=row[0], nombre=row[1], marca=row[2], precio=row[3], cantidad=row[4])
        for row in rows]
        cursor.close()
        return productos

    #Método para filtrar los productos por precio
    def get_by_precio(precio):
        db = get_db()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM productos WHERE precio < %s", (precio,))
        rows = cursor.fetchall()
        productos = [Producto(id_producto=row[0], nombre=row[1], marca=row[2], precio=row[3], cantidad=row[4])
        for row in rows]
        cursor.close()
        return productos
    
        #Método para filtrar los productos por cantidad
    def get_by_cantidad(cantidad):
        db = get_db()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM productos WHERE cantidad < %s", (cantidad,))
        rows = cursor.fetchall()
        productos = [Producto(id_producto=row[0], nombre=row[1], marca=row[2], precio=row[3], cantidad=row[4])
        for row in rows]
        cursor.close()
        return productos