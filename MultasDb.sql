use MultasDB;


CREATE TABLE Usuarios (
    Id INT IDENTITY PRIMARY KEY,
    Cedula VARCHAR(20) UNIQUE NOT NULL,
    Nombre NVARCHAR(100) NOT NULL,
    Clave NVARCHAR(50) NOT NULL,
    Rol NVARCHAR(20) NOT NULL, -- Ej: Agente, OficinaCentral, Administrador
    Activo BIT DEFAULT 1
);

-- Insertar un agente en la tabla Usuarios
INSERT INTO Usuarios (Cedula, Nombre, Clave, Rol, Activo)
VALUES ('123456789', 'Juan Pérez', 'claveSecreta1', 'Agente', 1);

-- Insertar una persona con rol OficinaCentral en la tabla Usuarios
INSERT INTO Usuarios (Cedula, Nombre, Clave, Rol, Activo)
VALUES ('987654321', 'María López', 'claveSecreta2', 'OficinaCentral', 1);


select *from Usuarios


CREATE TABLE Multas (
    Id INT IDENTITY PRIMARY KEY,
    CedulaCiudadano VARCHAR(20) NOT NULL,
    NombreCiudadano NVARCHAR(100) NOT NULL,
    ConceptoId INT NOT NULL,
    Descripcion NVARCHAR(500),
    Latitud DECIMAL(9, 6),  -- Ej: 19.432608
    Longitud DECIMAL(9, 6), -- Ej: -99.133209
    Foto VARBINARY(MAX),
    FechaRegistro DATETIME DEFAULT GETDATE(),
    Estado NVARCHAR(20) DEFAULT 'Activa', -- Activa, Perdona, Pagada
    AgenteId INT NOT NULL -- Identificador del agente que registró la multa
);
ALTER TABLE Multas
ALTER COLUMN Foto VARBINARY(MAX) NULL;


select *from Multas

CREATE TABLE ConceptosMultas (
    Id INT IDENTITY PRIMARY KEY,
    Nombre NVARCHAR(100) NOT NULL,
    Descripcion NVARCHAR(250) NULL
);

INSERT INTO ConceptosMultas (Nombre, Descripcion)
VALUES
    ('Exceso de velocidad', 'Multa por superar el límite de velocidad permitido en la vía.'),
    ('Estacionamiento indebido', 'Multa por estacionarse en un lugar no permitido.'),
    ('No uso de casco', 'Multa por no utilizar el casco en vehículos de dos ruedas.');

select *from ConceptosMultas


CREATE TABLE Comisiones (
    Id INT IDENTITY PRIMARY KEY,
    AgenteId INT NOT NULL,   -- Identificador del agente que recibe la comisión
    MultaId INT NOT NULL,    -- Identificador de la multa que generó la comisión
    Monto DECIMAL(10, 2) NOT NULL, -- Monto de la comisión (10% de la multa)
    Mes INT NOT NULL,        -- Mes en el que se generó la comisión
    Año INT NOT NULL         -- Año en el que se generó la comisión
);

INSERT INTO Comisiones (AgenteId, MultaId, Monto, Mes, Año) VALUES
(2, 7, 500 * 0.10, 11, 2024), 
(2, 8, 750 * 0.10, 11, 2024), 
(2, 9, 1000 * 0.10, 11, 2024); 

select *from Comisiones


CREATE TABLE ReportesIngreso (
    Id INT PRIMARY KEY IDENTITY,
    Mes INT,
    Año INT,
    Total DECIMAL(10, 2),
    TipoMulta NVARCHAR(50),
    Cantidad INT
);

select *from ReportesIngreso