from sqlalchemy import create_engine
import pandas as pd
import plotly.express as px

#conexión con autenticación de windows
engine = create_engine(
    "mssql+pyodbc://localhost\\SQLEXPRESS/GreenTaxiTrip2021_2022?driver=ODBC+Driver+17+for+SQL+Server&trusted_connection=yes"
)

#consulta directa con el query
#query = 