## Setup
```
CREATE OR REPLACE EXTERNAL TABLE `cedar-abacus-375916.dezoomcampeu.yellow_tripdata`
OPTIONS (
    format = 'CSV',
    uris = ['gs://prefect-de-zoomcamp-vy-2023/data/yellow/yellow_tripdata_*.csv.gz']   
);
```
Same for fhv and green


### Question 1
```
What is the count of records in the model fact_trips after running all models with the test run variable disabled and filtering for 2019 and 2020 data only (pickup datetime)?
```

Answer: `Number of rows 61,604,282`


### Question 2
```
What is the distribution between service type filtering by years 2019 and 2020 data as done in the videos?
```

Answer: `89.8/10.2`

### Question 3
```
What is the count of records in the model stg_fhv_tripdata after running all models with the test run variable disabled (:false)?
```

Answer: `43244696`

### Question 4
```
What is the count of records in the model fact_fhv_trips after running all dependencies with the test run variable disabled (:false)?
```

Answer: `22998722`
