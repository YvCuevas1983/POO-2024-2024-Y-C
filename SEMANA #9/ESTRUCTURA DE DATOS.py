class Producto:
    def __init__(self, id, nombre, cantidad, precio):
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id

    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_cantidad(self):
        return self.cantidad

    def set_cantidad(self, cantidad):
        self.cantidad = cantidad

    def get_precio(self):
        return self.precio

    def set_precio(self, precio):
        self.precio = precio

    def __str__(self):
        return f"ID: {self.id}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: {self.precio}"


class Inventario:
    def __init__(self):
        self.productos = []

    def añadir_producto(self, producto):
        # Verificar si el ID ya existe
        if any(p.get_id() == producto.get_id() for p in self.productos):
            print("El ID ya existe.")
            return False
        self.productos.append(producto)
        return True

    def eliminar_producto_por_id(self, id):
        self.productos = [p for p in self.productos if p.get_id() != id]
        return True

    def actualizar_producto(self, id, nueva_cantidad=None, nuevo_precio=None):
        for producto in self.productos:
            if producto.get_id() == id:
                if nueva_cantidad is not None:
                    producto.set_cantidad(nueva_cantidad)
                if nuevo_precio is not None:
                    producto.set_precio(nuevo_precio)
                return True
        return False

    def buscar_productos_por_nombre(self, nombre):
        resultados = [p for p in self.productos if nombre.lower() in p.get_nombre().lower()]
        return resultados

    def mostrar_productos(self):
        if not self.productos:
            print("El inventario está vacío.")
        else:
            for producto in self.productos:
                print(producto)


def mostrar_menu():
    print("\nMenú de Inventario:")
    print("1. Añadir nuevo producto")
    print("2. Eliminar producto por ID")
    print("3. Actualizar cantidad o precio de un producto")
    print("4. Buscar producto(s) por nombre")
    print("5. Mostrar todos los productos")
    print("6. Salir")


def main():
    import sys
    inventario = Inventario()
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            id = input("Ingrese ID del producto: ")
            nombre = input("Ingrese nombre del producto: ")
            cantidad = int(input("Ingrese cantidad del producto: "))
            precio = float(input("Ingrese precio del producto: "))
            producto = Producto(id, nombre, cantidad, precio)
            if inventario.añadir_producto(producto):
                print("Producto añadido correctamente.")

        elif opcion == '2':
            id = input("Ingrese ID del producto a eliminar: ")
            inventario.eliminar_producto_por_id(id)
            print("Producto eliminado correctamente.")

        elif opcion == '3':
            id = input("Ingrese ID del producto a actualizar: ")
            nueva_cantidad = input("Ingrese nueva cantidad (deje en blanco si no desea cambiarla): ")
            nuevo_precio = input("Ingrese nuevo precio (deje en blanco si no desea cambiarlo): ")
            nueva_cantidad = int(nueva_cantidad) if nueva_cantidad else None
            nuevo_precio = float(nuevo_precio) if nuevo_precio else None
            if inventario.actualizar_producto(id, nueva_cantidad, nuevo_precio):
                print("Producto actualizado correctamente.")
            else:
                print("No se encontró el producto con el ID dado.")

        elif opcion == '4':
            nombre = input("Ingrese nombre del producto a buscar: ")
            resultados = inventario.buscar_productos_por_nombre(nombre)
            if not resultados:
                print("No se encontraron productos con el nombre dado.")
            else:
                print("Productos encontrados:")
                for p in resultados:
                    print(p)

        elif opcion == '5':
            inventario.mostrar_productos()

        elif opcion == '6':
            print("Saliendo...")
            sys.exit()

        else:
            print("Opción no válida. Intente de nuevo.")


if __name__ == "__main__":
    main()
