import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Bakery Production Optimization Project", page_icon="🥖", layout="wide")

# Sidebar
st.sidebar.title("Menú")
menu = st.sidebar.radio("Navegación", ["Inicio", "Objetivos y Metodología", "Herramientas y Resultados", "Visualizaciones y Modelos", "Power BI Dashboard"])

# Imagen siempre visible
st.image("images/Bakery_2.png")

# Inicio
if menu == "Inicio":
    st.title("🥖 Bakery Production Optimization Project 🍞")
    st.markdown("""
    ¡Bienvenido a la aplicación del proyecto de optimización de producción de panadería! Esta aplicación proporciona una visión general del proyecto, incluyendo objetivos, metodología, herramientas usadas, resultados y más.

    ### Sobre el Proyecto
    La producción en una panadería puede ser un desafío debido a la naturaleza perecedera de los productos y la variabilidad en la demanda. Este proyecto tiene como objetivo desarrollar un modelo de aprendizaje automático que ayude a predecir las cantidades óptimas de producción, minimizando el desperdicio y mejorando la eficiencia.

    ### Problemas Abordados
    - **Pérdidas Financieras**: Los productos no vendidos generan pérdidas significativas.
    - **Desperdicio de Recursos**: La producción ineficiente resulta en ingredientes y mano de obra desperdiciados.
    - **Impacto Ambiental**: La producción excesiva contribuye a una mayor huella ambiental.

    ### Beneficios Esperados
    - **Reducción de Pérdidas**: Minimizar las pérdidas financieras al ajustar la producción a la demanda real.
    - **Eficiencia Operativa**: Mejorar la eficiencia en el uso de recursos y la planificación de la producción.
    - **Sostenibilidad**: Reducir el impacto ambiental al disminuir el desperdicio de productos.

    ### Estructura de la Aplicación
    Utiliza el menú de la izquierda para navegar por las diferentes secciones del proyecto, donde encontrarás detalles sobre los objetivos, la metodología, las herramientas utilizadas, los resultados obtenidos, las visualizaciones generadas y el dashboard interactivo de Power BI.
    """)

# Objetivos y Metodología
elif menu == "Objetivos y Metodología":
    st.title("🎯 Objetivos y ⚙️ Metodología")
    st.markdown("""
    ### 🎯 Objetivos
    El objetivo principal de este proyecto es desarrollar un modelo de aprendizaje automático para predecir las cantidades óptimas de producción en una panadería. Esto tiene como objetivo minimizar el desperdicio, reducir las pérdidas financieras, conservar recursos y disminuir la huella ambiental. El proyecto aborda los siguientes problemas clave:
    - **Pérdidas Financieras**: Los productos no utilizados generan pérdidas financieras significativas.
    - **Desperdicio de Recursos**: La producción ineficiente resulta en ingredientes y mano de obra desperdiciados.
    - **Impacto Ambiental**: La producción excesiva contribuye a una mayor huella ambiental.

    Al aprovechar los datos históricos de ventas, producción y demanda, el proyecto busca crear un modelo predictivo que pueda pronosticar con precisión las necesidades de producción, optimizando así las operaciones de la panadería.

    ### ⚙️ Metodología
    La metodología seguida en este proyecto incluye los siguientes pasos:

    - **📥 Carga y limpieza de datos**: Se cargan los datos históricos de ventas, producción y demanda, y se realiza una limpieza de datos para asegurar su calidad.
    - **🔍 Análisis exploratorio de datos (EDA)**: Se visualizan las distribuciones y relaciones entre variables para entender mejor el conjunto de datos.
    - **🛠️ Preprocesamiento de datos**: Se estandarizan los datos numéricos y se codifican las variables categóricas para preparar los datos para el entrenamiento del modelo.
    - **🧠 Desarrollo y evaluación de modelos de aprendizaje automático**: Se desarrollan y evalúan varios modelos de aprendizaje automático para predecir las cantidades óptimas de producción.
    - **📊 Generación de visualizaciones**: Se generan visualizaciones para interpretar los resultados y facilitar la toma de decisiones.
    - **🔮 Predicción de cantidades óptimas de producción**: Se utilizan los modelos entrenados para predecir las cantidades óptimas de producción.
    """)

