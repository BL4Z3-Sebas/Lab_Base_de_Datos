from flask import Flask, render_template
import plotly
import json
import sys
import os

# Asegura que Python pueda encontrar tus scripts
sys.path.append(os.path.join(os.path.dirname(__file__), 'PaginaWeb/templates'))

from Grafica_1 import crear_grafica1
from Grafica_2 import crear_grafica2
from Grafica_3 import crear_grafica3
from Grafica_4 import crear_grafica4
from Grafica_5 import crear_grafica5

app = Flask(
    __name__,
    template_folder='Databases Lab Proyect/PaginaWeb/templates',
    static_folder='Databases Lab Proyect/PaginaWeb/static'
)

@app.route('/')
def index():
    
    fig1 = crear_grafica1()
    fig2 = crear_grafica2()
    fig3 = crear_grafica3()
    fig4 = crear_grafica4()
    fig5 = crear_grafica5()
    graphs = {
        "grafico1": fig1.to_html(full_html=False),
        "grafico2": fig2.to_html(full_html=False),
        "grafico3": fig3.to_html(full_html=False),
        "grafico4": fig4.to_html(full_html=False),
        "grafico5": fig5.to_html(full_html=False)
    }

    return render_template("index.html", graphs=graphs)

if __name__ == '__main__':
    app.run(debug=True)
