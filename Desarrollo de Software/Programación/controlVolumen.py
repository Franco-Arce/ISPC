class ControlVolumen:
    MIN_VOLUMEN = 1
    MAX_VOLUMEN = 10

    def __init__(self, volumen_medio=5):
        self.volumen = volumen_medio
    
    def ajustar_volumen(self, ajuste):
        nuevo_volumen = self.volumen + ajuste
        if nuevo_volumen < ControlVolumen.MIN_VOLUMEN:
            self.volumen = ControlVolumen.MIN_VOLUMEN
        elif nuevo_volumen > ControlVolumen.MAX_VOLUMEN:
            self.volumen = ControlVolumen.MAX_VOLUMEN
        else:
            self.volumen = nuevo_volumen
    
    def __str__(self):
        return f"Nivel de volumen actual: {self.volumen}"

def menu():
    print("\nControl de Volumen")
    print("1. Aumentar Volumen")
    print("2. Disminuir Volumen")
    print("3. Consultar Nivel de Volumen")
    print("4. Salir")

def main():
    control_volumen = ControlVolumen()

    while True:
        menu()
        opcion = input("Elige una opción (1/2/3/4): ")

        if opcion == '1':
            ajuste = int(input("Ingrese la cantidad para aumentar el volumen: "))
            control_volumen.ajustar_volumen(ajuste)
            print("Volumen ajustado.")

        elif opcion == '2':
            ajuste = int(input("Ingrese la cantidad para disminuir el volumen: "))
            control_volumen.ajustar_volumen(-ajuste)
            print("Volumen ajustado.")

        elif opcion == '3':
            print(control_volumen)

        elif opcion == '4':
            print("Saliendo del programa.")
            print(control_volumen)  # Mostrar el nivel final de volumen
            break

        else:
            print("Opción no válida. Inténtelo de nuevo.")

if __name__ == "__main__":
    main()
