class Producto:
    def __init__(self,id_producto,nombre, cantidad, precio):
        self._id = id_producto
        self._nombre = nombre
        self._cantidad = cantidad
        self._precio = precio

    def get_id(self):
        return self._id
    def get_nombre(self):
        return self._nombre
    def get_cantidad(self):
        return self._cantidad
    def get_precio(self):
        return self._precio
    def set_cantidad(self, cantidad):
        if cantidad >=0:
            self._cantidad = cantidad
        else:
            print("La cantidad no puede ser negativa")
    def set_precio(self, precio):
        if precio >=0:
            self._precio = precio
        else:
            print("El precio no puede ser negativo")
    def __str__(self):
        return f"ID: {self._id} | Nombre:{self._nombre} | Cantidad: {self._cantidad} | Precio: ${self._precio}"