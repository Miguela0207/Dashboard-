import random
from faker import Faker
from datetime import datetime
from django.shortcuts import render
from venta.models import Venta
import plotly.express as px
import pandas as pd

def saludar(request):
    # Obtener todas las instancias del modelo Venta
    ventas = Venta.objects.all()
    
    # Crear un DataFrame con los datos de Venta
    df = pd.DataFrame(list(ventas.values()))
    
    # Definir el orden deseado de los meses
    orden_meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']
    
    # Convertir la columna "mes" en una categoría con el orden deseado
    df['mes'] = pd.Categorical(df['mes'], categories=orden_meses, ordered=True)
    
    # Agrupar los datos por barrio y mes y sumar las ventas
    df_grouped = df.groupby(['barrio', 'mes']).sum().reset_index()
    
    # Generar el gráfico de barras con título personalizado
    grafico = px.bar(df_grouped, x="barrio", y="venta", color="mes", barmode="group")
    
    # Personalizar el título del gráfico
    grafico.update_layout(
        title={
            'text': "Ventas por Barrio y Mes",
            'y': 0.95,  # Ubicación vertical del título
            'x': 0.5,   # Ubicación horizontal del título (centrado)
            'xanchor': 'center',  # Anclaje horizontal del título (centrado)
            'yanchor': 'top',     # Anclaje vertical del título (arriba)
            'font': dict(size=24) # Tamaño de la letra del título
        }
    )
    
    # Convertir el gráfico en HTML
    mihtml = grafico.to_html(full_html=False)
    
    # Definir el contexto con los datos que se pasarán a la plantilla
    context = {
        "nombre": "Miguel",
        "venta": ventas,
        "grafico": mihtml
    }
    
    # Renderizar la plantilla HTML con el contexto
    return render(request, "venta/index.html", context)


#DATOS RAMDON

def generar_datos_aleatorios():
    # Inicializar Faker para generar nombres de barrios aleatorios
    faker = Faker()
    
    # Lista de nombres de barrios
    barrios = [faker.city() for _ in range(5)]
    
    # Lista de meses
    meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']
    
    # Generar un dato por mes en cada barrio
    for barrio in barrios:
        for mes in meses:
            # Generar un valor de venta aleatorio entre 100 y 1000
            venta = random.randint(100, 1000)
            
            # Crear una nueva instancia del modelo Venta y guardarla en la base de datos
            nueva_venta = Venta(barrio=barrio, venta=venta, mes=mes)
            nueva_venta.save()

# Llamar a la función para generar los datos aleatorios
generar_datos_aleatorios()