# Definición de la clase base
class Animal:
    def __init__(self, nombre):
        self.__nombre = nombre  # Encapsulación del nombre del animal

    def get_nombre(self):
        return self.__nombre

    def hacer_sonido(self):
        pass  # Método que será sobrescrito en las clases derivadas


# Definición de una clase derivada
class Perro(Animal):
    def __init__(self, nombre, raza):
        super().__init__(nombre)
        self.__raza = raza  # Encapsulación de la raza del perro

    def get_raza(self):
        return self.__raza

    def hacer_sonido(self):
        return "Guau!"  # Polimorfismo: método sobrescrito


# Creación de instancias y uso de los métodos
def main():
    # Crear una instancia de la clase derivada
    mi_perro = Perro("niña", "rottweiler")

    # Utilizar métodos para demostrar funcionalidad
    print(f"Nombre del perro: {mi_perro.get_nombre()}")
    print(f"Raza del perro: {mi_perro.get_raza()}")
    print(f"Sonido del perro: {mi_perro.hacer_sonido()}")


if __name__ == "__main__":
    main()