class Moneda:
    tasas_conversion = {
        ('USD', 'PESO'): 4000,   
        ('PESO', 'USD'): 0.00025 
    }

    def __init__(self, cantidad, tipo):
        self.cantidad = cantidad
        self.tipo = tipo

    def __str__(self):
        return f"{self.cantidad:.2f} {self.tipo}"
    
    def __add__(self, otra):
        if self.tipo == otra.tipo:
            return Moneda(self.cantidad + otra.cantidad, self.tipo)
        else:
            raise ValueError("No se pueden sumar diferentes tipos de monedas")

    def convertir_a(self, nuevo_tipo):
        if self.tipo == nuevo_tipo:
            return Moneda(self.cantidad, self.tipo)
        if (self.tipo, nuevo_tipo) in Moneda.tasas_conversion:
            tasa = Moneda.tasas_conversion[(self.tipo, nuevo_tipo)]
            cantidad_convertida = self.cantidad * tasa
            return Moneda(cantidad_convertida, nuevo_tipo)
        else:
            raise ValueError(f"No se puede convertir de {self.tipo} a {nuevo_tipo}")

def menu():
    print("Conversor de Monedas")
    print("1. Convertir Pesos a Dólares")
    print("2. Convertir Dólares a Pesos")
    print("3. Salir")

def main():
    while True:
        menu()
        opcion = input("Elige una opción (1/2/3): ")

        if opcion == '1':
            cantidad_pesos = float(input("Ingrese la cantidad de pesos a convertir: "))
            pesos = Moneda(cantidad_pesos, 'PESO')
            dolares = pesos.convertir_a('USD')
            print(f"{pesos} equivale a {dolares}")

        elif opcion == '2':
            cantidad_dolares = float(input("Ingrese la cantidad de dólares a convertir: "))
            dolares = Moneda(cantidad_dolares, 'USD')
            pesos = dolares.convertir_a('PESO')
            print(f"{dolares} equivale a {pesos}")

        elif opcion == '3':
            print("Saliendo del programa.")
            break

        else:
            print("Opción no válida. Inténtelo de nuevo.")

if __name__ == "__main__":
    main()
