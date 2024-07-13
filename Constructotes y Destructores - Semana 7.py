# Clase que representa un archivo
class Archivo:
    # Constructor que se ejecuta al crear una instancia de la clase
    def __init__(self, nombre_archivo, modo):
        # Inicializa los atributos del objeto
        self.nombre_archivo = nombre_archivo
        self.modo = modo
        # Abre el archivo en el modo especificado
        self.archivo = open(nombre_archivo, modo)
        print(f"Archivo '{self.nombre_archivo}' abierto en modo '{self.modo}'.")

    # Método para escribir datos en el archivo
    def escribir(self, datos):
        if 'w' in self.modo or 'a' in self.modo:
            self.archivo.write(datos)
            print(f"Datos escritos en el archivo '{self.nombre_archivo}'.")
        else:
            print(f"No se puede escribir en el archivo '{self.nombre_archivo}' en modo '{self.modo}'.")

    # Destructor que se ejecuta al eliminar la instancia de la clase
    def __del__(self):
        # Cierra el archivo
        self.archivo.close()
        print(f"Archivo '{self.nombre_archivo}' cerrado.")

# Ejemplo de uso de la clase Archivo
def main():
    # Crear una instancia de la clase Archivo
    archivo = Archivo('mi_archivo.txt', 'w')
    # Escribir datos en el archivo
    archivo.escribir('Hola, mundo!\n')
    # Al finalizar la función, el destructor se activará y cerrará el archivo

if __name__ == '__main__':
    main()

# En este punto, el archivo se cerrará automáticamente ya que la instancia
# de la clase Archivo será destruida al salir del ámbito de la función main.
