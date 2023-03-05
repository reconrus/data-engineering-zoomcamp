### Question 1
```
Install Spark and PySpark

Install Spark
Run PySpark
Create a local spark session
Execute spark.version.

What's the output?
```

Answer: `3.3.2`


### Question 2
```
HVFHW June 2021

Read it with Spark using the same schema as we did in the lessons.
We will use this dataset for all the remaining questions.
Repartition it to 12 partitions and save it to parquet.
What is the average size of the Parquet (ending with .parquet extension) Files that were created (in MB)? Select the answer which most closely matches.
```

Answer: `~23.4MB`


### Question 3
```
Count records

How many taxi trips were there on June 15?

Consider only trips that started on June 15.
```

Answer: `452,470`


### Question 4
```
Longest trip for each day

Now calculate the duration for each trip.
How long was the longest trip in Hours?
```

Answer: `66.8788888888889 hours`


### Question 5
```
User Interface

Spark’s User Interface which shows application's dashboard runs on which local port?
```

Answer: `4040`


### Question 6
```
Most frequent pickup location zone

Load the zone lookup data into a temp view in Spark
Zone Data

Using the zone lookup data and the fhvhv June 2021 data, what is the name of the most frequent pickup location zone?
```

Answer: `Crown Heights North`
