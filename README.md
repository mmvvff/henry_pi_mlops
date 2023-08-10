# Henry: Proyecto Individual MLOps

*Contexto.* Este proyecto responde a las consignas establecidas por la organizacion Henry como parte del primer proyecto individual: [MLOps](https://github.com/soyHenry/PI_ML_OPS).

 El proyecto esta dividido en 4 partes. En resumen, el proyecto consiste en limpiar y normalizar una base datos (ETL), examinar la naturaleza y composicion de los datos (EDA), diseñar e implementar un modelo de semejanza de caracteristicas de casos (ML), y alimentar un sistema de consultas a traves de un API en Render.com: [Enlace API](https://henry-mlops-imdb.onrender.com/docs)

**1. ETL**
Para facilitar la lectura, dividimos el ETL en 4 fases:
1. [Limpieza de datos](data_prcssng/01_etl_movies_subset_limpiar.ipynb)
2. [Desanidar movies](data_prcssng/02_etl_movies_desanidar_v3.ipynb)
3. [Desanidar credits](data_prcssng/03_etl_credits_desanidar_v3.ipynb)
4. [Generar dfs para alimentar consultas del API](data_prcssng/04_etl_merge_datafinal_v2.ipynb)

**2. EDA**

[EDA: ¿Qué podemos esperar de las consultas?](data_prcssng/05_eda_v1.ipynb)

**3. ML**

[ML no-supervisado: Sistema de Recomendación](data_prcssng/06_ml_recomendaciones_v3.ipynb)

**4. Prueba de consultas**

En esta seccion, incluimos una prueba piloto de funciones que median las consultas: [Test de consultas](data_prcssng/07_test_funciones.ipynb)

**5. API consultas**

El API con acceso a las consultas esta disponible en el siguiente [Enlace API](https://henry-mlops-imdb.onrender.com/docs)

**6. Video: API consultas**

En caso que no se posible acceder [Enlace API](https://henry-mlops-imdb.onrender.com/docs), se ponde a disposición el siguiente video.