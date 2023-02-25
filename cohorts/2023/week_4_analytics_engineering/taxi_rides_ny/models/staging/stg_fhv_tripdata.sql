{{ config(materialized='view') }}

with tripdata as 
(
  select *
  from {{ source('staging','fhv_tripdata') }}
  where EXTRACT(YEAR FROM pickup_datetime) = 2019 
)
select
    cast(PUlocationID as integer) as  pickup_locationid,
    cast(DOlocationID as integer) as dropoff_locationid,
    
    cast(pickup_datetime as timestamp) as pickup_datetime,
    cast(dropOff_datetime as timestamp) as dropoff_datetime,
    
    cast(dispatching_base_num as string) as dispatching_base_num ,
    cast(SR_Flag as string) as sr_flag ,
    cast(Affiliated_base_number as string) as affiliated_base_number ,
from tripdata


-- dbt build --m <model.sql> --var 'is_test_run: false'
{% if var('is_test_run', default=true) %}

  limit 100

{% endif %}
