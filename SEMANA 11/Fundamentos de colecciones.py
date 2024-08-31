class Producto:
    def __init__(self, producto_id, nombre, cantidad, precio):
        self.producto_id = producto_id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def obtener_id(self):
        return self.producto_id

    def obtener_nombre(self):
        return self.nombre

    def obtener_cantidad(self):
        return self.cantidad

    def obtener_precio(self):
        return self.precio

    def establecer_nombre(self, nombre):
        self.nombre = nombre

    def establecer_cantidad(self, cantidad):
        self.cantidad = cantidad

    def establecer_precio(self, precio):
        self.precio = precio

    def __str__(self):
        return f"ID: {self.producto_id}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: {self.precio}"


import json

class Inventario:
    def __init__(self):
        self.productos = {}

    def añadir_producto(self, producto):
        self.productos[producto.obtener_id()] = producto

    def eliminar_producto(self, producto_id):
        if producto_id in self.productos:
            del self.productos[producto_id]

    def actualizar_producto(self, producto_id, nombre=None, cantidad=None, precio=None):
        if producto_id in self.productos:
            producto = self.productos[producto_id]
            if nombre is not None:
                producto.establecer_nombre(nombre)
            if cantidad is not None:
                producto.establecer_cantidad(cantidad)
            if precio is not None:
                producto.establecer_precio(precio)

    def buscar_producto_por_nombre(self, nombre):
        encontrados = [p for p in self.productos.values() if p.obtener_nombre().lower() == nombre.lower()]
        return encontrados

    def mostrar_todos_productos(self):
        for producto in self.productos.values():
            print(producto)

    def guardar_inventario(self, archivo):
        with open(archivo, 'w') as f:
            json.dump({p_id: p.__dict__ for p_id, p in self.productos.items()}, f)

    def cargar_inventario(self, archivo):
        try:
            with open(archivo, 'r') as f:
                datos = json.load(f)
                self.productos = {p_id: Producto(**p) for p_id, p in datos.items()}
        except FileNotFoundError:
            print("El archivo no existe.")


def mostrar_menu():
    print("\n--- Menú de Inventario ---")
    print("1. Añadir Producto")
    print("2. Eliminar Producto")
    print("3. Actualizar Producto")
    print("4. Buscar Producto por Nombre")
    print("5. Mostrar Todos los Productos")
    print("6. Guardar Inventario")
    print("7. Cargar Inventario")
    print("8. Salir")


def main():
    inventario = Inventario()
    archivo_inventario = 'inventario.json'

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            producto_id = input("ID del producto: ")
            nombre = input("Nombre del producto: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            producto = Producto(producto_id, nombre, cantidad, precio)
            inventario.añadir_producto(producto)
        elif opcion == '2':
            producto_id = input("ID del producto a eliminar: ")
            inventario.eliminar_producto(producto_id)
        elif opcion == '3':
            producto_id = input("ID del producto a actualizar: ")
            nombre = input("Nuevo nombre (dejar en blanco para no cambiar): ")
            cantidad = input("Nueva cantidad (dejar en blanco para no cambiar): ")
            precio = input("Nuevo precio (dejar en blanco para no cambiar): ")
            cantidad = int(cantidad) if cantidad else None
            precio = float(precio) if precio else None
            inventario.actualizar_producto(producto_id, nombre or None, cantidad, precio)
        elif opcion == '4':
            nombre = input("Nombre del producto a buscar: ")
            productos_encontrados = inventario.buscar_producto_por_nombre(nombre)
            for producto in productos_encontrados:
                print(producto)
        elif opcion == '5':
            inventario.mostrar_todos_productos()
        elif opcion == '6':
            inventario.guardar_inventario(archivo_inventario)
        elif opcion == '7':
            inventario.cargar_inventario(archivo_inventario)
        elif opcion == '8':
            break
        else:
            print("Opción no válida. Intente nuevamente.")


if __name__ == "__main__":
    main()
