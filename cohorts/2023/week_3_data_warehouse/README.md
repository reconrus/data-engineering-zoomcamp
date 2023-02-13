### Setup
1. `prefect config set PREFECT_API_URL=https://api.prefect.cloud/api/accounts/[account_id]/workspaces/[workspace_id]`
2. `python3 etl_web_to_gcs.py`
3. ```
    CREATE OR REPLACE EXTERNAL TABLE `cedar-abacus-375916.dezoomcampeu.fhv`
    OPTIONS (
        format = 'CSV',
        uris = ['gs://prefect-de-zoomcamp-vy-2023/data/fhv/fhv_tripdata_2019-*.csv.gz']   
    );

    CREATE OR REPLACE TABLE cedar-abacus-375916.dezoomcampeu.fhv_non_partitoned AS
    SELECT * FROM cedar-abacus-375916.dezoomcampeu.fhv;
    ```

### Question 1
What is the count for fhv vehicle records for year 2019?

```
SELECT count(*) FROM `cedar-abacus-375916.dezoomcampeu.fhv`
```

Answer: `43244696`

### Question 2
Write a query to count the distinct number of affiliated_base_number for the entire dataset on both the tables.
What is the estimated amount of data that will be read when this query is executed on the External Table and the Table?

External:
```
SELECT count(distinct(affiliated_base_number)) FROM `cedar-abacus-375916.dezoomcampeu.fhv`;
```
Answer:
```
Bytes processed
2.52 GB
Bytes billed
2.52 GB
```

Internal:
```
SELECT count(distinct(affiliated_base_number)) FROM `cedar-abacus-375916.dezoomcampeu.fhv_non_partitoned`;
```

Answer:
```
Bytes processed
317.94 MB
Bytes billed
318 MB
```

### Question 3
How many records have both a blank (null) PUlocationID and DOlocationID in the entire dataset?

```
SELECT count(*) FROM `cedar-abacus-375916.dezoomcampeu.fhv_non_partitoned`
WHERE PUlocationID is null AND DOlocationID is null
```

Answer: `717748`

### Question 4
What is the best strategy to optimize the table if query always filter by pickup_datetime and order by affiliated_base_number?

`Partition by pickup_datetime Cluster on affiliated_base_number`

### Question 5
Implement the optimized solution you chose for question 4. Write a query to retrieve the distinct affiliated_base_number between pickup_datetime 2019/03/01 and 2019/03/31 (inclusive).
Use the BQ table you created earlier in your from clause and note the estimated bytes. Now change the table in the from clause to the partitioned table you created for question 4 and note the estimated bytes processed. What are these values? Choose the answer which most closely matches.

Non-partitioned
```
SELECT count(distinct(affiliated_base_number)) FROM `cedar-abacus-375916.dezoomcampeu.fhv_non_partitoned`
WHERE pickup_datetime BETWEEN '2019-03-01' AND '2019-03-31'
```

Answer:
```
Bytes processed
647.87 MB
Bytes billed
648 MB
```

Partitioned:
```
CREATE OR REPLACE TABLE `cedar-abacus-375916.dezoomcampeu.fhv_partitoned`
PARTITION BY DATE(pickup_datetime)
CLUSTER BY affiliated_base_number AS (
  SELECT * FROM `cedar-abacus-375916.dezoomcampeu.fhv_non_partitoned`
);

SELECT count(distinct(affiliated_base_number)) FROM `cedar-abacus-375916.dezoomcampeu.fhv_partitoned`
WHERE pickup_datetime BETWEEN '2019-03-01' AND '2019-03-31'
```

Answer:
```
Bytes processed
23.05 MB
Bytes billed
24 MB
```

### Question 6
Where is the data stored in the External Table you created?

Answer: `GCP Bucket`

### Question 7
It is best practice in Big Query to always cluster your data:

Answer: `False`

