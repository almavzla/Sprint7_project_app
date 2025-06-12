# A continuación importaremos las librerías necesarias para el análisis exploratorio de datos
import streamlit as st
import pandas as pd
import plotly.express as px
# Crear dataframe / leer el archivo csv elegido
students_data = pd.read_csv('Students Social Media Addiction.csv')
st.title('Students Social Media Addiction:worried:')
st.header('Histogramas')
# Crear el primer histograma edad
st.subheader('Distribución de la edad de los estudiantes encuestados')
# Crear el botón 1
edad_hist_button = st.button(
    'Construir histograma edad', help='clic para crear',)
if edad_hist_button:  # Si se presionó el botón entonces...
    # Escribir este mensaje
    st.write('Creando histograma para el conjunto de datos')
    # Crear el histograma de edad
    fig_1 = px.histogram(students_data, x='Age',
                         title='Distribución de la Edad de los Estudiantes encuestados',
                         labels={'Age': 'Edad del Estudiante'},
                         color_discrete_sequence=['skyblue'])
    # Mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig_1, use_container_width=True)
# Crear el segundo histograma puntuación salud mental
st.subheader('Distribución de la Puntuación de Salud Mental de los Estudiantes')
# Crear botón 2
score_hist_button = st.button(
    'Construir histograma score', help='clic para crear',)  # Escribir este mensaje
if score_hist_button:  # Si se presionó el botón entonces...
    st.write('Creando el histograma score')
    # Crear el histograma de score
    fig_2 = px.histogram(students_data, x='Mental_Health_Score',
                         title='Distribución de la Puntuación de Salud Mental de los Estudiantes',
                         labels={
                             'Mental_Health_Score': 'Puntuación de Salud Mental (1-10)'},
                         color_discrete_sequence=['lightcoral'],
                         nbins=10)
    # Mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig_2, use_container_width=True)
# Ahora crearemos gráficos de dispersión
st.header('Gráficos de Dispersión')
# El usuario puede elegir que gráfica crear:
st.subheader('Selecciona que gráfico quieres crear:')
# Check box 1
disp_graph_1 = st.checkbox(
    'Horas de Uso Diario de Redes Sociales vs. Puntuación de Adicción:iphone:')
# Check box 2
disp_graph_2 = st.checkbox(
    'Horas de Sueño por Noche vs. Puntuación de Salud Mental:sleeping:')
# Si selecciona el primero
if disp_graph_1:
    st.write(
        'Creando gráfca para Horas de Uso Diario de Redes Sociales vs. Puntuación de Adicción:iphone:')
    # Crear la gráfica de dispersión
    fig_addiction = px.scatter(students_data,
                               x='Avg_Daily_Usage_Hours',
                               y='Addicted_Score',
                               title='Horas de Uso Diario de Redes Sociales vs. Puntuación de Adicción',
                               labels={
                                   'Avg_Daily_Usage_Hours': 'Horas de Uso Diario Promedio',
                                   'Addicted_Score': 'Puntuación de Adicción (1-10)'
                               })
    st.plotly_chart(fig_addiction, use_container_width=True)
if disp_graph_2:
    st.write(
        'Creando gráfico para Horas de Sueño por Noche vs. Puntuación de Salud Mental:sleeping:')
    # Crear la gráfica de dispersión
    fig_sleep_mental = px.scatter(students_data,
                                  x='Sleep_Hours_Per_Night',
                                  y='Mental_Health_Score',
                                  title='Horas de Sueño por Noche vs. Puntuación de Salud Mental',
                                  labels={
                                      'Sleep_Hours_Per_Night': 'Horas de Sueño por Noche',
                                      'Mental_Health_Score': 'Puntuación de Salud Mental (1-10)'
                                  })
    st.plotly_chart(fig_sleep_mental, use_container_width=True)

st.text('Fuente de información: https://www.kaggle.com/code/adilshamim8/social-media-addiction-among-students')
st.text('Appby: Alma Valenzuela')
