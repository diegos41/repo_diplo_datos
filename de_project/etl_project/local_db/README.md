## Setup 

For building the Docker image you run `docker build -t g_taxi_ingest:v001 .`

Creating the db and creating a network with PgAdmin: `docker-compose up`

After that, use the following as the entrypoint for the ingestion script:
```shell
URL="https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_2019-01.csv.gz"

docker run -it \
  --network=homework_default \
  g_taxi_ingest:v001 \
    --user=root \
    --password=root \
    --host=pgdatabase\
    --port=5432 \
    --db=ny_green_taxi \
    --table_name=green_taxi_trips \
    --url=${URL}
```

Finally, run the desired queries using web UI on port 8080.

- **Note**: [Taxi ZoneLookup Table](https://d37ci6vzurychx.cloudfront.net/misc/taxi+_zone_lookup.csv) is mandatory for doing joins in some queries (check *sql_queries/**doff_zone_largest_tip.sql*** ).