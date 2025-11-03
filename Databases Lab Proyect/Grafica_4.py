from sqlalchemy import create_engine
import pandas as pd
import plotly.express as px

def crear_grafica4():
    # conexión con autenticación de Windows
    engine = create_engine(
        "mssql+pyodbc://localhost\\SQLEXPRESS/GreenTaxiTrip2021_2022?driver=ODBC+Driver+17+for+SQL+Server&trusted_connection=yes"
    )

    # consulta SQL: duración promedio por mes
    query = """
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
    """

    # ejecutar la consulta
    df = pd.read_sql(query, engine)

    # crear columna representativa del mes (texto tipo "2021-03")
    df["Periodo"] = df["Año"].astype(str) + "-" + df["Mes"].astype(str).str.zfill(2)

    # crear la gráfica
    fig = px.line(
        df,
        x='Periodo',
        y='DuracionPromedio',
        title='Duración promedio de viajes por mes (2021-2022)',
        markers=True,
        line_shape='spline',
        labels={'Periodo': 'Mes', 'DuracionPromedio': 'Duración promedio (minutos)'}
    )

    # estilo igual al de tus otras gráficas
    fig.update_traces(line_color='green')
    fig.update_layout(
        hovermode='x unified',
        template='plotly_white',
        font=dict(size=14),
        title_x=0.5,
        xaxis=dict(
            tickangle=45,
            tickmode='array',
            tickvals=df['Periodo'],
            ticktext=df['Periodo']
        )
    )

    fig.show()
    return fig

# ejecutar función
crear_grafica4()
