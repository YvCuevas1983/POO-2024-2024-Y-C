class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        self.info = (titulo, autor)  # Tupla inmutable para título y autor
        self.categoria = categoria
        self.isbn = isbn

    def __str__(self):
        return f"'{self.info[0]}' por {self.info[1]} (Categoría: {self.categoria}, ISBN: {self.isbn})"


class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []  # Lista de libros actualmente prestados

    def __str__(self):
        return f"Usuario: {self.nombre}, ID: {self.id_usuario}, Libros prestados: {len(self.libros_prestados)}"


class Biblioteca:
    def __init__(self):
        self.libros = {}  # Diccionario de libros {ISBN: Libro}
        self.usuarios = {}  # Diccionario de usuarios {ID: Usuario}
        self.usuarios_registrados = set()  # Conjunto de IDs de usuarios

    def agregar_libro(self, libro):
        if libro.isbn in self.libros:
            print(f"El libro con ISBN {libro.isbn} ya está en la biblioteca.")
        else:
            self.libros[libro.isbn] = libro
            print(f"Libro añadido: {libro}")

    def quitar_libro(self, isbn):
        if isbn in self.libros:
            del self.libros[isbn]
            print(f"Libro con ISBN {isbn} eliminado de la biblioteca.")
        else:
            print(f"No se encontró el libro con ISBN {isbn}.")

    def registrar_usuario(self, usuario):
        if usuario.id_usuario in self.usuarios_registrados:
            print(f"El usuario con ID {usuario.id_usuario} ya está registrado.")
        else:
            self.usuarios[usuario.id_usuario] = usuario
            self.usuarios_registrados.add(usuario.id_usuario)
            print(f"Usuario registrado: {usuario}")

    def dar_baja_usuario(self, id_usuario):
        if id_usuario in self.usuarios_registrados:
            if self.usuarios[id_usuario].libros_prestados:
                print(f"El usuario tiene libros prestados y no puede ser dado de baja.")
            else:
                del self.usuarios[id_usuario]
                self.usuarios_registrados.remove(id_usuario)
                print(f"Usuario con ID {id_usuario} dado de baja.")
        else:
            print(f"No se encontró el usuario con ID {id_usuario}.")

    def prestar_libro(self, isbn, id_usuario):
        if isbn not in self.libros:
            print(f"El libro con ISBN {isbn} no está disponible.")
        elif id_usuario not in self.usuarios_registrados:
            print(f"No se encontró el usuario con ID {id_usuario}.")
        else:
            usuario = self.usuarios[id_usuario]
            libro = self.libros[isbn]
            usuario.libros_prestados.append(libro)
            del self.libros[isbn]
            print(f"Libro '{libro.info[0]}' prestado a {usuario.nombre}.")

    def devolver_libro(self, isbn, id_usuario):
        if id_usuario not in self.usuarios_registrados:
            print(f"No se encontró el usuario con ID {id_usuario}.")
            return

        usuario = self.usuarios[id_usuario]
        libro_prestado = next((libro for libro in usuario.libros_prestados if libro.isbn == isbn), None)

        if libro_prestado:
            usuario.libros_prestados.remove(libro_prestado)
            self.libros[isbn] = libro_prestado
            print(f"Libro '{libro_prestado.info[0]}' devuelto por {usuario.nombre}.")
        else:
            print(f"El usuario no tiene el libro con ISBN {isbn} prestado.")

    def buscar_libro(self, titulo=None, autor=None, categoria=None):
        resultados = []
        for libro in self.libros.values():
            if (titulo and titulo.lower() in libro.info[0].lower()) or \
                    (autor and autor.lower() in libro.info[1].lower()) or \
                    (categoria and categoria.lower() in libro.categoria.lower()):
                resultados.append(libro)

        if resultados:
            print("Resultados de búsqueda:")
            for libro in resultados:
                print(libro)
        else:
            print("No se encontraron libros que coincidan con los criterios de búsqueda.")

    def listar_libros_prestados(self, id_usuario):
        if id_usuario not in self.usuarios_registrados:
            print(f"No se encontró el usuario con ID {id_usuario}.")
        else:
            usuario = self.usuarios[id_usuario]
            if usuario.libros_prestados:
                print(f"Libros prestados por {usuario.nombre}:")
                for libro in usuario.libros_prestados:
                    print(libro)
            else:
                print(f"{usuario.nombre} no tiene libros prestados.")


# Ejemplo alternativo de uso del sistema
biblioteca = Biblioteca()

# Crear libros
libro3 = Libro("Orgullo y Prejuicio", "Jane Austen", "Novela Romántica", "1111111111")
libro4 = Libro("1984", "George Orwell", "Distopía", "2222222222")
libro5 = Libro("El Principito", "Antoine de Saint-Exupéry", "Fábula", "3333333333")

# Agregar libros a la biblioteca
biblioteca.agregar_libro(libro3)
biblioteca.agregar_libro(libro4)
biblioteca.agregar_libro(libro5)

# Crear usuarios
usuario3 = Usuario("Carlos Ruiz", "U003")
usuario4 = Usuario("Ana Gómez", "U004")

# Registrar usuarios
biblioteca.registrar_usuario(usuario3)
biblioteca.registrar_usuario(usuario4)

# Prestar libros
biblioteca.prestar_libro("1111111111", "U003")  # Prestar "Orgullo y Prejuicio" a Carlos Ruiz
biblioteca.prestar_libro("2222222222", "U004")  # Prestar "1984" a Ana Gómez

# Listar libros prestados
biblioteca.listar_libros_prestados("U003")
biblioteca.listar_libros_prestados("U004")

# Devolver libros
biblioteca.devolver_libro("1111111111", "U003")  # Devolver "Orgullo y Prejuicio" por Carlos Ruiz
biblioteca.devolver_libro("2222222222", "U004")  # Devolver "1984" por Ana Gómez

# Buscar libros
biblioteca.buscar_libro(autor="Jane Austen")  # Buscar libros por autor
biblioteca.buscar_libro(categoria="Distopía")  # Buscar libros por categoría

# Dar de baja a un usuario
biblioteca.dar_baja_usuario("U003")  # Dar de baja a Carlos Ruiz
biblioteca.dar_baja_usuario("U004")  # Dar de baja a Ana Gómez
