USE fundidora;
CREATE TABLE Fundiciones (
    id SERIAL PRIMARY KEY,
    temperatura_actual DECIMAL(5,2),
    capacidad DECIMAL(10,2),
    material_fundido DECIMAL(10,2),
    pureza DECIMAL(5,2)
);
-- Modificamos la tabla para permitir ingresar mayor cantidad de digitos en la temperatura actual
ALTER TABLE Fundiciones
MODIFY COLUMN temperatura_actual DECIMAL(7,2);

-- Creamos 10 sentencias INSERT con datos de ejemplo
INSERT INTO Fundiciones (temperatura_actual, capacidad, material_fundido, pureza) VALUES (1200.00, 5000.00, 3000.00, 99.9);
INSERT INTO Fundiciones (temperatura_actual, capacidad, material_fundido, pureza) VALUES (1400.00, 4500.00, 2000.00, 99.5);
INSERT INTO Fundiciones (temperatura_actual, capacidad, material_fundido, pureza) VALUES (1600.00, 4800.00, 2800.00, 98.7);
INSERT INTO Fundiciones (temperatura_actual, capacidad, material_fundido, pureza) VALUES (1768.00, 4000.00, 3500.00, 99.8);
INSERT INTO Fundiciones (temperatura_actual, capacidad, material_fundido, pureza) VALUES (961.00, 6000.00, 3000.00, 99.9);
INSERT INTO Fundiciones (temperatura_actual, capacidad, material_fundido, pureza) VALUES (1064.00, 5200.00, 3100.00, 99.7);
INSERT INTO Fundiciones (temperatura_actual, capacidad, material_fundido, pureza) VALUES (1200.00, 5300.00, 3300.00, 99.6);
INSERT INTO Fundiciones (temperatura_actual, capacidad, material_fundido, pureza) VALUES (1500.00, 4900.00, 3200.00, 99.4);
INSERT INTO Fundiciones (temperatura_actual, capacidad, material_fundido, pureza) VALUES (1555.00, 4700.00, 3400.00, 99.8);
INSERT INTO Fundiciones (temperatura_actual, capacidad, material_fundido, pureza) VALUES (1900.00, 5100.00, 2900.00, 99.2);

-- Creamos 5 consultas de tipo SELECT
SELECT * FROM Fundiciones WHERE pureza > 95;
SELECT COUNT(*) FROM Fundiciones WHERE capacidad > 1000;
SELECT AVG(temperatura_actual) AS temp_promedio FROM Fundiciones;
SELECT SUM(material_fundido) AS total_material_fundido FROM Fundiciones;
SELECT * FROM Fundiciones ORDER BY capacidad DESC LIMIT 1;
