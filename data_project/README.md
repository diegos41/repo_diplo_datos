## ETL Pipelines (*etl_project/*)

### ETL Pipeline A- Local DataBase (*etl_project/local_db/*)

<picture>
<source media= "(prefers-color-scheme: light)" srcset= "https://github.com/diegos41/repo_diplo_datos/blob/main/images/pipeline_etl_1.png">
<img alt= "This is the picture for etl pipeline A.">
</picture>

Esta pipeline ingiere el archivo *CSV* correspondiente al servicio **green taxi**, en el mes de enero de 2019.

El script se corre en un contenedor de Docker y efectúa mayoritariamente los procesos de extracción, transformación y carga de *data*. Cabe destacar el uso de *Pandas* (no solo aquí si no a lo largo de todos los projectos) para la transformación de *datatypes*, como así también la creación de una tabla en *PostgreSQL*. 

Los servicios utilizados se construyeron utilizando *Docker-Compose*, que facilita su creación e interconectividad en solo un archivo *.YAML* y permite la ejecución de los contenedores en simultáneo.

Finalmente, se ejecutaron ciertas *SQL* queries para obtener información del dataset utilizando el apartado *Query* en pgAdmin web UI. 

<br>

### ETL Pipeline B- GCS Bucket (*etl_project/gcs_db/*)

<picture>
<source media= "(prefers-color-scheme: light)" srcset= "https://github.com/diegos41/repo_diplo_datos/blob/main/images/pipeline_etl_2.png">
<img alt= "This is the picture for etl pipeline B.">
</picture>