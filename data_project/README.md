# Data Project: Pipelines

- Nota: Parte del contenido de este directorio se encuentra en inglés debido a que mis principales fuentes de aprendizaje se encontraban en dicho idioma. Sin embargo, utilizo lenguaje estándar que es bastante conocido en la industria.

## ELT Pipeline (*elt_project/*)

<picture>
<source media= "(prefers-color-scheme: light)" srcset= "https://github.com/diegos41/repo_diplo_datos/blob/main/images/pipeline_elt.png">
<img alt= "This is the picture for elt pipeline.">
</picture>

En esta pipeline se crea primero la infraestructura necesaria para poder almacenar/procesar los datos en la nube *(Google Cloud Platform)*, utilizando *Terraform*. Las credenciales son reconocidas automáticamente gracias a la creación de una variable de entorno (descargar *Google SDK* previamente).

Se realiza la ingestión de los datasets *yellow taxi data- 2019/2020* y *green taxi data- 2019/2020* mediante un script y utilizando el entorno local. Se hizo uso de la *Google API* para poder acceder al *Bucket* satisfactoriamente.

Una vez cargados los datos en el *GCS Bucket*, se procede a crear dos *materialized tables* (una para cada servicio), con la ayuda de *BigQuery*. 

Las tablas creadas sirven de *source tables* (ver ***schema.yml***) para la serie de transformaciones hechas en *dbt Cloud* (ver subfolder ***dbt_production/***). El objetivo final es la creación de una *fact table* uniendo los dos servicios. Se toma como inspiración el *Kimball's Dimensional Modelling*.
En dbt se realiza la creación de dos *staging models*, uno para cada servicio, donde se 'castean' los tipos de datos a otros más adecuados según la columna en cuestión, entre otros ajustes. Todo esto es realizado con *SQL* queries. Finalmente, se crea una *fact table*, donde se efectúan *joins* con la [Taxi Zone Lookup Table](https://d37ci6vzurychx.cloudfront.net/misc/taxi+_zone_lookup.csv), para poder ver en detalle las zonas donde ocurren los ascensos/descensos de pasajeros, y no solamente observar *location ID's* que no proveen de mucha información a los stakeholders.

Adicionalmente, se utiliza de nuevo *Taxi Zone Lookup Table*, pero esta vez junto con *fact_trips* para crear un *core model* que permitirá saber las ganancias mensuales de ambos servicios (diríjase a ***dm_monthly_zone_revenue.sql***).

Por último, se toma la *fact table* (*fact_trips*) como recurso para crear un dashboard con *Google Looker Studio*, donde pueden observarse algunas tendencias interesantes (véase ***elt_project/results_dashboard.pdf***).

<br>

## ETL Pipelines (*etl_project/*)

### ETL Pipeline A- Local DataBase (*etl_project/local_db/*)

<picture>
<source media= "(prefers-color-scheme: light)" srcset= "https://github.com/diegos41/repo_diplo_datos/blob/main/images/pipeline_etl_1.png">
<img alt= "This is the picture for etl pipeline A.">
</picture>

Esta pipeline ingiere el archivo *CSV* correspondiente al servicio **green taxi**, en el mes de enero de 2019.

El script se corre en un contenedor de *Docker* y efectúa mayoritariamente los procesos de extracción, transformación y carga de *data*. Cabe destacar el uso de *Pandas* (no solo aquí si no a lo largo de todos los projectos) para la transformación de *datatypes*, como así también la creación de una tabla en *PostgreSQL*. 

Los servicios utilizados se construyeron utilizando *Docker-Compose*, que facilita su creación e interconectividad en solo un archivo *.YAML* y permite la ejecución de los contenedores en simultáneo.

Finalmente, se ejecutaron ciertas *SQL* queries para obtener información del dataset utilizando el apartado *Query* en pgAdmin web UI. 

<br>

### ETL Pipeline B- GCS Bucket (*etl_project/gcs_db/*)

<picture>
<source media= "(prefers-color-scheme: light)" srcset= "https://github.com/diegos41/repo_diplo_datos/blob/main/images/pipeline_etl_2.png">
<img alt= "This is the picture for etl pipeline B.">
</picture>

En este caso se extraerá el archivo *CSV* del mes de noviembre de 2020 para el servicio **green taxi**. 

Es un excelente ejemplo de reproducibilidad y trabajo colaborativo, ya que el script es tomado desde un repositorio en *GitHub* y es ejecutado en un contenedor de Docker (usando una imagen de *DockerHub*), aislando por completo al computador local que se utilice. 

Prefect se basa en Python y divide el proceso ETL en *Tasks* y *Flow*. Es bastante intuitivo y permite organizar cada procedimiento. 
También permite programar los deployments tanto desde la terminal como desde la Prefect UI en el puerto 4200. Una vez que el deployment 'se activa', empieza a correr lo que se llama *Job*, donde se encuentra el script. 

Finalmente, el dataset es subido a un Bucket de *Google Cloud Storage*. En este caso, Prefect se encarga del manejo de la Google API ya que solo hay que agregar lo que le llaman *GcsBucket Block* al script y listo.

<br>

# Anexo: Ingestion script

Por último, incluyo una forma alternativa de ingerir los datos, creando un script ejecutable directamente desde la *CLI*. El mismo se encuentra en ***shell_script/***.


