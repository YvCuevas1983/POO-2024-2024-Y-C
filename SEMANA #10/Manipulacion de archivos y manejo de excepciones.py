# Clase Producto
class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):  # Constructor inicializa atributos de Producto
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def a_cadena(self):
        # Convierte el objeto Producto en una cadena CSV
        return f"{self.id_producto},{self.nombre},{self.cantidad},{self.precio}"

    @staticmethod
    def from_cadena(product_str):
        # Crea un objeto Producto a partir de una cadena CSV
        id_producto, nombre, cantidad, precio = product_str.split(',')
        return Producto(id_producto, nombre, int(cantidad), float(precio))

# Clase Inventario
class Inventario:
    def __init__(self, archivo):  # Constructor recibe la ruta del archivo donde se almacenan los productos
        self.archivo = archivo

    def añadir_producto(self, producto):
        # Verifica si el producto ya existe antes de añadirlo
        if self.mostrar_producto_por_id(producto.id_producto):
            return False
        try:
            with open(self.archivo, 'a') as f:
                f.write(producto.a_cadena() + '\n')  # Añade el producto al archivo
            return True
        except PermissionError:
            print("Error: No se tienen permisos para escribir en el archivo.")
            return False
        except Exception as e:
            print(f"Error inesperado al añadir producto: {e}")
            return False

    def eliminar_producto(self, id_producto):
        try:
            productos = self.leer_productos()
            # Filtra productos para eliminar el que coincide con id_producto
            productos_actualizados = [p for p in productos if p.id_producto != id_producto]
            if len(productos_actualizados) < len(productos):
                self.guardar_productos(productos_actualizados)
                return True
            return False
        except PermissionError:
            print("Error: No se tienen permisos para modificar el archivo.")
            return False
        except Exception as e:
            print(f"Error inesperado al eliminar producto: {e}")
            return False

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        try:
            productos = self.leer_productos()
            for p in productos:
                if p.id_producto == id_producto:
                    # Actualiza la cantidad y/o el precio si se proveen
                    if cantidad is not None:
                        p.cantidad = cantidad
                    if precio is not None:
                        p.precio = precio
                    self.guardar_productos(productos)
                    return True
            return False
        except PermissionError:
            print("Error: No se tienen permisos para modificar el archivo.")
            return False
        except Exception as e:
            print(f"Error inesperado al actualizar producto: {e}")
            return False

    def buscar_producto(self, nombre):
        try:
            productos = self.leer_productos()
            # Filtra productos que contienen el nombre buscado (sin distinguir mayúsculas/minúsculas)
            resultados = [p for p in productos if nombre.lower() in p.nombre.lower()]
            return resultados
        except Exception as e:
            print(f"Error inesperado al buscar producto: {e}")
            return []

    def mostrar_producto_por_id(self, id_producto):
        try:
            productos = self.leer_productos()
            for p in productos:
                if p.id_producto == id_producto:
                    return p  # Devuelve el producto si se encuentra
            return None
        except Exception as e:
            print(f"Error inesperado al mostrar producto por ID: {e}")
            return None

    def mostrar_productos(self):
        try:
            return self.leer_productos()  # Devuelve todos los productos del inventario
        except Exception as e:
            print(f"Error inesperado al mostrar todos los productos: {e}")
            return []

    def leer_productos(self):
        productos = []
        try:
            with open(self.archivo, 'r') as f:
                for line in f:
                    productos.append(Producto.from_cadena(line.strip()))  # Crea productos a partir de las líneas del archivo
        except FileNotFoundError:
            print(f"Error: El archivo '{self.archivo}' no se encontró.")
        except PermissionError:
            print(f"Error: No se tienen permisos para leer el archivo '{self.archivo}'.")
        except Exception as e:
            print(f"Error inesperado al leer productos: {e}")
        return productos

    def guardar_productos(self, productos):
        try:
            with open(self.archivo, 'w') as f:
                for p in productos:
                    f.write(p.a_cadena() + '\n')  # Guarda todos los productos en el archivo
        except PermissionError:
            print(f"Error: No se tienen permisos para escribir en el archivo '{self.archivo}'.")
        except Exception as e:
            print(f"Error inesperado al guardar productos: {e}")

