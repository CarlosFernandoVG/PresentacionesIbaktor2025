CREATE TABLE ventas (
    fecha DATE,
    producto VARCHAR(100),
    cantidad INT,
    precio DECIMAL(10,2)
);

LOAD DATA INFILE '/Users/carlosvasquezguerra/Documents/Ibaktor Bootcamp/MATERIALES DANL M4/MariaDB/ventas.csv'
INTO TABLE ventas
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"' 
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(fecha, producto, cantidad, precio);

CREATE USER 'python_user'@'localhost' IDENTIFIED BY '';
GRANT ALL PRIVILEGES ON nombre_db.* TO 'python_user'@'localhost';
FLUSH PRIVILEGES;


#SELECT 
#    producto,
#    TIMESTAMPDIFF(DAY, MIN(fecha), MAX(fecha)) as dias_en_venta,
#    WEEK(fecha, 3) as semana_del_anio,
#    SUM(cantidad) as unidades_vendidas
#    FROM ventas
#GROUP BY producto, WEEK(fecha, 3);