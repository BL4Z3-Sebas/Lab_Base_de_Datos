from sqlalchemy import create_engine
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

def crear_grafica2():
    #conexión con autenticación de windows
    engine = create_engine(
        "mssql+pyodbc://localhost\\SQLEXPRESS/GreenTaxiTrip2021_2022?driver=ODBC+Driver+17+for+SQL+Server&trusted_connection=yes"
    )

    #consulta directa con el query
    query = """
    SELECT 
        YEAR(viaje) AS Año,
        MONTH(viaje) AS Mes,
        AVG(tarifa) AS Promedio_Tarifa
    FROM (
        SELECT lpep_pickup_datetime AS viaje, fare_amount AS tarifa FROM dbo.[01/21GreenTrip]
        UNION ALL SELECT lpep_pickup_datetime, fare_amount FROM dbo.[02/21GreenTrip]
        UNION ALL SELECT lpep_pickup_datetime, fare_amount FROM dbo.[03/21GreenTrip]
        UNION ALL SELECT lpep_pickup_datetime, fare_amount FROM dbo.[04/21GreenTrip]
        UNION ALL SELECT lpep_pickup_datetime, fare_amount FROM dbo.[05/21GreenTrip]
        UNION ALL SELECT lpep_pickup_datetime, fare_amount FROM dbo.[06/21GreenTrip]
        UNION ALL SELECT lpep_pickup_datetime, fare_amount FROM dbo.[07/21GreenTrip]
        UNION ALL SELECT lpep_pickup_datetime, fare_amount FROM dbo.[08/21GreenTrip]
        UNION ALL SELECT lpep_pickup_datetime, fare_amount FROM dbo.[09/21GreenTrip]
        UNION ALL SELECT lpep_pickup_datetime, fare_amount FROM dbo.[10/21GreenTrip]
        UNION ALL SELECT lpep_pickup_datetime, fare_amount FROM dbo.[11/21GreenTrip]
        UNION ALL SELECT lpep_pickup_datetime, fare_amount FROM dbo.[12/21GreenTrip]
        UNION ALL SELECT lpep_pickup_datetime, fare_amount FROM dbo.[01/22GreenTrip]
        UNION ALL SELECT lpep_pickup_datetime, fare_amount FROM dbo.[02/22GreenTrip]
        UNION ALL SELECT lpep_pickup_datetime, fare_amount FROM dbo.[03/22GreenTrip]
        UNION ALL SELECT lpep_pickup_datetime, fare_amount FROM dbo.[04/22GreenTrip]
        UNION ALL SELECT lpep_pickup_datetime, fare_amount FROM dbo.[05/22GreenTrip]
        UNION ALL SELECT lpep_pickup_datetime, fare_amount FROM dbo.[06/22GreenTrip]
        UNION ALL SELECT lpep_pickup_datetime, fare_amount FROM dbo.[07/22GreenTrip]
        UNION ALL SELECT lpep_pickup_datetime, fare_amount FROM dbo.[08/22GreenTrip]
        UNION ALL SELECT lpep_pickup_datetime, fare_amount FROM dbo.[09/22GreenTrip]
        UNION ALL SELECT lpep_pickup_datetime, fare_amount FROM dbo.[10/22GreenTrip]
        UNION ALL SELECT lpep_pickup_datetime, fare_amount FROM dbo.[11/22GreenTrip]
        UNION ALL SELECT lpep_pickup_datetime, fare_amount FROM dbo.[12/22GreenTrip]
    ) AS tt
    WHERE tt.viaje >= '2021-01-01' AND tt.viaje < '2023-01-01'
    GROUP BY YEAR(viaje), MONTH(viaje)
    ORDER BY Año, Mes;
    """

    #Ejecutar el query
    df = pd.read_sql(query, engine)
    print(df.head())

    # Convertimos el número de mes a nombre
    meses = ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun',
            'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dic']
    df['MesNombre'] = df['Mes'].apply(lambda x: meses[x-1])

    # Separar datos por año
    df_2021 = df[df['Año'] == 2021]
    df_2022 = df[df['Año'] == 2022]

    # Crear figura
    fig = go.Figure()

    # Añadir barras de 2021
    fig.add_trace(go.Bar(
        x=df_2021['MesNombre'],
        y=df_2021['Promedio_Tarifa'],
        name='2021',
        marker_color='navy',
        text=df_2021['Promedio_Tarifa'].round(2),
        textposition='inside',
        hovertemplate='Año: 2021<br>Mes: %{x}<br>Tarifa promedio: %{y:.2f} USD<extra></extra>'
    ))

    # Añadir barras de 2022
    fig.add_trace(go.Bar(
        x=df_2022['MesNombre'],
        y=df_2022['Promedio_Tarifa'],
        name='2022',
        marker_color='yellow',
        text=df_2022['Promedio_Tarifa'].round(2),
        textposition='inside',
        hovertemplate='Año: 2022<br>Mes: %{x}<br>Tarifa promedio: %{y:.2f} USD<extra></extra>'
    ))

    # Configurar el diseño
    fig.update_layout(
        title='Promedio mensual de tarifas — Años 2021 y 2022',
        xaxis_title='Mes',
        yaxis_title='Tarifa promedio (USD)',
        barmode='group',  # barras una al lado de la otra
        legend=dict(
            title='Año',
            orientation='h',
            yanchor='bottom',
            y=1.02,
            xanchor='center',
            x=0.5
        ),
        plot_bgcolor='white'
    )

    fig.show()
    return fig

crear_grafica2()