# Clase para administrar el inventario desde la consola
class AdministrarTienda:
    def __init__(self, archivo):  # Constructor inicializa el inventario con el archivo dado
        self.inventario = Inventario(archivo)
        self.menu_principal()

    def menu_principal(self):
        while True:
            # Menú principal para las operaciones de la tienda
            print("\n--- MOVIMIENTOS DE TIENDA ---")
            print("1. Añadir producto")
            print("2. Buscar producto")
            print("3. Eliminar producto")
            print("4. Mostrar todos los productos")
            print("5. Salir")
            opcion = input("Selecciona una opción: ")

            if opcion == "1":
                self.ingreso_productos()
            elif opcion == "2":
                self.formulario_busqueda_producto()
            elif opcion == "3":
                self.formulario_eliminar_producto()
            elif opcion == "4":
                self.mostrar_todos_los_productos()
            elif opcion == "5":
                print("Saliendo... gracias por peferir nuestro sistema 💖🎈😍")
                break
            else:
                print("Opción no válida. Inténtalo de nuevo.")

    def ingreso_productos(self):
        # Formulario para ingresar un nuevo producto
        id_producto = input("ID Producto: ")
        nombre_producto = input("Nombre: ")
        cantidad_producto = input("Cantidad: ")
        precio_producto = input("Precio: ")

        if not all([id_producto, nombre_producto, cantidad_producto, precio_producto]):
            print("Advertencia: Todos los campos deben ser completados.")
            return

        producto_existente = self.inventario.mostrar_producto_por_id(id_producto)
        if producto_existente:
            # Actualiza el producto existente si ya se encuentra en el inventario
            producto_existente.nombre = nombre_producto
            producto_existente.cantidad = int(cantidad_producto)
            producto_existente.precio = float(precio_producto)
            self.inventario.actualizar_producto(id_producto, producto_existente.cantidad, producto_existente.precio)
            print("Producto actualizado correctamente.")
        else:
            # Añade un nuevo producto al inventario
            producto = Producto(id_producto, nombre_producto, int(cantidad_producto), float(precio_producto))
            if self.inventario.añadir_producto(producto):
                print("Producto añadido correctamente.")
            else:
                print("Error: ID del producto ya existe o se produjo un error al añadir el producto.")

    def formulario_busqueda_producto(self):
        # Formulario para buscar un producto por nombre
        nombre = input("Nombre del producto a buscar: ")
        resultados = self.inventario.buscar_producto(nombre)
        if resultados:
            for p in resultados:
                print(f"ID: {p.id_producto}, Nombre: {p.nombre}, Cantidad: {p.cantidad}, Precio: {p.precio}")
        else:
            print("No se encontraron productos.")

    def formulario_eliminar_producto(self):
        # Formulario para eliminar un producto por ID
        id_producto = input("ID del producto a eliminar: ")
        if self.inventario.eliminar_producto(id_producto):
            print("Producto eliminado correctamente.")
        else:
            print("Error: Producto no encontrado o se produjo un error al eliminar el producto.")

    def mostrar_todos_los_productos(self):
        # Muestra todos los productos en el inventario
        productos = self.inventario.mostrar_productos()
        if productos:
            for p in productos:
                print(f"ID: {p.id_producto}, Nombre: {p.nombre}, Cantidad: {p.cantidad}, Precio: {p.precio}")
        else:
            print("No hay productos en el inventario o se produjo un error al mostrar los productos.")

# Ejecutar la aplicación
if __name__ == "__main__":
    archivo_inventario = "inventario.txt"
    AdministrarTienda(archivo_inventario)

