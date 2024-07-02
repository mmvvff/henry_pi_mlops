# Henry: Individual MLOps Project

[Spanish](https://github.com/mmvvff/henry_pi_mlops/blob/main/README_ES.md)

*Context.* This project responds to the guidelines established by the Henry organization as part of the first individual project: [MLOps](https://github.com/soyHenry/PI_ML_OPS).

The project is divided into 4 parts. In summary, the project consists of i. cleaning and normalizing a database (ETL), ii. examining the nature and composition of the data (EDA), iii. designing and implementing a feature similarity model (ML) to serve as the basis for a recommendation system, and iv. feeding a set of queries through an API on Render: [API Link](https://henry-mlops-imdb.onrender.com/docs)

#### 1. ETL
To facilitate reading, we divided the ETL phase into 4 stages:
1. [Data cleaning](data_prcssng/01_etl_movies_subset_limpiar.ipynb)
2. [Unnesting movies](data_prcssng/02_etl_movies_desanidar_v3.ipynb)
3. [Unnesting credits](data_prcssng/03_etl_credits_desanidar_v3.ipynb)
4. [Generating dataframes to feed API queries](data_prcssng/04_etl_merge_datafinal_v2.ipynb)

#### 2. EDA
The [exploratory data analysis](data_prcssng/05_eda_v1.ipynb) phase is guided by the following question: What can we expect as a result in the queries?

#### 3. ML of the recommendation system
The recommendation system is based on an [unsupervised model.](data_prcssng/06_ml_recomendaciones_v3.ipynb)

#### 4. Query API

1. Pilot test of functions that mediate queries: [Query test.](data_prcssng/07_test_funciones.ipynb)
2. The query API implemented on Render: [API Link.](https://henry-mlops-imdb.onrender.com/docs)
3. API implementation test: [video](https://drive.google.com/file/d/1h8k3CaLe0Q51vcL0pdxmG2JCakkP_UNy/view?usp=sharing)
4. [Querying the API using Python](https://github.com/mmvvff/henry_pi_mlops/blob/main/data_prcssng/08_api_consult.ipynb).