class Persona:
    def __init__(self, nombre="", edad=0, dni=""):
        self.__nombre = nombre
        self.__edad = edad
        self.__dni = dni

    # Getters
    @property
    def nombre(self):
        return self.__nombre

    @property
    def edad(self):
        return self.__edad

    @property
    def dni(self):
        return self.__dni

    # Setters con validación
    @nombre.setter
    def nombre(self, nombre):
        if isinstance(nombre, str) and nombre.strip():
            self.__nombre = nombre
        else:
            raise ValueError("Nombre no válido.")

    @edad.setter
    def edad(self, edad):
        if isinstance(edad, int) and 0 <= edad <= 120:
            self.__edad = edad
        else:
            raise ValueError("Edad no válida. Debe ser un número entre 0 y 120.")

    @dni.setter
    def dni(self, dni):
        if isinstance(dni, str) and len(dni) == 9 and dni[:-1].isdigit() and dni[-1].isalpha():
            self.__dni = dni
        else:
            raise ValueError("DNI no válido. Debe tener 8 dígitos seguidos de una letra.")

    # Método para mostrar los datos
    def __str__(self):
        return(f"Nombre: {self.__nombre}\n"
               f"Edad: {self.__edad}\n"
               f"DNI: {self.__dni[:-1]}\n")

    # Método para comprobar si es mayor de edad
    def esMayorDeEdad(self):
        return self.edad >= 18

# APLICACIÓN DE CONSOLA
def main():
    nombre = input("Ingrese el nombre: ")
    edad = int(input("Ingrese la edad: "))
    dni = input("Ingrese el DNI (8 dígitos y luego una letra): ")

    # Crear objeto Persona
    persona = Persona(nombre, edad, dni)

    # Mostrar datos de la persona
    print("\n--DATOS DE LA PERSONA--")
    print(persona)

    # Verificar si es mayor de edad
    if persona.esMayorDeEdad():
        print(f"{persona.nombre} es mayor de edad.")
    else:
        print(f"{persona.nombre} es menor de edad.")

if __name__ == "__main__":
    main()