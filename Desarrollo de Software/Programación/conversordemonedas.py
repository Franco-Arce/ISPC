class Moneda:
    tasasCambio = {
        'USD': 1.0,         # Dólar estadounidense
        'ARS': 943.75,      # Peso argentino
        'MXN': 18.99,       # Peso mexicano
        'EUR': 0.90,        # Euro
    }

    def __init__(self, cantidad, moneda):
        if moneda not in Moneda.tasasCambio:
            raise ValueError("Moneda no soportada")
        self.cantidad = cantidad
        self.moneda = moneda

    def convertirA(self, nuevaMoneda):
        if nuevaMoneda not in Moneda.tasasCambio:
            raise ValueError("Moneda no soportada")
        tasaActual = Moneda.tasasCambio[self.moneda]
        nuevaTasa = Moneda.tasasCambio[nuevaMoneda]
        cantidadConvertida = (self.cantidad / tasaActual) * nuevaTasa
        return Moneda(cantidadConvertida, nuevaMoneda)

    def __str__(self):
        return f"{self.cantidad:.2f} {self.moneda}"

    def __add__(self, otra):
        if not isinstance(otra, Moneda):
            raise TypeError("Se puede sumar solo con otra instancia de Moneda")
        cantidadConvertida = otra.convertirA(self.moneda).cantidad
        nuevaCantidad = self.cantidad + cantidadConvertida
        return Moneda(nuevaCantidad, self.moneda)

def menu():
    while True:
        print("\n--MENÚ--")
        print("1. Convertir moneda")
        print("2. Sumar monedas")
        print("3. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            cantidad = float(input("Ingresa la cantidad: "))
            monedaOrigen = input("Ingresa la moneda de origen (USD, ARS, MXN, EUR): ").upper()
            monedaDestino = input("Ingresa la moneda de destino (USD, ARS, MXN, EUR): ").upper()

            try:
                m = Moneda(cantidad, monedaOrigen)
                convertido = m.convertirA(monedaDestino)
                print(f"\nResultado: {convertido}")
            except ValueError as e:
                print(f"Error: {e}")

        elif opcion == '2':
            cantidad1 = float(input("Ingresa la cantidad de la primera moneda: "))
            moneda1 = input("Ingresa la primera moneda (USD, ARS, MXN, EUR): ").upper()
            cantidad2 = float(input("Ingresa la cantidad de la segunda moneda: "))
            moneda2 = input("Ingresa la segunda moneda (USD, ARS, MXN, EUR): ").upper()

            try:
                m1 = Moneda(cantidad1, moneda1)
                m2 = Moneda(cantidad2, moneda2)
                suma = m1 + m2
                print(f"\nResultado de la suma: {suma}")
            except (ValueError, TypeError) as e:
                print(f"Error: {e}")

        elif opcion == '3':
            print("Saliendo.")
            break

        else:
            print("Opción no válida. Inténtalo de nuevo.")

# Ejecutar el menú interactivo
menu()
