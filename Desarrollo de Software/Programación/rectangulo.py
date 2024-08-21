class Rectangulo:
    def __init__(self, largo, ancho):
        self.__largo = largo
        self.__ancho = ancho

    # Método calcular area
    def calcularArea(self):
        return self.__largo * self.__ancho
    
    # Método calcular perimetro
    def calcularPerimetro(self):
        return 2 * (self.__largo + self.__ancho)

# APLICACIÓN DE CONSOLA
def main():
    print("Aplicación para calcular el área y el perímetro de un rectángulo.")
    
    largo = float(input("Ingrese el largo del rectángulo: "))
    ancho = float(input("Ingrese el ancho del rectángulo: "))
    
    rectangulo = Rectangulo(largo, ancho)
    
    while True:
        print("\nSeleccione una opción:")
        print("1 - Calcular área")
        print("2 - Calcular perímetro")
        print("3 - Salir")
        
        opcion = input("Ingrese su opción: ")

        if opcion == "1":
            area = rectangulo.calcularArea()
            print(f"El área del rectángulo es: {area}")
        elif opcion == "2":
            perimetro = rectangulo.calcularPerimetro()
            print(f"El perímetro del rectángulo es: {perimetro}")
        elif opcion == "3":
            print("Gracias por usar la aplicación.")
            break
        else:
            print("Opción no válida, intente de nuevo.")

if __name__ == "__main__":
    main()