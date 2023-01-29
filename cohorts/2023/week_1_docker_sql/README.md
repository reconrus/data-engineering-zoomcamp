### Start PG

```
mkdir data
mkdir data/ny_taxi_postgres_data
mkdir data/pgadmin
sudo chown 5050:5050 data/pgadmin
sudo chmod a+rwx data/ny_taxi_postgres_data
```

`docker compose up -d`

### Ingest Data

`docker build -t taxi_ingest:v001 .`

```
URL="https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_2019-01.csv.gz"

docker run -it \
  --network=week_1_docker_sql_pgnetwork \
  taxi_ingest:v001 \
    --user=root \
    --password=root \
    --host=pgdatabase \
    --port=5432 \
    --db=ny_taxi \
    --table_name=yellow_taxi_trips \
    --url=${URL}
```

Comment lines with `lpep`, rebuild and run
```
docker run -it   --network=week_1_docker_sql_pgnetwork   taxi_ingest:v001     --user=root     --password=root     --host=pgdatabase     --port=5432     --db=ny_taxi     --table_name=taxi_zone_lookup     --url=${URL}
```


### SQL Queries
#### Question 3. Count records
```
SELECT count(*) FROM public.yellow_taxi_trips
WHERE lpep_pickup_datetime::date = to_date('2019-01-15', 'YYYY-MM-dd')
  and lpep_dropoff_datetime::date = to_date('2019-01-15', 'YYYY-MM-dd')
```
Answer: `20530`


#### Question 4. Largest trip for each day
Assuming the `trip_distance` is indexed :)
```
SELECT lpep_pickup_datetime::date FROM public.yellow_taxi_trips
ORDER BY trip_distance DESC
LIMIT 1
```

Answer: `2019-01-15`

#### Question 5. The number of passengers
```
SELECT count(*) FROM public.yellow_taxi_trips
WHERE lpep_pickup_datetime::date = to_date('2019-01-01', 'YYYY-MM-dd')
  and (passenger_count = 2 or passenger_count = 3)
GROUP BY passenger_count
ORDER BY passenger_count
```

Answer: ```
1282
254
```

#### Question 6. Largest tip

```
SELECT tzl."Zone"
FROM ( 
	SELECT *
	FROM 
		public.yellow_taxi_trips
	INNER JOIN
		public.taxi_zone_lookup
		ON "PULocationID" = "LocationID"
	WHERE
		"Zone" = 'Astoria'
) puzone
LEFT JOIN 
	public.taxi_zone_lookup tzl
	ON puzone."DOLocationID" = tzl."LocationID"
ORDER BY tip_amount DESC
LIMIT 1
```

Answer: `Long Island City/Queens Plaza`
