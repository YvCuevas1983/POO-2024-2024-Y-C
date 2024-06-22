# Clase Producto que representa un producto en la tienda
class Producto:
    def __init__(self, codigo, nombre, precio, cantidad):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def __str__(self):
        return f'Producto [Código: {self.codigo}, Nombre: {self.nombre}, Precio: {self.precio}, Cantidad: {self.cantidad}]'

    def actualizar_cantidad(self, cantidad):
        self.cantidad = cantidad

# Clase Cliente que representa un cliente de la tienda
class Cliente:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email

    def __str__(self):
        return f'Cliente [Nombre: {self.nombre}, Email: {self.email}]'

# Clase Pedido que representa un pedido realizado por un cliente
class Pedido:
    def __init__(self, cliente):
        self.cliente = cliente
        self.productos = []

    def agregar_producto(self, producto, cantidad):
        if producto.cantidad >= cantidad:
            self.productos.append((producto, cantidad))
            producto.actualizar_cantidad(producto.cantidad - cantidad)
        else:
            print(f'No hay suficiente stock de {producto.nombre} para añadir {cantidad} unidades.')

    def total_pedido(self):
        total = sum(producto.precio * cantidad for producto, cantidad in self.productos)
        return total

    def __str__(self):
        detalles = '\n'.join([f'{producto.nombre} x{cantidad} - ${producto.precio * cantidad}' for producto, cantidad in self.productos])
        return f'Pedido de {self.cliente.nombre}:\n{detalles}\nTotal: ${self.total_pedido()}'

# Crear productos
producto1 = Producto(1, 'Laptop', 1000, 10)
producto2 = Producto(2, 'Mouse', 20, 50)
producto3 = Producto(3, 'Teclado', 50, 30)

# Crear cliente
cliente1 = Cliente('Carlos Ruiz', 'carlos@example.com')

# Crear pedido
pedido1 = Pedido(cliente1)
pedido1.agregar_producto(producto1, 1)
pedido1.agregar_producto(producto2, 2)

# Mostrar detalles del pedido
print(pedido1)

# Mostrar estado actualizado de los productos
print(producto1)
print(producto2)
print(producto3)
