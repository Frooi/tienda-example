create database tienda;

USE tienda;

CREATE TABLE productos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    descripcion VARCHAR(255),
    precio DECIMAL(10, 2) NOT NULL,
    imagen VARCHAR(255) NULL,
    categoria VARCHAR(100) NOT NULL DEFAULT 'General'
);

CREATE TABLE facturas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    producto_id INT NOT NULL,
    cantidad INT NOT NULL,
    total DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (producto_id) REFERENCES productos(id)
);