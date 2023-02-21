from fastapi import FastAPI
import pandas as pd

description= """
## Rodrigo Pérez Delgado
(_Github:_) przdel

## Funciones disponibles:
(_1_) **get_max_duration** <br><br>
Película con mayor duración con filtros opcionales de AÑO, PLATAFORMA Y TIPO DE DURACIÓN.<br><br><br>
(_2_) **get_score_count** <br><br>
Cantidad de películas por plataforma con un puntaje mayor a XX en determinado año.<br><br><br>
(_3_) **get_count_platform** <br><br>
Cantidad de películas por plataforma con filtro de PLATAFORMA.<br><br><br>
(_4_) **get_actor**<br><br>
Actor que más se repite según plataforma y año.<br>
""" 

app = FastAPI(
    title='Proyecto Individual 01',
    description=description,
    version='0.0.1'
)



df = pd.read_csv('Datasets/df_consultas.csv')

@app.get("/", tags=["Bienvenida"])
def index():
    return "Henry - Rodrigo Pérez - Proyecto Individual 01 - Favor de entrar /docs "

#Consulta 1: Película con mayor duración con filtros opcionales de AÑO, 
#PLATAFORMA Y TIPO DE DURACIÓN.(la función debe llamarse get_max_duration(year, platform, duration_type))
@app.get("/get_max_duration/", tags=["get_max_duration"])
def get_max_duration(year: int = None, plataform: str = None, duration_type: str = None):

    df_filtro = df.copy()

    if year is not None:
        df_filtro = df_filtro[df_filtro['release_year'] == year]

    if plataform is not None:
        if plataform == "amazon":
            df_filtro = df_filtro[df_filtro['id'].str.contains('a')]
        elif plataform == "disney":
            df_filtro = df_filtro[df_filtro['id'].str.contains('d')]
        elif plataform == "hulu":
            df_filtro = df_filtro[df_filtro['id'].str.contains('h')]
        elif plataform == "netflix":
            df_filtro = df_filtro[df_filtro['id'].str.contains('n')]

    if duration_type is not None:
        df_filtro = df_filtro[df_filtro['duration_type'] == duration_type]

    max_row = df_filtro.loc[df_filtro['duration_int'].idxmax()]
    titulo = max_row['title']
    
    return {"El titulo con mayor duración es:": titulo}



#Consulta 2: Cantidad de películas por plataforma con un puntaje mayor a XX en 
#determinado año (la función debe llamarse get_score_count(platform, scored, year))

@app.get("/get_score_count/", tags=["get_score_count"])
def get_score_count(plataform: str, year: int, scored: float):
    
    df_filtro = df.copy()

    if plataform is not None:
        if plataform == "amazon":
            df_filtro = df_filtro[df_filtro['id'].str.contains('a')]
        elif plataform == "disney":
            df_filtro = df_filtro[df_filtro['id'].str.contains('d')]
        elif plataform == "hulu":
            df_filtro = df_filtro[df_filtro['id'].str.contains('h')]
        elif plataform == "netflix":
            df_filtro = df_filtro[df_filtro['id'].str.contains('n')]
    
    df_filtro = df_filtro[df_filtro['release_year'] == year]

    df_filtro = df_filtro[df_filtro['scoreMean'] > scored]

    cantidad_score = df_filtro.shape[0]

    return {"El numero de peliculas con un Score mayor al solicitado es:": cantidad_score}



#Consulta 3: Cantidad de películas por plataforma con filtro de PLATAFORMA. 
#(La función debe llamarse get_count_platform(platform))
@app.get("/get_count_platform/", tags=["get_count_platform"])
def get_count_platform(plataform: str):

    df_filtro = df.copy()

    if plataform is not None:
        if plataform == "amazon":
            df_filtro = df_filtro[df_filtro['id'].str.contains('a')]
        elif plataform == "disney":
            df_filtro = df_filtro[df_filtro['id'].str.contains('d')]
        elif plataform == "hulu":
            df_filtro = df_filtro[df_filtro['id'].str.contains('h')]
        elif plataform == "netflix":
            df_filtro = df_filtro[df_filtro['id'].str.contains('n')]

    cantidad_pelicula = df_filtro.shape[0]

    return {"El numero de peliculas por plataform:": cantidad_pelicula}

#Consulta 4: Actor que más se repite según plataforma y año. 
# (La función debe llamarse get_actor(platform, year))
@app.get("/get_actor/", tags=["get_actor"])
def get_actor(plataform: str, year: int):

    df_filtro = df.copy()
    
    if plataform == "amazon":
        df_filtro = df_filtro[df_filtro['id'].str.contains('a')]
    elif plataform == "disney":
        df_filtro = df_filtro[df_filtro['id'].str.contains('d')]
    elif plataform == "hulu":
        return 'No se cuenta con información para esta plataforma'
    elif plataform == "netflix":
        df_filtro = df_filtro[df_filtro['id'].str.contains('n')]

    df_filtro = df_filtro[df_filtro['release_year'] == year]  

    actores = {}
    peliculas_procesadas = set() #evitar que las peliculas se repitan
    for i in range(len(df_filtro)): 
        pelicula = df_filtro.iloc[i] 
        if pelicula['id'] in peliculas_procesadas:
            continue
        lista_actores = pelicula['cast']
        if pd.isna(lista_actores) or lista_actores == '': #evitar valores nulos
            continue
        lista_actores = lista_actores.split(', ') #se divide para poder procesarlo
        for actor in lista_actores:
            if actor in actores:
                actores[actor] += 1
            else:
                actores[actor] = 1
        peliculas_procesadas.add(pelicula['id'])

    actor_mas_frecuente = max(actores, key=actores.get)
    return {"El actor más frecuente es:": actor_mas_frecuente}




