import datetime

class Producto:
    id_counter = 1  # Contador para asignar IDs automáticamente

    def __init__(self, nombre, fecha_caducidad, precio):
        self.id = Producto.id_counter
        Producto.id_counter += 1
        self.nombre = nombre
        self.fecha_caducidad = fecha_caducidad
        self.precio = precio

    def calcular_precio_con_descuento(self):
        hoy = datetime.date.today()
        dias_restantes = (self.fecha_caducidad - hoy).days
        
        if dias_restantes < 0:
            return 0  # Producto vencido, no se puede vender
        elif dias_restantes < 3:
            return self.precio * 0.3  # 70% de descuento
        elif 3 <= dias_restantes <= 5:
            return self.precio * 0.6  # 40% de descuento
        else:
            return self.precio  # Precio normal

    def __str__(self):
        return (f"ID: {self.id}, Nombre: {self.nombre}, "
                f"Fecha de Caducidad: {self.fecha_caducidad}, "
                f"Precio Original: {self.precio:.2f}, "
                f"Precio con Descuento: {self.calcular_precio_con_descuento():.2f}")

def menu():
    print("\nGestión de Compra de Productos")
    print("1. Agregar Producto")
    print("2. Mostrar Productos Disponibles")
    print("3. Salir")

def main():
    productos = []

    while True:
        menu()
        opcion = input("Elige una opción (1/2/3): ")

        if opcion == '1':
            nombre = input("Ingrese el nombre del producto: ")
            fecha_caducidad_input = input("Ingrese la fecha de caducidad (YYYY-MM-DD): ")
            fecha_caducidad = datetime.datetime.strptime(fecha_caducidad_input, '%Y-%m-%d').date()
            precio = float(input("Ingrese el precio del producto: "))
            
            producto = Producto(nombre, fecha_caducidad, precio)
            productos.append(producto)
            print("Producto agregado exitosamente.")

        elif opcion == '2':
            print("\nProductos Disponibles:")
            for producto in productos:
                if producto.calcular_precio_con_descuento() > 0:
                    print(producto)
                else:
                    print(f"ID: {producto.id}, Nombre: {producto.nombre} - Producto vencido y no disponible para la venta.")

        elif opcion == '3':
            print("Saliendo del programa.")
            break

        else:
            print("Opción no válida. Inténtelo de nuevo.")

if __name__ == "__main__":
    main()
