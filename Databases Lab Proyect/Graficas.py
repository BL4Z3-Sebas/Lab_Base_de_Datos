from sqlalchemy import create_engine
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt

# 🔹 Conexión con autenticación de Windows
engine = create_engine(
    "mssql+pyodbc://localhost\\SQLEXPRESS/GreenTaxiTrip2021_2022?driver=ODBC+Driver+17+for+SQL+Server&trusted_connection=yes"
)

# 🔹 Consulta directa con UNION ALL y filtro por año
query = """
SELECT 
    CAST(tr.lpep_pickup_datetime AS DATE) AS Fecha,
    COUNT(*) AS TotalViajes
FROM (
    SELECT lpep_pickup_datetime FROM dbo.[01/21GreenTrip]
    UNION ALL SELECT lpep_pickup_datetime FROM dbo.[02/21GreenTrip]
    UNION ALL SELECT lpep_pickup_datetime FROM dbo.[03/21GreenTrip]
    UNION ALL SELECT lpep_pickup_datetime FROM dbo.[04/21GreenTrip]
    UNION ALL SELECT lpep_pickup_datetime FROM dbo.[05/21GreenTrip]
    UNION ALL SELECT lpep_pickup_datetime FROM dbo.[06/21GreenTrip]
    UNION ALL SELECT lpep_pickup_datetime FROM dbo.[07/21GreenTrip]
    UNION ALL SELECT lpep_pickup_datetime FROM dbo.[08/21GreenTrip]
    UNION ALL SELECT lpep_pickup_datetime FROM dbo.[09/21GreenTrip]
    UNION ALL SELECT lpep_pickup_datetime FROM dbo.[10/21GreenTrip]
    UNION ALL SELECT lpep_pickup_datetime FROM dbo.[11/21GreenTrip]
    UNION ALL SELECT lpep_pickup_datetime FROM dbo.[12/21GreenTrip]
    UNION ALL SELECT lpep_pickup_datetime FROM dbo.[01/22GreenTrip]
    UNION ALL SELECT lpep_pickup_datetime FROM dbo.[02/22GreenTrip]
    UNION ALL SELECT lpep_pickup_datetime FROM dbo.[03/22GreenTrip]
    UNION ALL SELECT lpep_pickup_datetime FROM dbo.[04/22GreenTrip]
    UNION ALL SELECT lpep_pickup_datetime FROM dbo.[05/22GreenTrip]
    UNION ALL SELECT lpep_pickup_datetime FROM dbo.[06/22GreenTrip]
    UNION ALL SELECT lpep_pickup_datetime FROM dbo.[07/22GreenTrip]
    UNION ALL SELECT lpep_pickup_datetime FROM dbo.[08/22GreenTrip]
    UNION ALL SELECT lpep_pickup_datetime FROM dbo.[09/22GreenTrip]
    UNION ALL SELECT lpep_pickup_datetime FROM dbo.[10/22GreenTrip]
    UNION ALL SELECT lpep_pickup_datetime FROM dbo.[11/22GreenTrip]
    UNION ALL SELECT lpep_pickup_datetime FROM dbo.[12/22GreenTrip]
) AS tr
WHERE tr.lpep_pickup_datetime >= '2021-01-01' AND tr.lpep_pickup_datetime < '2023-01-01'
GROUP BY CAST(tr.lpep_pickup_datetime AS DATE)
ORDER BY Fecha;
"""

# 🔹 Ejecutar el query directamente
df = pd.read_sql(query, engine)

# 🔹 Mostrar primeros datos
print(df.head())

# 🔹 Graficar
plt.figure(figsize=(12,6))
plt.plot(df['Fecha'], df['TotalViajes'], color='green', linewidth=2)
plt.title('Total de viajes por día (2021–2022)', fontsize=14)
plt.xlabel('Fecha')
plt.ylabel('Número de viajes')
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()
