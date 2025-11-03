from sqlalchemy import create_engine
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

def crear_grafica3():
    # Conexión con autenticación de Windows
    engine = create_engine(
        "mssql+pyodbc://localhost\\SQLEXPRESS/GreenTaxiTrip2021_2022?driver=ODBC+Driver+17+for+SQL+Server&trusted_connection=yes"
    )

    # QUERY AÑO 2021 (simplificado)
    query_2021 = """
    SELECT 
        passenger_count AS [Num. pasajeros],
        COUNT(*) AS [Viajes por Num. pasajeros]
    FROM (
        SELECT passenger_count FROM dbo.[01/21GreenTrip]
        UNION ALL SELECT passenger_count FROM dbo.[02/21GreenTrip]
        UNION ALL SELECT passenger_count FROM dbo.[03/21GreenTrip]
        UNION ALL SELECT passenger_count FROM dbo.[04/21GreenTrip]
        UNION ALL SELECT passenger_count FROM dbo.[05/21GreenTrip]
        UNION ALL SELECT passenger_count FROM dbo.[06/21GreenTrip]
        UNION ALL SELECT passenger_count FROM dbo.[07/21GreenTrip]
        UNION ALL SELECT passenger_count FROM dbo.[08/21GreenTrip]
        UNION ALL SELECT passenger_count FROM dbo.[09/21GreenTrip]
        UNION ALL SELECT passenger_count FROM dbo.[10/21GreenTrip]
        UNION ALL SELECT passenger_count FROM dbo.[11/21GreenTrip]
        UNION ALL SELECT passenger_count FROM dbo.[12/21GreenTrip]
    ) AS all_data
    WHERE passenger_count IS NOT NULL AND passenger_count != 0 AND passenger_count <= 6
    GROUP BY passenger_count
    ORDER BY passenger_count;
    """

    # QUERY AÑO 2022 (simplificado)
    query_2022 = """
    SELECT 
        passenger_count AS [Num. pasajeros],
        COUNT(*) AS [Viajes por Num. pasajeros]
    FROM (
        SELECT passenger_count FROM dbo.[01/22GreenTrip]
        UNION ALL SELECT passenger_count FROM dbo.[02/22GreenTrip]
        UNION ALL SELECT passenger_count FROM dbo.[03/22GreenTrip]
        UNION ALL SELECT passenger_count FROM dbo.[04/22GreenTrip]
        UNION ALL SELECT passenger_count FROM dbo.[05/22GreenTrip]
        UNION ALL SELECT passenger_count FROM dbo.[06/22GreenTrip]
        UNION ALL SELECT passenger_count FROM dbo.[07/22GreenTrip]
        UNION ALL SELECT passenger_count FROM dbo.[08/22GreenTrip]
        UNION ALL SELECT passenger_count FROM dbo.[09/22GreenTrip]
        UNION ALL SELECT passenger_count FROM dbo.[10/22GreenTrip]
        UNION ALL SELECT passenger_count FROM dbo.[11/22GreenTrip]
        UNION ALL SELECT passenger_count FROM dbo.[12/22GreenTrip]
    ) AS all_data
    WHERE passenger_count IS NOT NULL AND passenger_count != 0 AND passenger_count <= 6
    GROUP BY passenger_count
    ORDER BY passenger_count;
    """

    # Ejecutar los queries correctamente
    df_2021 = pd.read_sql(query_2021, engine)
    df_2022 = pd.read_sql(query_2022, engine)

    # Crear gráfico combinado (dos pie charts lado a lado)
    fig = make_subplots(
        rows=1, cols=2,
        specs=[[{'type': 'domain'}, {'type': 'domain'}]],
        subplot_titles=['Distribución de pasajeros — 2021', 'Distribución de pasajeros — 2022']
    )

    fig.add_trace(go.Pie(
        labels=df_2021['Num. pasajeros'],
        values=df_2021['Viajes por Num. pasajeros'],
        name='2021',
        hole=0.4,
        textinfo='label+percent',
        hovertemplate='Pasajeros: %{label}<br>Viajes: %{value}<br>%: %{percent}<extra></extra>'
    ), 1, 1)

    fig.add_trace(go.Pie(
        labels=df_2022['Num. pasajeros'],
        values=df_2022['Viajes por Num. pasajeros'],
        name='2022',
        hole=0.4,
        textinfo='label+percent',
        hovertemplate='Pasajeros: %{label}<br>Viajes: %{value}<br>%: %{percent}<extra></extra>'
    ), 1, 2)

    fig.update_layout(
        title_text='Distribución de viajes según número de pasajeros — Años 2021 y 2022',
        annotations=[
            dict(text='2021', x=0.18, y=0.5, font_size=16, showarrow=False),
            dict(text='2022', x=0.82, y=0.5, font_size=16, showarrow=False)
        ],
        legend_title_text='Número de pasajeros',
        showlegend=True,
        height=600
    )

    fig.show()
    return fig

crear_grafica3()