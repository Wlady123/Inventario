from inventario import Inventario
from producto import Producto

inventario = Inventario()

while True:
    print("\n===== MENÚ INVENTARIO =====")
    print("1. Agregar producto")
    print("2. Eliminar producto")
    print("3. Actualizar producto")
    print("4. Buscar producto por nombre")
    print("5. Mostrar todos los productos")
    print("6. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        id_producto = int(input("Ingrese ID: "))
        nombre = input("Ingrese nombre: ")
        cantidad = int(input("Ingrese cantidad: "))
        precio = float(input("Ingrese precio: "))

        producto = Producto(id_producto, nombre, cantidad, precio)
        inventario.agregar_producto(producto)

    elif opcion == "2":
        id_producto = int(input("Ingrese ID a eliminar: "))
        inventario.eliminar_producto(id_producto)

    elif opcion == "3":
        id_producto = int(input("Ingrese ID a actualizar: "))
        cantidad = input("Nueva cantidad (deje vacío si no desea cambiar): ")
        precio = input("Nuevo precio (deje vacío si no desea cambiar): ")

        nueva_cantidad = int(cantidad) if cantidad else None
        nuevo_precio = float(precio) if precio else None

        inventario.actualizar_producto(id_producto, nueva_cantidad, nuevo_precio)

    elif opcion == "4":
        nombre = input("Ingrese nombre a buscar: ")
        inventario.buscar_por_nombre(nombre)

    elif opcion == "5":
        inventario.mostrar_productos()

    elif opcion == "6":
        print("Saliendo del sistema...")
        break

    else:
        print("Opción inválida, intente nuevamente.")




