class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.estaPrestado = False

    def prestar(self):
        if not self.estaPrestado:
            self.estaPrestado = True
            print(f'El libro "{self.titulo}" ha sido prestado.')
        else:
            print(f'El libro "{self.titulo}" ya está prestado.')

    def devolver(self):
        if self.estaPrestado:
            self.estaPrestado = False
            print(f'El libro "{self.titulo}" ha sido devuelto.')
        else:
            print(f'El libro "{self.titulo}" ya estaba disponible.')

    def __str__(self):
        estado = "Prestado" if self.estaPrestado else "Disponible"
        return f'Título: {self.titulo}, Autor: {self.autor}, Estado: {estado}'

class Biblioteca:
    def __init__(self):
        self.libros = []

    def agregarLibro(self, libro):
        self.libros.append(libro)
        print(f'El libro "{libro.titulo}" ha sido agregado a la biblioteca.')

    def buscarPorTitulo(self, titulo):
        for libro in self.libros:
            if libro.titulo.lower() == titulo.lower():
                return libro
        return None

    def buscarPorAutor(self, autor):
        resultados = []
        for libro in self.libros:
            if libro.autor.lower() == autor.lower():
                resultados.append(libro)
        return resultados

    def buscar(self, criterio):
        resultados = []
        for libro in self.libros:
            if criterio.lower() in libro.titulo.lower() or criterio.lower() in libro.autor.lower():
                resultados.append(libro)
        return resultados

    def mostrarEstadoLibro(self, titulo):
        libro = self.buscarPorTitulo(titulo)
        if libro:
            print(libro)
        else:
            print(f'No se encontró un libro con el título "{titulo}".')

    def menu(self):
        while True:
            print("\n---MENÚ--")
            print("1. Buscar libro por título")
            print("2. Buscar libro por autor")
            print("3. Prestar libro")
            print("4. Devolver libro")
            print("5. Salir")
            opcion = input("Selecciona una opción: ")

            if opcion == '1':
                titulo = input("\nIntroduce el título del libro: ")
                libro = self.buscarPorTitulo(titulo)
                if libro:
                    print(libro)
                else:
                    print(f'No se encontró un libro con el título "{titulo}".')

            elif opcion == '2':
                autor = input("\nIntroduce el autor del libro: ")
                resultados = self.buscarPorAutor(autor)
                if resultados:
                    for libro in resultados:
                        print(libro)
                else:
                    print(f'No se encontraron libros por el autor "{autor}".')

            elif opcion == '3':
                titulo = input("\nIntroduce el título del libro a prestar: ")
                libro = self.buscarPorTitulo(titulo)
                if libro:
                    libro.prestar()
                else:
                    print(f'No se encontró un libro con el título "{titulo}".')

            elif opcion == '4':
                titulo = input("\nIntroduce el título del libro a devolver: ")
                libro = self.buscarPorTitulo(titulo)
                if libro:
                    libro.devolver()
                else:
                    print(f'No se encontró un libro con el título "{titulo}".')

            elif opcion == '5':
                print("Saliendo del programa.")
                break

            else:
                print("Opción no válida. Por favor, selecciona una opción del 1 al 5.")

biblioteca = Biblioteca()

libro1 = Libro("Cien años de soledad", "Gabriel García Márquez")
libro2 = Libro("El amor en los tiempos del cólera", "Gabriel García Márquez")
libro3 = Libro("Don Quijote de la Mancha", "Miguel de Cervantes")

biblioteca.agregarLibro(libro1)
biblioteca.agregarLibro(libro2)
biblioteca.agregarLibro(libro3)

biblioteca.menu()