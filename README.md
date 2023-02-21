<p align=center><img src=https://assets.soyhenry.com/logos/LOGO-HENRY-04.png><p>

# PROYECTO INDIVIDUAL N°1 - DATA ENGINEER

## *Desarrollado por Rodrigo Pérez Delgado para Henry´s bootcamp* 


#### Problemática:
Realizar el ciclo de vida de un proyecto de **Machine Learning**, contemplando el tratamiento y recolección de los datos. Así como el entrenamiento y mantenimiento del modelo de ML según llegan nuevos datos.

#### Rol del desarrollador:
- Data engineer

<hr> 

### Proceso de "ETL" (Extract, transform, load) en VisualStudioCode - Python:

`EXTRACCIÓN DE DATOS Y TRANSFORMACIONES`


- Importación de la librería pandas para el manejo de dataframes.
- Ingesta de datos de streaming en sus respectivos dataframes (Disney, Amazon, Hulu y Netflix).
- Análisis exploratorio de los distintos datasets para conocer sus características principales.
- Generación del campo ID.
- Unificación  de las 4 plataformas a través de la función 'concat' en un dataframe único "df".
- Reemplazo valores nulos del campo Rating por "g".
- Conversión de date_added al formato adecuado (AAAA-mm-dd).
- Conversión de campos de textos a minúscula.
- Separación de columna 'duration' en dos ("duration_int" y "duration_type").
- Unificación de season y seasons en 'season' en la columna 'duration_type'.
- Ingesta de los 8 archivos csv que contienen los Scores de los usuarios en sus respectivos dataframes.
- Unificación de los 8 archivos a través de la función 'concat' en un dataframe único "scoredf".
- Conversión de timestamp al formato adecuado (AAAA-mm-dd).
- Renombramos las columnas 'rating':'score', 'timestamp':'scoreDate' y'movieId':'id'.
- Creación de una columna nueva con el score promedio de cada película.
- Unificación de los dataframes (df y scoredf) en un solo dataframe (dffinal). Usando como relación la columna 'id'.
- Creación de un dataframe nuevo (df_consultas) enfocado en la API de consultas usando como base el 'dffinal'.
- Eliminación de los duplicados de la columna 'id' (la cual hace referencia a la película) quedándonos únicamente con 22998 valores únicos.
- Exportamos 'df_consultas' en un archivo csv.
- Exportamos 'dffinal' en un archivo .parquet.

#### [Archivo Jupiter con el proceso de ETL](https://github.com/roprz/PI_1_Henry/blob/main/ETL/ETL.ipynb "ETL")


### Desarrollo de las consultas solicitadas:

`CONSULTAS A REALIZADAS`

1. **get_max_duration** 
Película con mayor duración con filtros opcionales de AÑO, PLATAFORMA Y TIPO DE DURACIÓN.
2. **get_score_count**
Cantidad de películas por plataforma con un puntaje mayor a XX en determinado año.
3. **get_count_platform**
Cantidad de películas por plataforma con filtro de PLATAFORMA.
4. **get_actor**
Actor que más se repite según plataforma y año.

#### [Carpeta con la que se desarrolla el API de Deta Space con la Consultas](https://github.com/roprz/PI_1_Henry/tree/main/API%20Deta%20Space "API Consultas")

### API de consultas
`Ingrese al siguiente URL:` [https://deta.space/discovery/@roprz/pi_1/exp-UHYs](https://deta.space/discovery/@roprz/pi_1/exp-UHYs)

### Realización de EDA con ayuda de la librería Dataprep:
- Se importó la librería dataprep y pyarrow.
- Con ayuda de la librería pyarrow se instaló nuestro archivo dffinal.parquet en un df.
- Tomamos una muestra del df para realizar nuestro análisis, ya que son demasiados datos para nuestra capacidad de procesamiento.
- Creamos un reporte con ayuda de la librería dataprep (reporte_EDA.html).- Visualizamos la correlación de los datos.
- Gracias al análisis tomó la decisión de realizar el modelo con la librería Surprise. Ya que esta sólo requiere el ID de la película, ID del usuario y Score que le otorgó a la película. Y contamos la info preparada para ello.

#### [Desarrollo del EDA](https://github.com/roprz/PI_1_Henry/blob/main/EDA/EDA.ipynb "EDA")
#### [Reporte EDA](https://github.com/roprz/PI_1_Henry/blob/main/EDA/reporte_EDA.html "Reporte EDA")

### Sistema de Recomendación:

- Importamos la librerías para la lectura de nuestro dataset en formato parquet.
- Instanciamos en un dataframe.
- Revisamos el número de id´s únicos con los que contamos antes de tomar una fracción del dataset.
- Tomamos una muestra al 25 por ciento (más adelante en el documento comprobé que este era el volumen de datos ideal).
- Comprobamos que todos los id´s se encuentren en la muestra.
- Instalación de la librería surprise para realizar el modelo.
- Mandamos a llamar las funciones necesarias de la librería.
- Creamos el objeto Reader con las escalas del Score.
- Cargamos los datos en una estructura de Surprise.
- Realizamos la división de los datos de entrenamiento y de prueba.
- Definimos la grilla de hiper parámetros a explorar.
- Inicializamos el objeto GridSearchCV.
- Entrenamos el modelo.
- Mejores hiper parámetros encontrados: {'n_factors': 50, 'n_epochs': 30, 'lr_all': 0.002, 'reg_all': 0.04}.
- El modelo se probó con el 100, 50, 25 y 10 por ciento de los datos. Buscando la mejor accuracy.
- Nuestro mejor resultado fue con 25%, con una media de 0.9953 de RMSE.
- Probamos que el modelo funcione de manera correcta.
- Exportamos nuestro modelo.

#### [Archivo Jupiter con el proceso de creación del modelo de ML](https://github.com/roprz/PI_1_Henry/blob/main/ML/Creacion%20del%20modelo/ML.ipynb "creación del modelo de ML")

#### [Prueba de importación de modelo y prueba](https://github.com/roprz/PI_1_Henry/blob/main/ML/Creacion%20del%20modelo/ML.ipynb "creación del modelo de ML")

#### [Función desarrollada con el modelo y función para su deploy](https://github.com/roprz/PI_1_Henry/blob/main/ML/Funcion%20ML/modeloML.ipynb "Función modelo de ML")

### Video de explicación:
`Ingrese al siguiente URL:` [https://drive.google.com/drive/u/1/folders/14w2LaXqYdRgZt_IkV28jsG9SkKotQdFb](https://drive.google.com/drive/u/1/folders/14w2LaXqYdRgZt_IkV28jsG9SkKotQdFb)