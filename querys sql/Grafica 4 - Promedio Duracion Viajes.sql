--Grafica 4: Promedio mensual de duracion de viaje por los años 2021 a 2022
SELECT 
        YEAR(lpep_pickup_datetime) AS Año,
        MONTH(lpep_pickup_datetime) AS Mes,
        AVG(DATEDIFF(MINUTE, lpep_pickup_datetime, lpep_dropoff_datetime)) AS DuracionPromedio
    FROM (
        SELECT lpep_pickup_datetime, lpep_dropoff_datetime FROM dbo.[01/21GreenTrip]
        UNION ALL SELECT lpep_pickup_datetime, lpep_dropoff_datetime FROM dbo.[02/21GreenTrip]
        UNION ALL SELECT lpep_pickup_datetime, lpep_dropoff_datetime FROM dbo.[03/21GreenTrip]
        UNION ALL SELECT lpep_pickup_datetime, lpep_dropoff_datetime FROM dbo.[04/21GreenTrip]
        UNION ALL SELECT lpep_pickup_datetime, lpep_dropoff_datetime FROM dbo.[05/21GreenTrip]
        UNION ALL SELECT lpep_pickup_datetime, lpep_dropoff_datetime FROM dbo.[06/21GreenTrip]
        UNION ALL SELECT lpep_pickup_datetime, lpep_dropoff_datetime FROM dbo.[07/21GreenTrip]
        UNION ALL SELECT lpep_pickup_datetime, lpep_dropoff_datetime FROM dbo.[08/21GreenTrip]
        UNION ALL SELECT lpep_pickup_datetime, lpep_dropoff_datetime FROM dbo.[09/21GreenTrip]
        UNION ALL SELECT lpep_pickup_datetime, lpep_dropoff_datetime FROM dbo.[10/21GreenTrip]
        UNION ALL SELECT lpep_pickup_datetime, lpep_dropoff_datetime FROM dbo.[11/21GreenTrip]
        UNION ALL SELECT lpep_pickup_datetime, lpep_dropoff_datetime FROM dbo.[12/21GreenTrip]
        UNION ALL SELECT lpep_pickup_datetime, lpep_dropoff_datetime FROM dbo.[01/22GreenTrip]
        UNION ALL SELECT lpep_pickup_datetime, lpep_dropoff_datetime FROM dbo.[02/22GreenTrip]
        UNION ALL SELECT lpep_pickup_datetime, lpep_dropoff_datetime FROM dbo.[03/22GreenTrip]
        UNION ALL SELECT lpep_pickup_datetime, lpep_dropoff_datetime FROM dbo.[04/22GreenTrip]
        UNION ALL SELECT lpep_pickup_datetime, lpep_dropoff_datetime FROM dbo.[05/22GreenTrip]
        UNION ALL SELECT lpep_pickup_datetime, lpep_dropoff_datetime FROM dbo.[06/22GreenTrip]
        UNION ALL SELECT lpep_pickup_datetime, lpep_dropoff_datetime FROM dbo.[07/22GreenTrip]
        UNION ALL SELECT lpep_pickup_datetime, lpep_dropoff_datetime FROM dbo.[08/22GreenTrip]
        UNION ALL SELECT lpep_pickup_datetime, lpep_dropoff_datetime FROM dbo.[09/22GreenTrip]
        UNION ALL SELECT lpep_pickup_datetime, lpep_dropoff_datetime FROM dbo.[10/22GreenTrip]
        UNION ALL SELECT lpep_pickup_datetime, lpep_dropoff_datetime FROM dbo.[11/22GreenTrip]
        UNION ALL SELECT lpep_pickup_datetime, lpep_dropoff_datetime FROM dbo.[12/22GreenTrip]
    ) AS viajes
    WHERE 
        lpep_dropoff_datetime > lpep_pickup_datetime
        AND YEAR(lpep_pickup_datetime) BETWEEN 2021 AND 2022
        AND DATEDIFF(MINUTE, lpep_pickup_datetime, lpep_dropoff_datetime) BETWEEN 1 AND 180
    GROUP BY 
        YEAR(lpep_pickup_datetime), 
        MONTH(lpep_pickup_datetime)
    ORDER BY Año, Mes;