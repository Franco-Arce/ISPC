
---

# Actividad Individual: Diseño y Desarrollo de Objetos
![Fundidora de Metales preciosos](https://github.com/user-attachments/assets/c3106541-74c3-4343-acd1-dfe4c63ef992)

## Objetivo

Diseñar 
y desarrollar una clase en Python que represente una fundidora de metales, aplicando TDD (Desarrollo Guiado por Pruebas), conceptos de Programación Orientada a Objetos (POO) y diseñando la base de datos correspondiente.

## Descripción del Código

La clase `Fundidora` simula una fundidora de metales con los siguientes comportamientos clave:

1. **Seleccionar Metal**: Permite seleccionar el tipo de metal y ajusta la temperatura necesaria para fundirlo.
2. **Calentar**: Calienta la fundidora a la temperatura requerida para el metal seleccionado.
3. **Fundir Material**: Funde una cantidad específica de material sin exceder la capacidad de la fundidora y solo si la temperatura es la adecuada.

Método estándar implementado:
- **`__str__`**: Devuelve una representación en cadena del estado actual de la fundidora.

### Principios Aplicados

- **Abstracción**: La clase `Fundidora` abstrae los detalles internos de su funcionamiento, proporcionando métodos claros para la interacción del usuario.
- **Encapsulamiento**: Los datos y métodos relevantes están encapsulados dentro de la clase, y los atributos se protegen adecuadamente mediante validaciones.

## Desarrollo Guiado por Pruebas (TDD)

1. **Pruebas Unitarias**: Las pruebas se escribieron primero en el archivo `test_fundidora.py`.
2. **Implementación de la Clase**: La clase `Fundidora` en `fundidora.py` se desarrolló para pasar las pruebas.
3. **Refactorización**: El código se refactorizó según fuera necesario para cumplir con los requisitos de las pruebas.

## Base de Datos

- **Diseño**: Incluye la sentencia `CREATE TABLE` para la fundidora.
- **Datos de Ejemplo**: Incluye 10 sentencias `INSERT` con datos de prueba.
- **Consultas**: Contiene 5 consultas `SELECT` para extraer información.

**Archivo SQL**: `sqlFile.sql`

## Instalación y Ejecución

1. **Ejecutar el Código Principal**:
   ```bash
   python fundidora.py
   ```

2. **Ejecutar las Pruebas Unitarias**:
   ```bash
   python -m unittest test_fundidora
   ```

## Video de Presentación

Para una demostración del funcionamiento del programa y una breve explicación sobre la aplicación de los principios de POO y TDD, adjunto link al siguiente video en YouTube:

[Ver Video de Presentación](https://youtu.be/BADQmpgejzo)


## Archivos Incluidos

- **`fundidora.py`**: Implementación de la clase `Fundidora`.
- **`test_fundidora.py`**: Pruebas unitarias para la clase `Fundidora`.
- **`sqlFile.sql`**: Script SQL con el diseño de la base de datos y datos de ejemplo.
- **`Evidencia4.mp4`**: Video de presentación del proyecto.

---
