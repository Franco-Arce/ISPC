class Tarea:
    def __init__(self, nombre, completada=False):
        self.nombre = nombre
        self.completada = completada

    def __str__(self):
        estado = "Completada" if self.completada else "Pendiente"
        return f"Tarea: {self.nombre} - Estado: {estado}"
    
    def __len__(self):
        return 1

# Crear algunas tareas
tarea1 = Tarea("Aprender POO")
tarea2 = Tarea("Realizar ejercicios en Python", completada= True)
tarea3 = Tarea("Leer documentación")

# Lista de tareas
lista_tareas = [tarea1, tarea2, tarea3]

for tarea in lista_tareas:
    print(tarea)

# Contar cuántas tareas hay en la lista
total_tareas = sum(len(tarea) for tarea in lista_tareas)
print(f"Total de tareas: {total_tareas}")
