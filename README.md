# Explorador ESOLMET

Este proyecto es una aplicación web interactiva desarrollada con Shiny for Python. Permite visualizar, analizar y descargar datos meteorológicos y solarimétricos de la estación ESOLMET-IER, abarcando diferentes años y variables clave.

Puedes visitar la Web App con este enlace:
[https://jramonha.shinyapps.io/explorador-esolmet1/](https://jramonha.shinyapps.io/explorador-esolmet1/)


## Objetivo

El proyecto busca ofrecer una herramienta interactiva y accesible para explorar y analizar datos meteorológicos y solarimétricos recopilados por ESOLMET-IER. Diseñada para facilitar la comprensión de patrones climáticos y la exploración de datos históricos, esta aplicación web incorpora gráficos dinámicos y herramientas avanzadas de filtrado, que permiten visualizar tendencias personalizables en diferentes escalas de tiempo: diaria, semanal, mensual o anual.

Además, la herramienta proporciona promedios mensuales y garantiza el acceso sencillo a los datos en un formato descargable, promoviendo su reutilización y análisis detallado.


## Proceso de limpieza de datos

Los datos crudos de ESOLMET son procesados en seis pasos clave para asegurar su consistencia y preparación para análisis:

1. **Carga y conversión**:  
   - Los archivos `.csv` se leen con `pandas`, convirtiendo valores no numéricos en `NaN`.

2. **Definición de índice temporal**:  
   - La columna 0 se define como índice del DataFrame y se convierte a formato `datetime` utilizando `parse_dates=True`.

3. **Renombrado de columnas**:  
   - Las columnas reciben nombres más claros y descriptivos, como `'I_dir_Avg'` → `'Ib'` (radiación solar directa).

4. **Eliminación de columnas irrelevantes**:  
   - Columnas como `'RECORD'`, `'I_uv_Avg'` y `'Rain_mm_Tot'` se eliminan si están presentes.

5. **Exportación de datos limpios**:  
   - Los datos procesados se guardan en formato `.parquet` para un manejo más eficiente.


## Estructura del proyecto

### Archivos principales

1. [app.py](https://github.com/JRamonHA/Proyecto-Final/blob/main/app.py): 
   - Contiene la lógica principal de la aplicación web, incluidas las definiciones de la interfaz de usuario y el servidor.
   - Utiliza librerías como `pandas` y `plotly` para el manejo y la visualización de datos.

2. [funciones.py](https://github.com/JRamonHA/Proyecto-Final/blob/main/funciones.py): 
   - Proporciona utilidades para cargar datos según el año.

3. [limpieza.ipynb](https://github.com/JRamonHA/Proyecto-Final/blob/main/notebooks/limpieza.ipynb): 
   - Implementa el proceso de limpieza y preprocesamiento de los datos antes de cargarlos en la aplicación.

4. [index.qmd](https://github.com/JRamonHA/Proyecto-Final/blob/main/index.qmd): 
   - Diapositivas sobre la presentación del proyecto.


## Funcionalidades

La aplicación web incluye lo siguiente:

1. **Visualización anual y mensual**:
   - Gráficos interactivos que muestran las tendencias de variables meteorológicas a lo largo del tiempo.
   - Resúmenes mensuales que incluyen medias, máximos, mínimos y desviaciones estándar.

2. **Selección de datos personalizada**:
   - Filtros por año, rango de fechas y variable meteorológica.

3. **Exploración de datos**:
   - Vista tabular de los datos filtrados.

4. **Descarga de datos**:
   - Posibilidad de descargar los datos seleccionados en formato CSV.


## Créditos
Los datos pertenecen a la estación [ESOLMET-IER](https://esolmet.ier.unam.mx/) y están destinados únicamente para fines educativos y de investigación.
