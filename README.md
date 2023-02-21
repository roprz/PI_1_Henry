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
- Unificación  de las 4 plataformas a través de la función 'concat' en un dataframe único "df".
- Reemplazo valores nulos del campo Rating por "g".
- Conversión de date_added al formato adecuado (AAAA-mm-dd).
- Conversión de campos de textos a minuscula.
- Separación de columna 'duration' en dos ("duration_int" y "duration_type").
- Unificación de season y seasons en 'season' en la columna 'duration_type'.
- Ingesta de los 8 archivos csv que contienen los Scores de los usuarios en sus respectivos dataframes.
- Unificación de los 8 archivos a través de la función 'concat' en un dataframe único "scoredf".
- Conversión de timestamp al formato adecuado (AAAA-mm-dd).
- Renombramos las columnas 'rating':'score', 'timestamp':'scoreDate' y'movieId':'id'.
- Creación de una columna nueva con el score promedio de cada pelicula.
- Unificación de los dataframes (df y scoredf) en un solo dataframe (dffinal). Usando como relación la columna 'id'.
- Creación de un dataframe nuevo (df_consultas) enfocado en la API de consultas usando como base el 'dffinal'.
- Eliminación de los duplicado de la columna 'id' (la cual hace referecia a la película) quedandonos únicamente con 22998 valores únicos.
- Exportarmos 'df_consultas' en un archivo csv.
- Exportamos 'dffinal' en un archivo .parquet.

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

### Proceso de puesta a disposición los datos utilizando FastAPI (framework que permite construir APIs con Python) y Deta Space para realizar el deploy: 
- Generación de archivo main.py (donde desarrollar el script) y otro requirements.txt (donde alojar los requerimientos para la API)
- Importación de las librerías a utilizar
- Declaración de la creación de la API 
- Declaración de la ruta de acceso para la base de datos (df_consultas)
- Desarrollo de las consultas con formato:
   
```ruby
@app.get("/tipo_de_consulta/")
def tipo_de_consulta(variable1:tipo_de_dato, variable"n":...):
  desarrollo_de_la_funcion
```

7. Creacion de una cuenta en Deta
8. Instalacion del Deta CLI en consola de forma local mediante comando "iwr https://get.deta.dev/cli.ps1 -useb | iex"
9. Comprobación de la correcta instalacion con "deta --help"
10. Login en deta a traves de la consola mediante comando "deta login"
11. Ubicado en el path de la carpeta donde se encuentra la API desarrollada se procede a la creacion de un micro mediante el comando "deta new"
12. Una vez creado el micro, se realizan las pruebas correspondientes a las consultas con el endpoint URL provisto por deta.

<hr>

### Instrucciones para la utilización de la herramienta: 
`Ingrese al siguiente URL:` [https://qlprmb.deta.dev](https://qlprmb.deta.dev)

Segun lo consulta que quiera solicitar, debera agregarle a continuación del URL la **consulta y variables** con el siguiente **formato**:
- Consulta 1: .../**get_word_count/?plataforma=netflix&keyword=love**
- Consulta 2: ...**/get_score_count/?plataform=netflix&score=85&year=2010**
- Consulta 3: ...**/get_second_score/?plataforma=amazon**
- Consulta 4: ...**/get_longest/?plataforma=netflix&duracion=min&anio=2016**
- Consulta 5: ...**/get_rating_count/?rate=18%2B**

Las variables pueden ser reemplazadas en el formato de consulta por el elemento deseado: 
- **Plataforma**: **netflix, disney, hulu, amazon**
- **Keyword**: puede ser reemplazado por cualquier termino deseado (la busqueda se realiza en el "titulo" de peliculas)
- **Score**: puntaje determinado de movie/serie
- **Year**: año de estreno de movie/serie
- **Duracion**: tipo de duracion en **min** o **season**
- **Rate**: rate de determinada pelicula utilizando **g** (general), **7+**, **13+**, **16+**, **18+** (*Nota: el simbola "+" debe ser reemplazado por "%2B" - Ejemplo: 18+ = 18%2B*)

<hr> 

#### Ejemplos de busquedas: 
- **Consulta 1:** https://qlprmb.deta.dev/get_word_count/?plataforma=netflix&keyword=love
- **Consulta 2:** https://qlprmb.deta.dev/get_score_count/?plataform=netflix&score=85&year=2010
- **Consulta 3:** https://qlprmb.deta.dev/get_second_score/?plataforma=amazon
- **Consulta 4:** https://qlprmb.deta.dev/get_longest/?plataforma=netflix&duracion=min&anio=2016
- **Consulta 5:** https://qlprmb.deta.dev/get_rating_count/?rate=18%2B

##### *Nota: Para conocer mas detalles tecnicos acerca de las funciones y sus respectivos parametros puede ingresar a https://qlprmb.deta.dev/docs*


#### [Link a video explicativo confeccionado para equipo de data analytics](https://www.youtube.com/watch?v=o7A5xAoOQqE "Proyecto Individual data engineer - Henry's bootcamp")

<hr> 

#### Tecnologías utilizadas:
- Visual studio code
- Python
- Deta cloud
- FastApi
- Uvicorn
- Pandas library

  
<img src="https://visualstudio.microsoft.com/wp-content/uploads/2019/06/vs-code-responsive-01.svg" width="50"/><img src="https://www.python.org/static/community_logos/python-logo.png" width="150"/><img src="https://raw.githubusercontent.com/deta/.github/main/profile/deta_logo_dark.svg" width="250"/><img src="https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png" width="150"/><img src="https://raw.githubusercontent.com/tomchristie/uvicorn/master/docs/uvicorn.png" width="80"/><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/e/ed/Pandas_logo.svg/1920px-Pandas_logo.svg.png" width="150"/>