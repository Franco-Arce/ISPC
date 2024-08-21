class Persona:
    def __init__(self, nombre='', edad=None, DNI=''):
        self.nombre = nombre
        self.edad = edad
        self.DNI = DNI
    
    # Setters
    def set_nombre(self, nombre):
        if isinstance(nombre, str) and nombre:
            self.nombre = nombre
        else:
            raise ValueError("El nombre debe ser una cadena no vacía.")
    
    def set_edad(self, edad):
        if isinstance(edad, int) and edad >= 0:
            self.edad = edad
        else:
            raise ValueError("La edad debe ser un entero positivo.")
    
    def set_DNI(self, DNI):
        if isinstance(DNI, str) and len(DNI) == 8:   
            self.DNI = DNI
        else:
            raise ValueError("El DNI debe ser una cadena de 8 caracteres.")

    def get_nombre(self):
        return self.nombre
    
    def get_edad(self):
        return self.edad
    
    def get_DNI(self):
        return self.DNI
    
    def mostrar(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}, DNI: {self.DNI}"
    
    def es_mayor_de_edad(self):
        return self.edad >= 18

def main():
    print("Creación de Persona")
    nombre = input("Ingrese el nombre: ")
    edad = int(input("Ingrese la edad: "))
    DNI = input("Ingrese el DNI (8 caracteres): ")
    
    persona = Persona()
    
    try:
        persona.set_nombre(nombre)
        persona.set_edad(edad)
        persona.set_DNI(DNI)
        
        print("\nDatos de la persona:")
        print(persona.mostrar())
        
        if persona.es_mayor_de_edad():
            print("La persona es mayor de edad.")
        else:
            print("La persona es menor de edad.")
    
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
