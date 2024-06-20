from app.database import get_db

#Implementacion de la clase Producto
class Producto:
    def __init__(self, id_producto=None, nombre=None, descripcion=None, precio=None, cantidad=None):
        self.id_producto = id_producto
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
        self.cantidad = cantidad

    #Metodo para traer el listado de productos
    @staticmethod
    def get_all():
        db = get_db()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM productos")
        rows = cursor.fetchall()
        productos = [Producto(id_producto=row[0], nombre=row[1], descripcion=row[2], precio=row[3], cantidad=row[4])
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
            return Producto(id_producto=row[0], nombre=row[1], descripcion=row[2], precio=row[3], cantidad=row[4])
        return None
    
    #Método para guardar/actualizar un producto
    def save(self):
        db = get_db()
        cursor = db.cursor()
        if self.id_producto:
            cursor.execute("""
            UPDATE productos SET nombre = %s, descripcion = %s, precio = %s, cantidad = %s
            WHERE id_producto = %s
            """, (self.nombre, self.descripcion, self.precio, self.cantidad, self.id_producto))
        else:
            cursor.execute("""
            INSERT INTO productos (nombre, descripcion, precio, cantidad) VALUES (%s, %s, %s, %s)
            """, (self.nombre, self.descripcion, self.precio, self.cantidad))
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
        'descripcion': self.descripcion,
        'precio': self.precio,
        'cantidad': self.cantidad
        }