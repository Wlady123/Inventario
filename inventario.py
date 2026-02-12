from producto import Producto

class Inventario:
    def __init__(self):
        self.productos = []
    def agregar_producto(self, producto):
        for p in self.productos:
            if p.get_id() == producto.get_id():
                print ("Error: Ya existe un producto con ese ID")
                return
        self.productos.append(producto)
        print("Producto agregado correctamente")

    def eliminar_producto(self, id_producto):
        for p in self.productos:
            if p.get_id() == id_producto:
                self.productos.remove(p)
                print("Producto eliminado correctamente")
                return
        print("Producto no encontrado")

    def actualizar_producto(self, id_producto, nueva_cantidad=None, nuevo_precio=None):
        for p in self.productos:
            if p.get_id() == id_producto:

                if nueva_cantidad is not None:
                    p.set_cantidad(nueva_cantidad)

                if nuevo_precio is not None:
                    p.set_precio(nuevo_precio)

                print ("Producto actualizado correctamente")
                return
        print ("Producto no encontrado")

    def buscar_por_nombre(self, nombre):
        resultados = []

        for p in self.productos:
            if nombre.lower() in p.get_nombre().lower():
                resultados.append(p)

            if resultados:
                print ("Productos encontrados:")
                for producto in resultados:
                    print (producto)
            else:
                print("No se encontraron productos con ese nombre")


    def mostrar_productos(self):
        if not self.productos:
            print("El inventario esta vacio")
        else:
            for producto in self.productos:
                print(producto)


