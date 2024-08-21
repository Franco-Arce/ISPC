class Zona:
    def __init__(self, nombre, capacidad):
        self.nombre = nombre
        self.capacidad = capacidad
        self.entradas_disponibles = capacidad

    def mostrar_entradas(self):
        return f"Zona: {self.nombre} | Entradas disponibles: {self.entradas_disponibles}"

    def vender_entradas(self, cantidad):
        if cantidad <= self.entradas_disponibles:
            self.entradas_disponibles -= cantidad
            return True
        else:
            return False

def menu():
    print("\nGestión de Entradas - Expocoches")
    print("1. Mostrar número de entradas libres")
    print("2. Vender entradas")
    print("3. Salir")

def main():
    # Crear zonas
    zona_principal = Zona("Sala Principal", 1000)
    zona_compra_venta = Zona("Zona Compra-Venta", 200)
    zona_vip = Zona("Zona VIP", 25)

    zonas = {
        "1": zona_principal,
        "2": zona_compra_venta,
        "3": zona_vip
    }

    while True:
        menu()
        opcion = input("Elige una opción (1/2/3): ")

        if opcion == '1':
            print("\n-- ENTRADAS LIBRES --")
            for zona in zonas.values():
                print(zona.mostrar_entradas())

        elif opcion == '2':
            print("\n-- VENDER ENTRADAS --")
            print("1. Sala Principal")
            print("2. Zona Compra-Venta")
            print("3. Zona VIP")

            zona_opcion = input("Elige la zona (1/2/3): ")
            if zona_opcion in zonas:
                cantidad = int(input("¿Cuántas entradas deseas vender? "))
                zona = zonas[zona_opcion]
                if zona.vender_entradas(cantidad):
                    print(f"Se han vendido {cantidad} entradas en la {zona.nombre}.")
                else:
                    print(f"No hay suficientes entradas disponibles en la {zona.nombre}.")
            else:
                print("Opción de zona no válida.")

        elif opcion == '3':
            print("Saliendo del programa.")
            break

        else:
            print("Opción no válida. Inténtelo de nuevo.")

if __name__ == "__main__":
    main()
