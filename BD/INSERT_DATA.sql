-- CREATE DATABASE ESTUDIANTEDB

-- Crear la tabla ESTUDIANTE
CREATE TABLE ESTUDIANTE (
    id INT PRIMARY KEY IDENTITY(1, 1),
    nombre VARCHAR(255),
    apellido VARCHAR(255),
    cedula VARCHAR(12),
    estatura FLOAT,
    peso FLOAT,
    fecha_nacimiento DATE,
    edad INT
);

-- Insertar datos en la tabla ESTUDIANTE
INSERT INTO ESTUDIANTE (nombre, apellido, cedula, estatura, peso, fecha_nacimiento,edad)
VALUES ('Kienan', 'Sutlieff', 
        CONCAT('09', RIGHT(CONVERT(VARCHAR, RAND()*1000000000), 10)), 
        1.0, 92, '2000-09-26',
        DATEDIFF(YEAR, '2000-09-26', GETDATE()));

INSERT INTO ESTUDIANTE (nombre, apellido, cedula, estatura, peso, fecha_nacimiento)
VALUES (
    'Sigismondo', 'Agronski',
    CONCAT('09', RIGHT(CONVERT(VARCHAR, RAND()*1000000000), 10)),
    1.2, 80, '2000-04-20'
);

INSERT INTO ESTUDIANTE (nombre, apellido, cedula, estatura, peso, fecha_nacimiento)
VALUES (
    'Libbi', 'Morad',
    CONCAT('09', RIGHT(CONVERT(VARCHAR, RAND()*1000000000), 10)),
    1.8, 62, '2000-01-29'
);

INSERT INTO ESTUDIANTE (nombre, apellido, cedula, estatura, peso, fecha_nacimiento, edad)
VALUES (
    'Libbi', 'Morad',
    CONCAT('09', RIGHT(CONVERT(VARCHAR, RAND()*1000000000), 10)),
    1.8, 62, '2000-01-29',
    DATEDIFF(YEAR, '2000-01-29', GETDATE())
);

INSERT INTO ESTUDIANTE (nombre, apellido, cedula, estatura, peso, fecha_nacimiento, edad)
VALUES (
    'Nancey', 'Jump',
    CONCAT('09', RIGHT(CONVERT(VARCHAR, RAND()*1000000000), 10)),
    1.1, 70, '2000-06-10',
    DATEDIFF(YEAR, '2000-06-10', GETDATE())
);

INSERT INTO ESTUDIANTE (nombre, apellido, cedula, estatura, peso, fecha_nacimiento, edad)
VALUES (
    'Nina', 'March',
    CONCAT('09', RIGHT(CONVERT(VARCHAR, RAND()*1000000000), 10)),
    1.3, 86, '2000-01-21',
    DATEDIFF(YEAR, '2000-01-21', GETDATE())
);


INSERT INTO ESTUDIANTE (nombre, apellido, cedula, estatura, peso, fecha_nacimiento, edad)
VALUES (
    'Nolie', 'Soro',
    CONCAT('09', RIGHT(CONVERT(VARCHAR, RAND()*1000000000), 10)),
    1.2, 86, '2000-12-08',
    DATEDIFF(YEAR, '2000-12-08', GETDATE())
);

INSERT INTO ESTUDIANTE (nombre, apellido, cedula, estatura, peso, fecha_nacimiento, edad)
VALUES (
    'Lynn', 'Kinnoch',
    CONCAT('09', RIGHT(CONVERT(VARCHAR, RAND()*1000000000), 10)),
    1.5, 75, '2000-02-04',
    DATEDIFF(YEAR, '2000-02-04', GETDATE())
);

INSERT INTO ESTUDIANTE (nombre, apellido, cedula, estatura, peso, fecha_nacimiento, edad)
VALUES (
    'Stefania', 'Everex',
    CONCAT('09', RIGHT(CONVERT(VARCHAR, RAND()*1000000000), 10)),
    1.2, 61, '2000-08-14',
    DATEDIFF(YEAR, '2000-08-14', GETDATE())
);

INSERT INTO ESTUDIANTE (nombre, apellido, cedula, estatura, peso, fecha_nacimiento, edad)
VALUES (
    'Rockwell', 'Cantua',
    CONCAT('09', RIGHT(CONVERT(VARCHAR, RAND()*1000000000), 10)),
    1.4, 86, '2000-10-29',
    DATEDIFF(YEAR, '2000-10-29', GETDATE())
);