# Herramientas y Resultados
elif menu == "Herramientas y Resultados":
    st.title("🛠️ Herramientas y 📊 Resultados")
    st.markdown("""
    ### 🛠️ Herramientas Usadas
    Las herramientas utilizadas en este proyecto incluyen:

    - **Python 🐍**: Lenguaje de programación principal utilizado para el desarrollo del proyecto.
    - **Pandas 🐼**: Biblioteca utilizada para la manipulación y análisis de datos.
    - **Matplotlib 📉 y Seaborn 🐟**: Bibliotecas utilizadas para la visualización de datos.
    - **Scikit-learn 🤖**: Biblioteca utilizada para el preprocesamiento de datos y el desarrollo de modelos de aprendizaje automático.
    - **Power BI 📊**: Herramienta utilizada para crear dashboards interactivos.

    ### 📊 Resultados
    Los resultados del proyecto mostraron una reducción significativa en los productos no vendidos, minimizando las pérdidas y mejorando la eficiencia de la producción. Los modelos desarrollados permitieron predecir con precisión las cantidades óptimas de producción, lo que resultó en una mejor planificación y gestión de los recursos.

    #### Principales Resultados:
    - **Reducción de Pérdidas**: Se logró una reducción significativa en los productos no vendidos, lo que minimizó las pérdidas financieras.
    - **Mejora en la Eficiencia de Producción**: La producción se optimizó, resultando en un uso más eficiente de los recursos y una menor huella ambiental.
    - **Predicciones Precisas**: Los modelos desarrollados permitieron predecir con precisión las necesidades de producción, facilitando la toma de decisiones y la planificación de la producción.
    """)

# Visualizaciones y Modelos
elif menu == "Visualizaciones y Modelos":
    st.title("📊 Visualizaciones y 🧠 Modelos")
    st.markdown("""
    ### 📊 Visualizaciones
    Las visualizaciones generadas en el proyecto incluyen:
    """)

    # Checkboxes para seleccionar los gráficos
    ventas_hora = st.checkbox("Tendencias de ventas por hora del día 🕒")
    ventas_dia = st.checkbox("Tendencias de ventas por día de la semana 📅")
    cantidad_mes = st.checkbox("Cantidad vendida por mes 📆")
    merma_ano_familia = st.checkbox("Merma por año y familia 📉")
    merma_familia = st.checkbox("Merma por familia 🍞")

    # Mostrar gráficos seleccionados
    if ventas_hora:
        st.image("images/Sales by Hour.png", caption="Tendencias de ventas por hora del día 🕒")
    if ventas_dia:
        st.image("images/Sales by day week.png", caption="Tendencias de ventas por día de la semana 📅")
    if cantidad_mes:
        st.image("images/Total mounth.png", caption="Cantidad vendida por mes 📆")
    if merma_ano_familia:
        st.image("images/Merma by family and year.png", caption="Merma por año y familia 📉")
    if merma_familia:
        st.image("images/Merma by family.png", caption="Merma por familia 🍞")

    st.markdown("""
    ### 🧠 Modelos y Métricas
    #### Modelo 1: Basado en Familias de Productos y Días de la Semana
    - **Modelos Usados**: Regresión Lineal, Árbol de Decisión, Bosque Aleatorio, Gradient Boosting
    - **Métricas de Evaluación**: Error Cuadrático Medio (MSE), Error Absoluto Medio (MAE), Raíz del Error Cuadrático Medio (RMSE), R-cuadrado (R2)

    #### Modelo 2: Basado en Productos Individuales y Días de la Semana
    - **Modelo Usado**: Bosque Aleatorio
    - **Métricas de Evaluación**: Error Cuadrático Medio (MSE), Error Absoluto Medio (MAE), Raíz del Error Cuadrático Medio (RMSE), R-cuadrado (R2)
    """)

# Power BI Dashboard
elif menu == "Power BI Dashboard":
    st.title("📊 Power BI Dashboard")
    st.markdown("""
    Se creó un dashboard interactivo en Power BI para analizar los resultados de los modelos predictivos y compararlos con los pedidos realizados por el gerente. Este dashboard permite una comparación gráfica de las predicciones del modelo con los datos de pedidos reales, facilitando la toma de decisiones y la planificación de la producción.

    ### Características del Dashboard:
    - **Comparación de Predicciones y Pedidos Reales**: Gráficos que muestran las diferencias entre las cantidades predichas por los modelos y las cantidades realmente ordenadas por el gerente.
    - **Análisis de Tendencias**: Visualización de tendencias de ventas y producción a lo largo del tiempo.
    - **Interactividad**: Filtros y segmentadores que permiten a los usuarios explorar los datos dinámicamente y personalizar su vista.
    """)
    st.image("images/Powerbi.png")

# Ejecutar la aplicación con: streamlit run app.py