from datetime import datetime, timedelta

class Producto:
    idCounter = 1

    def __init__(self, nombre, caducidad, precio):
        self.id = Producto.idCounter
        self.nombre = nombre
        self.caducidad = datetime.strptime(caducidad, '%Y-%m-%d')
        self.precioOriginal = precio
        self.precio = precio
        Producto.idCounter += 1
    
    def calcularPrecio(self):
        diasRestantes = (self.caducidad - datetime.now()).days
        if diasRestantes < 0:
            raise ValueError(f"El producto '{self.nombre}' está vencido y no se puede vender.")
        elif diasRestantes < 3:
            self.precio = self.precioOriginal * 0.3
        elif diasRestantes <= 5:
            self.precio = self.precioOriginal * 0.6
        else:
            self.precio = self.precioOriginal
    
    def __str__(self):
        return (f"ID: {self.id} | Nombre: {self.nombre} | Caducidad: {self.caducidad.strftime('%Y-%m-%d')} | "
                f"Precio: ${self.precio:.2f}")

class Tienda:
    def __init__(self):
        self.productos = []

    def agregarProducto(self, nombre, caducidad, precio):
        producto = Producto(nombre, caducidad, precio)
        producto.calcularPrecio()
        self.productos.append(producto)
        print(f"Producto agregado: {producto}")
    
    def mostrarProductos(self):
        print("\n--PRODUCTOS EN LA TIENDA--")
        for producto in self.productos:
            print(producto)
    
    def comprarProducto(self, idProducto):
        for producto in self.productos:
            if producto.id == idProducto:
                try:
                    producto.calcularPrecio()
                    self.productos.remove(producto)
                    print(f"\nCompraste: {producto.nombre} por ${producto.precio:.2f}")
                    return
                except ValueError as e:
                    print(e)
                    return
        print(f"No se encontró el producto. ID: {idProducto}")

# Ejemplo de uso
if __name__ == "__main__":
    tienda = Tienda()

    # Agregar producto
    tienda.agregarProducto("Leche", "2024-08-25", 10.00)
    tienda.agregarProducto("Queso", "2024-08-23", 15.00)
    tienda.agregarProducto("Pan", "2024-08-21", 5.00)

    # Mostrar productos
    tienda.mostrarProductos()

    # Comprar un producto
    tienda.comprarProducto(2)  # Comprar Queso
    tienda.comprarProducto(3)  # Comprar Pan (puede estar vencido según la fecha actual)

    # Mostrar restantes
    tienda.mostrarProductos()