INSERT INTO ESTUDIANTE (nombre, apellido, cedula, estatura, peso, fecha_nacimiento, edad)
VALUES (
    'Cinda', 'Dyshart',
    CONCAT('09', RIGHT(CONVERT(VARCHAR, RAND()*1000000000), 10)),
    2.0, 69, '2000-06-04',
    DATEDIFF(YEAR, '2000-06-04', GETDATE())
);

INSERT INTO ESTUDIANTE (nombre, apellido, cedula, estatura, peso, fecha_nacimiento, edad)
VALUES (
    'Venita', 'Kulis',
    CONCAT('09', RIGHT(CONVERT(VARCHAR, RAND()*1000000000), 10)),
    1.2, 81, '2000-01-17',
    DATEDIFF(YEAR, '2000-01-17', GETDATE())
);

INSERT INTO ESTUDIANTE (nombre, apellido, cedula, estatura, peso, fecha_nacimiento, edad)
VALUES (
    'Riannon', 'Roskrug',
    CONCAT('09', RIGHT(CONVERT(VARCHAR, RAND()*1000000000), 10)),
    1.9, 88, '2000-02-21',
    DATEDIFF(YEAR, '2000-02-21', GETDATE())
);

INSERT INTO ESTUDIANTE (nombre, apellido, cedula, estatura, peso, fecha_nacimiento, edad)
VALUES (
    'Luther', 'Joddins',
    CONCAT('09', RIGHT(CONVERT(VARCHAR, RAND()*1000000000), 10)),
    1.4, 90, '2000-01-30',
    DATEDIFF(YEAR, '2000-01-30', GETDATE())
);

INSERT INTO ESTUDIANTE (nombre, apellido, cedula, estatura, peso, fecha_nacimiento, edad)
VALUES (
    'Lionel', 'Boundy',
    CONCAT('09', RIGHT(CONVERT(VARCHAR, RAND()*1000000000), 10)),
    1.9, 91, '2000-10-02',
    DATEDIFF(YEAR, '2000-10-02', GETDATE())
);

INSERT INTO ESTUDIANTE (nombre, apellido, cedula, estatura, peso, fecha_nacimiento, edad)
VALUES (
    'Jaine', 'Springall',
    CONCAT('09', RIGHT(CONVERT(VARCHAR, RAND()*1000000000), 10)),
    1.8, 87, '2000-01-14',
    DATEDIFF(YEAR, '2000-01-14', GETDATE())
);

INSERT INTO ESTUDIANTE (nombre, apellido, cedula, estatura, peso, fecha_nacimiento, edad)
VALUES (
    'Raffarty', 'Bilsland',
    CONCAT('09', RIGHT(CONVERT(VARCHAR, RAND()*1000000000), 10)),
    1.6, 62, '2000-08-28',
    DATEDIFF(YEAR, '2000-08-28', GETDATE())
);

INSERT INTO ESTUDIANTE (nombre, apellido, cedula, estatura, peso, fecha_nacimiento, edad)
VALUES (
    'Ardelis', 'Wasteney',
    CONCAT('09', RIGHT(CONVERT(VARCHAR, RAND()*1000000000), 10)),
    1.7, 87, '2000-01-15',
    DATEDIFF(YEAR, '2000-01-15', GETDATE())
);

INSERT INTO ESTUDIANTE (nombre, apellido, cedula, estatura, peso, fecha_nacimiento, edad)
VALUES (
    'Danell', 'Rosenschein',
    CONCAT('09', RIGHT(CONVERT(VARCHAR, RAND()*1000000000), 10)),
    1.0, 85, '2000-12-26',
    DATEDIFF(YEAR, '2000-12-26', GETDATE())
);

INSERT INTO ESTUDIANTE (nombre, apellido, cedula, estatura, peso, fecha_nacimiento, edad)
VALUES (
    'Conway', 'Courtman',
    CONCAT('09', RIGHT(CONVERT(VARCHAR, RAND()*1000000000), 10)),
    1.8, 74, '2000-03-30',
    DATEDIFF(YEAR, '2000-03-30', GETDATE())
);


