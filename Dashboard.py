import os


def mostrar_codigo(ruta_script):
    # Asegúrate de que la ruta al script es absoluta
    ruta_script_absoluta = os.path.abspath(ruta_script)
    print(f"Ruta absoluta del archivo: {ruta_script_absoluta}")

    try:
        with open(ruta_script_absoluta, 'r', encoding='utf-8') as archivo:
            print(f"\n--- Código de {ruta_script} ---\n")
            print(archivo.read())
    except FileNotFoundError:
        print("El archivo no se encontró.")
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo: {e}")


def mostrar_menu():
    # Define la ruta base donde se encuentra el dashboard.py
    ruta_base = os.path.dirname(os.path.abspath(__file__))
    print(f"Directorio base: {ruta_base}")

    # Imprime la lista de archivos en el directorio base para verificación
    print(f"Archivos en el directorio base: {os.listdir(ruta_base)}")

    opciones = {
        '1': 'SEMANA #2/Tarea de la semana #2 POO (Ejemplos).py',
        '2': 'TAREA DE LA SEMANA #3/EJERECICIO POO.py',
        '3': 'TAREA DE LA SEMANA #3/PROGRAMACIÓN TRADICIONAL.py',
        '4': 'SEMANA #4/Tarea de la semana #4.py',
        '5': 'SEMANA #5/Tipos de datos, Identificadores--semana-5.py',
        '6': 'SEMANA#6/Clases, objetos, herencia, encapsulamiento y polimorfismo.py',
        '7': 'SEMANA #7/Semana 7 -- Constructores y Destructores.py'

    }

    while True:
        print("\nProject - Dashboard")
        # Imprime las opciones del menú
        for key in opciones:
            print(f"{key} - {opciones[key]}")
        print("0 - Salir")

        eleccion = input("Elige un script para ver su código o '0' para salir: ")
        if eleccion == '0':
            break
        elif eleccion in opciones:
            # Asegura que el path sea absoluto
            ruta_script = os.path.join(ruta_base, opciones[eleccion])
            print(f"Ruta completa del script seleccionado: {ruta_script}")
            mostrar_codigo(ruta_script)
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")


# Ejecutar el dashboard
if __name__ == "__main__":
    mostrar_menu()