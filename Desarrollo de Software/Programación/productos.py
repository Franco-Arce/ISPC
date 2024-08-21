class Producto:
    def __init__(self, nombre, precio, stock=0):
        self.__nombre = nombre         
        self.__precio = precio         
        self.__stock = stock          

    # Getters
    @property
    def nombre(self):
        return self.__nombre

    @property
    def precio(self):
        return self.__precio

    @property
    def stock(self):
        return self.__stock

    # Método para actualizar el stock
    def actualizarStock(self, cantidad):
        if isinstance(cantidad, int):
            nuevo_stock = self.__stock + cantidad
            if nuevo_stock >= 0:
                self.__stock = nuevo_stock
            else:
                raise ValueError("La cantidad resultante de stock no puede ser negativa.")
        else:
            raise ValueError("La cantidad de stock debe ser un número entero.")

    # Método para calcular el total del inventario
    def calcularInventario(self):
        return self.__stock * self.__precio

    # Método para mostrar los datos del producto
    def __str__(self):
        return (f"Nombre: {self.__nombre}\n"
                f"Precio: ${self.__precio:.2f}\n"
                f"Stock: {self.__stock}\n"
                f"Valor total del inventario: ${self.calcularInventario():.2f}")

# Aplicación de consola
def main():
    nombre = input("Ingrese el nombre del producto: ")
    precio = float(input("Ingrese el precio del producto: "))

    # Crear objeto Producto
    producto = Producto(nombre, precio)

    while True:
        print("\nOpciones:")
        print("1. Actualizar stock")
        print("2. Calcular inventario")
        print("3. Salir y mostrar datos del producto")
        
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            cantidad = int(input("Ingrese la cantidad a agregar o reducir en el stock (puede ser negativo): "))
            try:
                producto.actualizarStock(cantidad)
                print(f"Stock actualizado: {producto.stock}")
            except ValueError as e:
                print(e)

        elif opcion == "2":
            inventarioTotal = producto.calcularInventario()
            print(f"Inventario total: ${inventarioTotal:.2f}")

        elif opcion == "3":
            print("\nDatos finales del producto:")
            print(producto)
            break

        else:
            print("Opción no válida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    main()