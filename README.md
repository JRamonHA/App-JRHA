# Explorador ESOLMET

Este proyecto es una aplicación web interactiva desarrollada con Shiny for Python. Permite visualizar, analizar y descargar datos meteorológicos y solarimétricos de la estación ESOLMET-IER, abarcando diferentes años y variables clave.

Puedes visitar la Web App directamente en este enlace:
[https://jramonha.shinyapps.io/explorador-esolmet/](https://jramonha.shinyapps.io/explorador-esolmet/)


## Objetivo

El objetivo principal de este proyecto es proporcionar una herramienta accesible y eficiente para explorar los datos meteorológicos y solarimétricos de ESOLMET-IER. La aplicación está diseñada para facilitar el análisis de tendencias anuales y mensuales, así como el acceso a los datos en un formato descargable.

## Funcionalidades

La aplicación incluye las siguientes funcionalidades:

1. **Visualización Anual y Mensual**:
   - Gráficos interactivos que muestran las tendencias de variables meteorológicas a lo largo del tiempo.
   - Resúmenes mensuales que incluyen medias, máximos, mínimos y desviaciones estándar.

2. **Selección de Datos Personalizada**:
   - Filtros por año, rango de fechas y variable meteorológica.

3. **Exploración de Datos**:
   - Vista tabular de los datos filtrados.

4. **Descarga de Datos**:
   - Posibilidad de descargar los datos seleccionados en formato CSV.

## Estructura del Proyecto

### Archivos Principales

1. **`app.py`**:
   - Contiene la lógica principal de la aplicación web, incluidas las definiciones de la interfaz de usuario y el servidor.
   - Utiliza librerías como `pandas` y `plotly` para el manejo y la visualización de datos.

2. **`index.qmd`**:
   - Documenta el diseño del sitio web estático con información adicional sobre el proyecto.

3. **`cleaning.ipynb`**:
   - Implementa el proceso de limpieza y preprocesamiento de los datos antes de cargarlos en la aplicación.

4. **`funciones.py`**:
   - Proporciona utilidades para cargar datos según el año y realizar cálculos específicos.
  
## Créditos
Los datos pertenecen a la estación ![ESOLMET-IER](https://esolmet.ier.unam.mx/) y están destinados únicamente para fines educativos y de investigación.
