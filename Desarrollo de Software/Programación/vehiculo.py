class Vehiculo:
    def __init__(self, color, marca, modelo, patente):
        self.color = color
        self.marca = marca
        self.modelo = modelo
        self.patente = patente
        self.__kilometraje = 0  # Atributo privado

    def conducir(self, km):
        if km > 0:
            self.__kilometraje += km
            print(f"Has conducido {km} kilómetros.")
        else:
            raise ValueError("La cantidad de kilómetros debe ser positiva.")

    @property
    def kilometraje(self):
        return self.__kilometraje

    def __str__(self):
        return (f"Datos del Vehículo:\n"
                f"Marca: {self.marca}\n"
                f"Modelo: {self.modelo}\n"
                f"Color: {self.color}\n"
                f"Patente: {self.patente}\n"
                f"Kilometraje recorrido: {self.kilometraje} km\n")

# Aplicación de consola
def main():
    # Crear una instancia del vehículo con los datos del usuario
    color = input("Ingrese el color del vehículo: ")
    marca = input("Ingrese la marca del vehículo: ")
    modelo = input("Ingrese el modelo del vehículo: ")
    patente = input("Ingrese la patente del vehículo: ")

    vehiculo = Vehiculo(color, marca, modelo, patente)

    # Conducir y mostrar kilometraje hasta que el usuario decida detenerse
    while True:
        km = input("Ingrese los kilómetros a conducir (o 'salir' para terminar): ")
        if km.lower() == 'salir':
            break
        try:
            km = float(km)
            vehiculo.conducir(km)
        except ValueError as e:
            print(e)

    # Mostrar los datos del vehículo y el kilometraje final
    print("\nResumen final del vehículo:")
    print(vehiculo)

if __name__ == "__main__":
    main()