class Estudiante:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad
        self.__asignaturas = {}

    def agregarAsignatura(self, asignatura, calificacion):
        self.__asignaturas[asignatura] = calificacion

    def calcularPromedio(self):
        if not self.__asignaturas:
            return 0.0
        total = sum(self.__asignaturas.values())
        return total / len(self.__asignaturas)

    def __str__(self):
        asignaturasStr = ", ".join([f"{asignatura}: {calificacion}" for asignatura, calificacion in self.__asignaturas.items()])
        return (f"Nombre: {self.__nombre} | Edad: {self.__edad} | "
                f"Asignaturas: {asignaturasStr} | Promedio: {self.calcularPromedio():.2f}")

class RegistroEstudiantes:
    def __init__(self):
        self.estudiantes = []

    def agregarEstudiante(self):
        nombre = input("Ingrese el nombre del estudiante: ")
        edad = int(input("Ingrese la edad del estudiante: "))
        estudiante = Estudiante(nombre, edad)
        self.estudiantes.append(estudiante)
        print(f"Estudiante '{nombre}' agregado correctamente.\n")

    def agregarAsignaturaAEstudiante(self):
        nombre = input("Ingrese el nombre del estudiante: ")
        estudiante = next((e for e in self.estudiantes if e.nombre == nombre), None)
        if estudiante:
            asignatura = input("Ingrese el nombre de la asignatura: ")
            calificacion = float(input("Ingrese la calificación de la asignatura: "))
            estudiante.agregarAsignatura(asignatura, calificacion)
            print(f"Asignatura '{asignatura}' con calificación {calificacion} agregada a {nombre}.\n")
        else:
            print(f"Estudiante '{nombre}' no encontrado.\n")

    def mostrarEstudiantes(self):
        if not self.estudiantes:
            print("No hay estudiantes registrados.\n")
        else:
            print("Estudiantes registrados:")
            for estudiante in self.estudiantes:
                print(estudiante)
            print()

def menu():
    registro = RegistroEstudiantes()
    
    while True:
        print("--MENÚ--")
        print("1. Agregar estudiante")
        print("2. Agregar asignatura a estudiante")
        print("3. Mostrar estudiantes")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            registro.agregarEstudiante()
        elif opcion == '2':
            registro.agregarAsignaturaAEstudiante()
        elif opcion == '3':
            registro.mostrarEstudiantes()
        elif opcion == '4':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Intente nuevamente.\n")

if __name__ == "__main__":
    menu()