class Libro:
    def __init__(self, titulo, autor, estado='disponible'):
        self.titulo = titulo
        self.autor = autor
        self.estado = estado
    
    def prestar(self):
        if self.estado == 'disponible':
            self.estado = 'prestado'
            return True
        else:
            return False
    
    def devolver(self):
        if self.estado == 'prestado':
            self.estado = 'disponible'
            return True
        else:
            return False
    
    def __str__(self):
        return f"Título: {self.titulo} | Autor: {self.autor} | Estado: {self.estado}"


class Biblioteca:
    def __init__(self):
        self.libros = []
    
    def agregar_libro(self, libro):
        self.libros.append(libro)
    
    def buscar_por_titulo(self, titulo):
        resultados = [libro for libro in self.libros if libro.titulo.lower() == titulo.lower()]
        return resultados
    
    def buscar_por_autor(self, autor):
        resultados = [libro for libro in self.libros if libro.autor.lower() == autor.lower()]
        return resultados
    
    def mostrar_estado_libro(self, titulo):
        for libro in self.libros:
            if libro.titulo.lower() == titulo.lower():
                return libro
        return None
    
    def __str__(self):
        return "\n".join(str(libro) for libro in self.libros)


def main():
    biblioteca = Biblioteca()
    
    # Agregar libros a la biblioteca
    biblioteca.agregar_libro(Libro("Padre Rico, Padre Pobre", "Robert Kiyosaki"))
    biblioteca.agregar_libro(Libro("El Principito", "Antoine de Saint-Exupéry"))
    biblioteca.agregar_libro(Libro("1984", "George Orwell"))
    
    while True:
        print("\nGestión de Biblioteca")
        print("1. Buscar libro por título")
        print("2. Buscar libro por autor")
        print("3. Mostrar estado de un libro")
        print("4. Prestar libro")
        print("5. Devolver libro")
        print("6. Mostrar todos los libros")
        print("7. Salir")
        
        opcion = input("Elija una opción (1-7): ")
        
        if opcion == '1':
            titulo = input("Ingrese el título del libro: ")
            resultados = biblioteca.buscar_por_titulo(titulo)
            if resultados:
                for libro in resultados:
                    print(libro)
            else:
                print("No se encontraron libros con ese título.")
        
        elif opcion == '2':
            autor = input("Ingrese el autor del libro: ")
            resultados = biblioteca.buscar_por_autor(autor)
            if resultados:
                for libro in resultados:
                    print(libro)
            else:
                print("No se encontraron libros de ese autor.")
        
        elif opcion == '3':
            titulo = input("Ingrese el título del libro: ")
            libro = biblioteca.mostrar_estado_libro(titulo)
            if libro:
                print(libro)
            else:
                print("No se encontró el libro.")
        
        elif opcion == '4':
            titulo = input("Ingrese el título del libro a prestar: ")
            libro = biblioteca.mostrar_estado_libro(titulo)
            if libro:
                if libro.prestar():
                    print(f"El libro '{titulo}' ha sido prestado.")
                else:
                    print(f"El libro '{titulo}' ya está prestado.")
            else:
                print("No se encontró el libro.")
        
        elif opcion == '5':
            titulo = input("Ingrese el título del libro a devolver: ")
            libro = biblioteca.mostrar_estado_libro(titulo)
            if libro:
                if libro.devolver():
                    print(f"El libro '{titulo}' ha sido devuelto.")
                else:
                    print(f"El libro '{titulo}' ya está disponible.")
            else:
                print("No se encontró el libro.")
        
        elif opcion == '6':
            print("\n-- Todos los libros en la biblioteca --")
            print(biblioteca)
        
        elif opcion == '7':
            print("Saliendo del programa.")
            break
        
        else:
            print("Opción no válida. Inténtelo de nuevo.")

if __name__ == "__main__":
    main()
