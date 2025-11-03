from sqlalchemy import create_engine
import pandas as pd
import plotly.express as px

def crear_grafica1():
    # conexión con autenticación de Windows
    engine = create_engine(
        "mssql+pyodbc://localhost\\SQLEXPRESS/GreenTaxiTrip2021_2022?driver=ODBC+Driver+17+for+SQL+Server&trusted_connection=yes"
    )

    # consulta directa con UNION ALL y filtro por año
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

    # ejecutar el query directamente
    df = pd.read_sql(query, engine)

    # crear la figura (gráfica)
    fig = px.line(
        df,
        x='Fecha',
        y='TotalViajes',
        title='Total de viajes por día (2021-2022)',
        markers=True,
        line_shape='spline',
        labels={'Fecha': 'Fecha', 'TotalViajes': 'Número de viajes'}
    )

    fig.update_traces(line_color='green')
    fig.update_layout(
        hovermode='x unified',
        template='plotly_white',
        font=dict(size=14),
        title_x=0.5
    )
    fig.show()
    return fig

crear_grafica1()