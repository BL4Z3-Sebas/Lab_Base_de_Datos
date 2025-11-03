import pandas as pd
import plotly.express as px
from sqlalchemy import create_engine

# Conexión a SQL Server
def crear_grafica5():
    engine = create_engine(
        "mssql+pyodbc://localhost\\SQLEXPRESS/GreenTaxiTrip2021_2022?driver=ODBC+Driver+17+for+SQL+Server&trusted_connection=yes"
    )

    query = """
    WITH durvsdis AS (
        SELECT lpep_pickup_datetime AS salida,
            trip_distance AS distancia
        FROM dbo.[01/21GreenTrip]
        UNION ALL SELECT lpep_pickup_datetime, trip_distance FROM dbo.[02/21GreenTrip]
        UNION ALL SELECT lpep_pickup_datetime, trip_distance FROM dbo.[03/21GreenTrip]
        UNION ALL SELECT lpep_pickup_datetime, trip_distance FROM dbo.[04/21GreenTrip]
        UNION ALL SELECT lpep_pickup_datetime, trip_distance FROM dbo.[05/21GreenTrip]
        UNION ALL SELECT lpep_pickup_datetime, trip_distance FROM dbo.[06/21GreenTrip]
        UNION ALL SELECT lpep_pickup_datetime, trip_distance FROM dbo.[07/21GreenTrip]
        UNION ALL SELECT lpep_pickup_datetime, trip_distance FROM dbo.[08/21GreenTrip]
        UNION ALL SELECT lpep_pickup_datetime, trip_distance FROM dbo.[09/21GreenTrip]
        UNION ALL SELECT lpep_pickup_datetime, trip_distance FROM dbo.[10/21GreenTrip]
        UNION ALL SELECT lpep_pickup_datetime, trip_distance FROM dbo.[11/21GreenTrip]
        UNION ALL SELECT lpep_pickup_datetime, trip_distance FROM dbo.[12/21GreenTrip]
        UNION ALL SELECT lpep_pickup_datetime, trip_distance FROM dbo.[01/22GreenTrip]
        UNION ALL SELECT lpep_pickup_datetime, trip_distance FROM dbo.[02/22GreenTrip]
        UNION ALL SELECT lpep_pickup_datetime, trip_distance FROM dbo.[03/22GreenTrip]
        UNION ALL SELECT lpep_pickup_datetime, trip_distance FROM dbo.[04/22GreenTrip]
        UNION ALL SELECT lpep_pickup_datetime, trip_distance FROM dbo.[05/22GreenTrip]
        UNION ALL SELECT lpep_pickup_datetime, trip_distance FROM dbo.[06/22GreenTrip]
        UNION ALL SELECT lpep_pickup_datetime, trip_distance FROM dbo.[07/22GreenTrip]
        UNION ALL SELECT lpep_pickup_datetime, trip_distance FROM dbo.[08/22GreenTrip]
        UNION ALL SELECT lpep_pickup_datetime, trip_distance FROM dbo.[09/22GreenTrip]
        UNION ALL SELECT lpep_pickup_datetime, trip_distance FROM dbo.[10/22GreenTrip]
        UNION ALL SELECT lpep_pickup_datetime, trip_distance FROM dbo.[11/22GreenTrip]
        UNION ALL SELECT lpep_pickup_datetime, trip_distance FROM dbo.[12/22GreenTrip]
    )
    SELECT 
        YEAR(salida) AS Año,
        MONTH(salida) AS Mes,
        ROUND(AVG(distancia), 2) AS DistanciaPromedio
    FROM durvsdis dd
    WHERE dd.distancia > 0 AND salida >= '2021-01-01' AND salida < '2023-01-01'
    GROUP BY YEAR(salida), MONTH(salida)
    ORDER BY Año, Mes;
    """

    # Leer datos desde SQL Server
    df = pd.read_sql(query, engine)

    # Crear columna de fecha (para eje X)
    df["Fecha"] = pd.to_datetime(df["Año"].astype(str) + "-" + df["Mes"].astype(str) + "-01")

    import plotly.io as pio
    pio.renderers.default = "browser"  # fuerza render nuevo en navegador


    # Crear la gráfica (solo Distancia Promedio)
    fig_dist = px.area(
        df,
        x="Fecha",
        y="DistanciaPromedio",
        title="Distancia promedio mensual de los viajes (2021-2022)",
        labels={
            "Fecha": "Fecha",
            "DistanciaPromedio": "Distancia promedio (millas)"
        },
        template="plotly_white"
    )
    fig_dist.update_traces(line_color="#4B9CD3", line_width=3, fillcolor="#4B9CD3", opacity=0.5)
    fig_dist.update_layout(
        title_font_size=18,
        font=dict(size=13),
        xaxis=dict(showgrid=True, gridcolor="lightgray"),
        yaxis=dict(showgrid=True, gridcolor="lightgray"),
        hovermode="x unified"
    )
    
    return fig_dist
