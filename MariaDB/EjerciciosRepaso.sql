# Fechas de venta del producto A
SELECT fecha
FROM ventas
WHERE ventas.producto = 'ProductoA';

# Fechas de venta del producto A
SELECT fecha
FROM ventas
WHERE producto = 'ProductoA';

#Total de ventas de los productos B sin considerar la cantidad
SELECT SUM(precio) AS SUM_Precio
FROM ventas
WHERE producto = 'ProductoB';

#Total de ventas de los productos B
SELECT SUM(precio*cantidad) AS SUM_Precio
FROM ventas
WHERE producto = 'ProductoB';

# Venta promedio de los productos
SELECT producto, AVG(precio*cantidad) AS Precio_Promedio
FROM ventas
GROUP BY producto;

# Venta promedio de los productos con más de 100 pesos en promedio
SELECT producto, AVG(precio*cantidad) AS Precio_Promedio
FROM ventas
GROUP BY producto;

# Venta promedio de los productos con más de 100 pesos en promedio
SELECT producto, AVG(precio*cantidad) AS Precio_Promedio
FROM ventas
GROUP BY producto
HAVING Precio_Promedio > 100;

#Queremos los tres productos que más ganancias dan
SELECT producto, SUM(precio*cantidad) AS Venta_Total
FROM ventas
GROUP BY producto;

SELECT producto, SUM(precio*cantidad) AS Venta_Total
FROM ventas
GROUP BY producto
ORDER BY Venta_Total DESC;

SELECT producto, SUM(precio*cantidad) AS Venta_Total
FROM ventas
GROUP BY producto
ORDER BY Venta_Total DESC
LIMIT 3;


SELECT producto
FROM (
	SELECT producto, SUM(precio*cantidad) AS Venta_Total
	FROM ventas
	GROUP BY producto
	ORDER BY Venta_Total DESC
	LIMIT 3
) AS TOP_3 ;

#Podemos tener la subconsulta en un CTE (Common Table Expression)

WITH TOP_3 AS( 
SELECT producto, SUM(precio*cantidad) AS Venta_Total
FROM ventas
GROUP BY producto
ORDER BY Venta_Total DESC
LIMIT 3)

SELECT producto
FROM TOP_3;















