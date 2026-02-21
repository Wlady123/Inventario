from producto import Producto

class Inventario:
    def __init__(self,archivo = "inventario.txt"):
        self.productos = []
        self.archivo = archivo
        self.cargar_desde_archivo()

    def agregar_producto(self, producto):
        for p in self.productos:
            if p.get_id() == producto.get_id():
                print ("Error: Ya existe un producto con ese ID")
                return
        self.productos.append(producto)
        print("Producto agregado correctamente")
        self.guardar_en_archivo()

    def eliminar_producto(self, id_producto):
        for p in self.productos:
            if p.get_id() == id_producto:
                self.productos.remove(p)
                print("Producto eliminado correctamente")
                self.guardar_en_archivo()
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
                self.guardar_en_archivo()
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

    # -------------------------
    # GUARDAR EN ARCHIVO
    # -------------------------

    def guardar_en_archivo(self):
        try:
            with open(self.archivo, "w") as f:
                for p in self.productos:
                    f.write(f"{p.get_id()},{p.get_nombre()},{p.get_cantidad()},{p.get_precio()}\n")
                    print("Inventario guardado en archivo.")
        except PermissionError:
            print("No tienes permisos para escribir el archivo.")


   # -------------------------
   # CARGAR DESDE ARCHIVO
   # -------------------------
    def cargar_desde_archivo(self):
            try:
                with open(self.archivo, "r") as f:
                    for linea in f:
                        id_,nombre,cantidad,precio = linea.strip().split(",")
                        producto = Producto(id_,nombre,int(cantidad),float(precio))
                        self.productos.append(producto)
                print("Inventario cargado desde archivo.")
            except FileNotFoundError:
                print("Archivo no encontrado. Se creara uno nuevo.")
                open(self.archivo, "w").close()




