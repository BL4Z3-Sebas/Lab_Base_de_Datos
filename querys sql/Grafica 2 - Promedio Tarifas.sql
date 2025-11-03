--Gráfica 2: Promedio de tarifas durante los años 2021 y 2022
DECLARE @TarifasTotales TABLE(
    viaje DATETIME,
    tarifa FLOAT
);

-- Insertar datos desde cada tabla mensual (2021 y 2022)
INSERT INTO @TarifasTotales (viaje, tarifa)
SELECT lpep_pickup_datetime, fare_amount
FROM dbo.[01/21GreenTrip]
UNION ALL
SELECT lpep_pickup_datetime, fare_amount
FROM dbo.[02/21GreenTrip]
UNION ALL
SELECT lpep_pickup_datetime, fare_amount
FROM dbo.[03/21GreenTrip]
UNION ALL
SELECT lpep_pickup_datetime, fare_amount
FROM dbo.[04/21GreenTrip]
UNION ALL
SELECT lpep_pickup_datetime, fare_amount
FROM dbo.[05/21GreenTrip]
UNION ALL
SELECT lpep_pickup_datetime, fare_amount
FROM dbo.[06/21GreenTrip]
UNION ALL
SELECT lpep_pickup_datetime, fare_amount
FROM dbo.[07/21GreenTrip]
UNION ALL
SELECT lpep_pickup_datetime, fare_amount
FROM dbo.[08/21GreenTrip]
UNION ALL
SELECT lpep_pickup_datetime, fare_amount
FROM dbo.[09/21GreenTrip]
UNION ALL
SELECT lpep_pickup_datetime, fare_amount
FROM dbo.[10/21GreenTrip]
UNION ALL
SELECT lpep_pickup_datetime, fare_amount
FROM dbo.[11/21GreenTrip]
UNION ALL
SELECT lpep_pickup_datetime, fare_amount
FROM dbo.[12/21GreenTrip]
UNION ALL
SELECT lpep_pickup_datetime, fare_amount
FROM dbo.[01/22GreenTrip]
UNION ALL
SELECT lpep_pickup_datetime, fare_amount
FROM dbo.[02/22GreenTrip]
UNION ALL
SELECT lpep_pickup_datetime, fare_amount
FROM dbo.[03/22GreenTrip]
UNION ALL
SELECT lpep_pickup_datetime, fare_amount
FROM dbo.[04/22GreenTrip]
UNION ALL
SELECT lpep_pickup_datetime, fare_amount
FROM dbo.[05/22GreenTrip]
UNION ALL
SELECT lpep_pickup_datetime, fare_amount
FROM dbo.[06/22GreenTrip]
UNION ALL
SELECT lpep_pickup_datetime, fare_amount
FROM dbo.[07/22GreenTrip]
UNION ALL
SELECT lpep_pickup_datetime, fare_amount
FROM dbo.[08/22GreenTrip]
UNION ALL
SELECT lpep_pickup_datetime, fare_amount
FROM dbo.[09/22GreenTrip]
UNION ALL
SELECT lpep_pickup_datetime, fare_amount
FROM dbo.[10/22GreenTrip]
UNION ALL
SELECT lpep_pickup_datetime, fare_amount
FROM dbo.[11/22GreenTrip]
UNION ALL
SELECT lpep_pickup_datetime, fare_amount
FROM dbo.[12/22GreenTrip];

-- calcular promedio de tarifa por mes y año
SELECT 
    YEAR(viaje) AS Año,
    MONTH(viaje) AS Mes,
    AVG(tarifa) AS Promedio_Tarifa
FROM @TarifasTotales tt
WHERE tt.viaje >= '2021-01-01' AND tt.viaje < '2023-01-01'
GROUP BY YEAR(viaje), MONTH(viaje)
ORDER BY Año, Mes;