
#CREATE DATABASE PruebasIbaktor2; 
#DROP DATABASE PruebasIbaktor2; 

#Usamos la base creada: 
#USE PruebasIbaktor;
#CREATE TABLE Usuarios (ID INT PRIMARY KEY, Nombre VARCHAR(100), Edad INT); 
INSERT INTO Usuarios (ID, Nombre, Edad) VALUES (1, 'Ana', 28); 

#SELECT Usuarios.Nombre, Pedidos.Fecha 
#FROM Usuarios 
#JOIN Pedidos 
#ON Usuarios.ID = Pedidos.UsuarioID 
#WHERE Usuarios.Edad > 25; 
