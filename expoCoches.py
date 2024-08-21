class Zona:
    def __init__(self, nombre, capacidad):
        self.__nombre = nombre
        self.__capacidad = capacidad
        self.__entradasDisponibles = capacidad

    @property
    def nombre(self):
        return self.__nombre

    @property
    def entradasDisponibles(self):
        return self.__entradasDisponibles

    def mostrarEntradasLibres(self):
        print(f"Entradas disponibles en {self.__nombre}: {self.__entradasDisponibles}")

    def venderEntradas(self, cantidad):
        if cantidad > self.__entradasDisponibles:
            print(f"No se pueden vender {cantidad} entradas en {self.__nombre}. Solo quedan {self.__entradasDisponibles}.")
        else:
            self.__entradasDisponibles -= cantidad
            print(f"Se han vendido {cantidad} entradas en {self.__nombre}. Entradas restantes: {self.__entradasDisponibles}")

    def __str__(self):
        return f"{self.__nombre} - Entradas disponibles: {self.__entradasDisponibles}"

def main():
    # Crear las zonas con las capacidades iniciales
    salaPrincipal = Zona("Sala Principal", 1000)
    zonaCompraVenta = Zona("Zona Compra-Venta", 200)
    zonaVIP = Zona("Zona VIP", 25)

    zonas = [salaPrincipal, zonaCompraVenta, zonaVIP]

    while True:
        print("\n--MENÚ--")
        print("1. Mostrar número de entradas libres")
        print("2. Vender entradas")
        print("3. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print("\nEntradas libres por zona:")
            for zona in zonas:
                print(zona)  # Utiliza el método __str__ para mostrar las entradas disponibles

        elif opcion == "2":
            print("\nSeleccione la zona para vender entradas:")
            for i, zona in enumerate(zonas, start=1):
                print(f"{i}. {zona.nombre}")

            try:
                zonaSeleccionada = int(input("Ingrese el número de la zona: ")) - 1

                if 0 <= zonaSeleccionada < len(zonas):
                    cantidad = int(input(f"Ingrese la cantidad de entradas a vender en {zonas[zonaSeleccionada].nombre}: "))
                    zonas[zonaSeleccionada].venderEntradas(cantidad)
                else:
                    print("Opción de zona no válida.")
            except ValueError:
                print("Entrada inválida. Por favor, ingrese un número.")

        elif opcion == "3":
            print("¡Gracias por usar el sistema de venta de entradas! Hasta luego.")
            break

        else:
            print("Opción no válida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    main()