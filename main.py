from fastapi import FastAPI
import os
import pandas as pd

# cargamos los datos
data_mvp_funciones = pd.read_csv(
    os.path.join("data_prcssng", "3_output", "data_mvp_final_funciones.csv"),
    index_col=0,
).convert_dtypes()
data_mvp_director = pd.read_csv(
    os.path.join("data_prcssng", "3_output", "data_mvp_final_funciones_exitodir.csv"),
    index_col=0,
).convert_dtypes()
data_mvp_recomendacion = pd.read_csv(
    os.path.join("data_prcssng", "3_output", "data_mvp_ml_recomend_indexed.csv"),
    index_col=[0, 1],
).convert_dtypes()

app = FastAPI()


@app.get("/peliculas_idioma/{idioma}")
# definimos
def pelicula_idioma(idioma: str):
    cantidad = (
        data_mvp_funciones["pelicula_id"]
        .loc[data_mvp_funciones["original_language"].isin([idioma])]
        .nunique()
    )
    return f"{cantidad} películas fueron estrenadas en idioma: {idioma}"


@app.get("/peliculas_duracion/{pelicula}")
# definimos
def pelicula_duracion(pelicula: str):
    pelicula_title = str(pelicula)
    duracion = data_mvp_funciones.loc[
        data_mvp_funciones["title"].str.contains(pelicula_title), "runtime"
    ].iloc[0]
    release_year = data_mvp_funciones.loc[
        data_mvp_funciones["title"].str.contains(pelicula_title), "release_year"
    ].iloc[0]
    return f"{pelicula_title}. Duración: {round(duracion)} min; año: {release_year}"


@app.get("/franquicia/{franquicia}")
# definimos
def franquicia(franquicia: str):
    franquicia_str = str(franquicia)
    franquicia_subset = data_mvp_funciones.loc[
        data_mvp_funciones["franquicia"].str.contains(franquicia_str)
    ]
    cantidad = franquicia_subset["pelicula_id"].nunique()
    ganancia = franquicia_subset["revenue"].sum()
    ganancia_res = "{:,}".format(round(ganancia))
    promedio = franquicia_subset["revenue"].mean()
    promedio_res = "{:,}".format(round(promedio))
    return f"La franquicia {franquicia_str} posee {cantidad} película(s), una ganancia total de USD${ganancia_res}, y una ganancia promedio de USD${promedio_res} por pelicula."


@app.get("/peliculas_pais/{pais}")
# definimos
def pelicula_pais(pais: str):
    pais_str = str(pais)
    cantidad = (
        data_mvp_funciones["pelicula_id"]
        .loc[data_mvp_funciones["pais_name"].str.contains(pais_str)]
        .nunique()
    )
    return f"Se produjeron {cantidad} películas en el país {pais}"


@app.get("/productoras_exitosas/{productora}")
# definimos
def productora_exitosa(productora: str):
    productora_subset = data_mvp_funciones.loc[
        data_mvp_funciones["productora"].str.contains(productora)
    ]
    revenue = productora_subset["revenue"].sum()
    revenue_res = "{:,}".format(round(revenue))
    cantidad = productora_subset["pelicula_id"].nunique()
    return f"La productora {productora} ha tenido un revenue total de USD${revenue_res}, y realizo un total de {cantidad} de pelicula(s)"


@app.get("/get_director/{director}")
# definimos
def director_exitoso(director: str):
    director_subset = data_mvp_director.loc[
        data_mvp_director["director"].str.contains(director)
    ]
    director_return = director_subset["director_return"].drop_duplicates()
    director_return_res = round(float(director_return.iloc[0]), 2)
    columns_peliculas = [
        "pelicula_id",
        "title",
        "release_date",
        "budget",
        "revenue",
        "return",
    ]
    director_peliculas = director_subset[columns_peliculas].drop_duplicates()
    peliculas = []
    for _, pelicula in director_peliculas.iterrows():
        pelicula_info = {
            "nombre": pelicula["title"],
            "fecha_lanzamiento": pelicula["release_date"],
            "costo (USD)": ("{:,}".format(round(pelicula["budget"]))),
            "ganancia (USD)": ("{:,}".format(round(pelicula["revenue"]))),
            "retorno (ratio)": round(pelicula["return"], 2),
        }
        peliculas.append(pelicula_info)
    return {
        "director": director,
        "retorno total": director_return_res,
        "peliculas": peliculas,
    }
