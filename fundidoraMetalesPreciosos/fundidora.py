# fundidora.py

class Fundidora:
    # Metales soportados por la Fundidora, instanciando la temperatura necesaria por metal
    METAL_TEMPERATURAS = {
        'oro': 1064,
        'plata': 961,
        'platino': 1768,
        'paladio': 1555,
    }

    def __init__(self, capacidad, temperatura_maxima):
        self.capacidad = capacidad  # Capacidad máxima de la fundidora en gramos
        self.temperatura_maxima = temperatura_maxima  # Temperatura máxima que puede alcanzar la fundidora
        self.temperatura_actual = 0  # Temperatura actual de la fundidora
        self.material_fundido = 0  # Cantidad de material fundido
        self.tipo_metal = None  # Tipo de metal a fundir
        self.temperatura_necesaria = 0  # Temperatura necesaria para fundir el metal seleccionado

    def seleccionar_metal(self, tipo_metal):
        """Selecciona el tipo de metal y ajusta la temperatura necesaria."""
        if tipo_metal.lower() not in self.METAL_TEMPERATURAS:
            raise ValueError(f"El metal '{tipo_metal}' no es soportado.")
        self.tipo_metal = tipo_metal.lower()
        self.temperatura_necesaria = self.METAL_TEMPERATURAS[self.tipo_metal]
        print(f"Metal seleccionado: {self.tipo_metal.capitalize()}, temperatura necesaria: {self.temperatura_necesaria}°C")

    def calentar(self):
        """Calienta la fundidora a la temperatura necesaria para el metal seleccionado."""
        if self.temperatura_necesaria > self.temperatura_maxima:
            raise ValueError(f"La temperatura necesaria ({self.temperatura_necesaria}°C) excede la capacidad máxima de la fundidora.")
        self.temperatura_actual = self.temperatura_necesaria
        print(f"Fundidora calentada a {self.temperatura_actual}°C para fundir {self.tipo_metal}.")

    def fundir_material(self, cantidad):
        """Funde una cantidad de material, siempre que no exceda la capacidad de la fundidora."""
        if cantidad > self.capacidad:
            raise ValueError("La cantidad de material excede la capacidad de la fundidora.")
        if self.temperatura_actual < self.temperatura_necesaria:
            raise ValueError(f"La temperatura actual ({self.temperatura_actual}°C) no es suficiente para fundir {self.tipo_metal}.")
        self.material_fundido += cantidad
        print(f"Se han fundido {cantidad} gramos de {self.tipo_metal}.")

    def verificar_pureza(self):
        """Calcula la pureza del material fundido basado en la temperatura actual."""
        if self.temperatura_actual >= 1000:
            return 99.9
        else:
            return 90.0

    def __str__(self):
        """Devuelve una cadena que describe el estado actual de la fundidora."""
        return (f"Fundidora con capacidad de {self.capacidad}g, "
                f"temperatura actual de {self.temperatura_actual}°C, "
                f"material fundido {self.material_fundido}g.")

if __name__ == "__main__":
    # Código que se ejecuta cuando se corre fundidora.py directamente
    mi_fundidora = Fundidora(capacidad=5000, temperatura_maxima=1800)

    tipo_metal = input("Ingrese el tipo de metal a fundir (oro, plata, platino, paladio): ").strip().lower()
    try:
        mi_fundidora.seleccionar_metal(tipo_metal)
        mi_fundidora.calentar()

        cantidad = float(input(f"Ingrese la cantidad de {tipo_metal} a fundir (en gramos): "))
        mi_fundidora.fundir_material(cantidad)

        pureza = mi_fundidora.verificar_pureza()
        print(f"La pureza del material fundido es: {pureza}%")

        print(mi_fundidora)

    except ValueError as e:
        print(e)