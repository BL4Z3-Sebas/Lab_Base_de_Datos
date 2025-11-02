--Grafica 1: Numero de viajes (totales) x mes (años 2021 y 2021)
DECLARE @ViajeTotales TABLE (
    viaje DATETIME
);

-- Insertar datos desde cada tabla
INSERT INTO @ViajeTotales (viaje)
SELECT tr.lpep_pickup_datetime
FROM dbo.[01/21GreenTrip] tr;

INSERT INTO @ViajeTotales (viaje)
SELECT tr.lpep_pickup_datetime
FROM dbo.[02/21GreenTrip] tr;

INSERT INTO @ViajeTotales (viaje)
SELECT tr.lpep_pickup_datetime
FROM dbo.[03/21GreenTrip] tr;

INSERT INTO @ViajeTotales (viaje)
SELECT tr.lpep_pickup_datetime
FROM dbo.[04/21GreenTrip] tr;

INSERT INTO @ViajeTotales (viaje)
SELECT tr.lpep_pickup_datetime
FROM dbo.[05/21GreenTrip] tr;

INSERT INTO @ViajeTotales (viaje)
SELECT tr.lpep_pickup_datetime
FROM dbo.[06/21GreenTrip] tr;

INSERT INTO @ViajeTotales (viaje)
SELECT tr.lpep_pickup_datetime
FROM dbo.[07/21GreenTrip] tr;

INSERT INTO @ViajeTotales (viaje)
SELECT tr.lpep_pickup_datetime
FROM dbo.[08/21GreenTrip] tr;

INSERT INTO @ViajeTotales (viaje)
SELECT tr.lpep_pickup_datetime
FROM dbo.[09/21GreenTrip] tr;

INSERT INTO @ViajeTotales (viaje)
SELECT tr.lpep_pickup_datetime
FROM dbo.[10/21GreenTrip] tr;

INSERT INTO @ViajeTotales (viaje)
SELECT tr.lpep_pickup_datetime
FROM dbo.[11/21GreenTrip] tr;

INSERT INTO @ViajeTotales (viaje)
SELECT tr.lpep_pickup_datetime
FROM dbo.[12/21GreenTrip] tr;

INSERT INTO @ViajeTotales (viaje)
SELECT tr.lpep_pickup_datetime
FROM dbo.[01/22GreenTrip] tr;

INSERT INTO @ViajeTotales (viaje)
SELECT tr.lpep_pickup_datetime
FROM dbo.[02/22GreenTrip] tr;

INSERT INTO @ViajeTotales (viaje)
SELECT tr.lpep_pickup_datetime
FROM dbo.[03/22GreenTrip] tr;

INSERT INTO @ViajeTotales (viaje)
SELECT tr.lpep_pickup_datetime
FROM dbo.[04/22GreenTrip] tr;

INSERT INTO @ViajeTotales (viaje)
SELECT tr.lpep_pickup_datetime
FROM dbo.[05/22GreenTrip] tr;

INSERT INTO @ViajeTotales (viaje)
SELECT tr.lpep_pickup_datetime
FROM dbo.[06/22GreenTrip] tr;

INSERT INTO @ViajeTotales (viaje)
SELECT tr.lpep_pickup_datetime
FROM dbo.[07/22GreenTrip] tr;

INSERT INTO @ViajeTotales (viaje)
SELECT tr.lpep_pickup_datetime
FROM dbo.[08/22GreenTrip] tr;

INSERT INTO @ViajeTotales (viaje)
SELECT tr.lpep_pickup_datetime
FROM dbo.[09/22GreenTrip] tr;

INSERT INTO @ViajeTotales (viaje)
SELECT tr.lpep_pickup_datetime
FROM dbo.[10/22GreenTrip] tr;

INSERT INTO @ViajeTotales (viaje)
SELECT tr.lpep_pickup_datetime
FROM dbo.[11/22GreenTrip] tr;

INSERT INTO @ViajeTotales (viaje)
SELECT tr.lpep_pickup_datetime
FROM dbo.[12/22GreenTrip] tr;

-- Contar cuántos viajes hubo por fecha (ignorando la hora)
SELECT 
    CAST(vt.viaje AS DATE) AS Fecha,
    COUNT(*) AS TotalViajes
FROM @ViajeTotales vt
WHERE vt.viaje >= '2021-01-01' AND vt.viaje < '2023-01-01'
GROUP BY CAST(vt.viaje AS DATE)
ORDER BY Fecha;