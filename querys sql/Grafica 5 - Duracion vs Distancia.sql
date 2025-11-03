-- Gráfica 5: Duración vs Distancia
WITH durvsdis AS (
    SELECT lpep_pickup_datetime AS salida,
           lpep_dropoff_datetime AS llegada,
           trip_distance AS distancia
    FROM dbo.[01/21GreenTrip]
    UNION ALL
    SELECT lpep_pickup_datetime, lpep_dropoff_datetime, trip_distance
    FROM dbo.[02/21GreenTrip]
    UNION ALL
    SELECT lpep_pickup_datetime, lpep_dropoff_datetime, trip_distance
    FROM dbo.[03/21GreenTrip]
    UNION ALL
    SELECT lpep_pickup_datetime, lpep_dropoff_datetime, trip_distance
    FROM dbo.[04/21GreenTrip]
    UNION ALL
    SELECT lpep_pickup_datetime, lpep_dropoff_datetime, trip_distance
    FROM dbo.[05/21GreenTrip]
    UNION ALL
    SELECT lpep_pickup_datetime, lpep_dropoff_datetime, trip_distance
    FROM dbo.[06/21GreenTrip]
    UNION ALL
    SELECT lpep_pickup_datetime, lpep_dropoff_datetime, trip_distance
    FROM dbo.[07/21GreenTrip]
    UNION ALL
    SELECT lpep_pickup_datetime, lpep_dropoff_datetime, trip_distance
    FROM dbo.[08/21GreenTrip]
    UNION ALL
    SELECT lpep_pickup_datetime, lpep_dropoff_datetime, trip_distance
    FROM dbo.[09/21GreenTrip]
    UNION ALL
    SELECT lpep_pickup_datetime, lpep_dropoff_datetime, trip_distance
    FROM dbo.[10/21GreenTrip]
    UNION ALL
    SELECT lpep_pickup_datetime, lpep_dropoff_datetime, trip_distance
    FROM dbo.[11/21GreenTrip]
    UNION ALL
    SELECT lpep_pickup_datetime, lpep_dropoff_datetime, trip_distance
    FROM dbo.[12/21GreenTrip]
    UNION ALL
    SELECT lpep_pickup_datetime, lpep_dropoff_datetime, trip_distance
    FROM dbo.[01/22GreenTrip]
    UNION ALL
    SELECT lpep_pickup_datetime, lpep_dropoff_datetime, trip_distance
    FROM dbo.[02/22GreenTrip]
    UNION ALL
    SELECT lpep_pickup_datetime, lpep_dropoff_datetime, trip_distance
    FROM dbo.[03/22GreenTrip]
    UNION ALL
    SELECT lpep_pickup_datetime, lpep_dropoff_datetime, trip_distance
    FROM dbo.[04/22GreenTrip]
    UNION ALL
    SELECT lpep_pickup_datetime, lpep_dropoff_datetime, trip_distance
    FROM dbo.[05/22GreenTrip]
    UNION ALL
    SELECT lpep_pickup_datetime, lpep_dropoff_datetime, trip_distance
    FROM dbo.[06/22GreenTrip]
    UNION ALL
    SELECT lpep_pickup_datetime, lpep_dropoff_datetime, trip_distance
    FROM dbo.[07/22GreenTrip]
    UNION ALL
    SELECT lpep_pickup_datetime, lpep_dropoff_datetime, trip_distance
    FROM dbo.[08/22GreenTrip]
    UNION ALL
    SELECT lpep_pickup_datetime, lpep_dropoff_datetime, trip_distance
    FROM dbo.[09/22GreenTrip]
    UNION ALL
    SELECT lpep_pickup_datetime, lpep_dropoff_datetime, trip_distance
    FROM dbo.[10/22GreenTrip]
    UNION ALL
    SELECT lpep_pickup_datetime, lpep_dropoff_datetime, trip_distance
    FROM dbo.[11/22GreenTrip]
    UNION ALL
    SELECT lpep_pickup_datetime, lpep_dropoff_datetime, trip_distance
    FROM dbo.[12/22GreenTrip]
)
SELECT 
    CAST(salida AS date) AS Fecha,
    ROUND(AVG(DATEDIFF(MINUTE, salida, llegada)), 2) AS DuracionPromedio_Minutos,
    ROUND(AVG(distancia), 2) AS DistanciaPromedio
FROM durvsdis dd
WHERE dd.distancia > 0 AND salida >= '2021-01-01' AND salida < '2023-01-01'
GROUP BY CAST(salida AS date) 
ORDER BY Fecha;