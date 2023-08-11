# Henry: Proyecto Individual MLOps

*Contexto.* Este proyecto responde a las consignas establecidas por la organizacion Henry como parte del primer proyecto individual: [MLOps](https://github.com/soyHenry/PI_ML_OPS).

 El proyecto esta dividido en 4 partes. En resumen, el proyecto consiste en i. limpiar y normalizar una base datos (ETL), ii. examinar la naturaleza y composicion de los datos (EDA), iii. diseñar e implementar un modelo de semejanza de caracteristicas de casos (ML) para que sirve de base para un sistema de recomendación, y iv. alimentar un conjunto de consultas a traves de un API en Render: [Enlace API](https://henry-mlops-imdb.onrender.com/docs)

#### 1. ETL
Para facilitar la lectura, dividimos la fase de ETL en 4 fases:
1. [Limpieza de datos](data_prcssng/01_etl_movies_subset_limpiar.ipynb)
2. [Desanidar movies](data_prcssng/02_etl_movies_desanidar_v3.ipynb)
3. [Desanidar credits](data_prcssng/03_etl_credits_desanidar_v3.ipynb)
4. [Generar dfs para alimentar consultas del API](data_prcssng/04_etl_merge_datafinal_v2.ipynb)

#### 2. EDA
La fase del [analisis exploratorio de datos](data_prcssng/05_eda_v1.ipynb) esta orientada por la siguiente pregunta: ¿Qué podemos esperar como resultado en las consultas?

#### 3. ML del sistema de recomendacion
El sistema de recomendación esta basado en un [modelo no-supervisado.](data_prcssng/06_ml_recomendaciones_v3.ipynb)

#### 4. API de consultas

1. Prueba piloto de funciones que median las consultas: [Test de consultas.](data_prcssng/07_test_funciones.ipynb)
2. El API de consultas implementado en Render: [Enlace API.](https://henry-mlops-imdb.onrender.com/docs)
3. Prueba de implementación del API: [video](https://drive.google.com/file/d/1l_noVxU2NVhfE3jFHW210eWAeEiPmo22/view?usp=sharing)