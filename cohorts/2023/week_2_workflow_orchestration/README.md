### Question 1. Load January 2020 data
1. `prefect orion start`
2. Go to Orion, add GCS Bucket (Block used to store data using GCP Cloud Storage Buckets.)
3. `python etl_web_to_gcs.py`

Answer: `447770`


### Question 2. Scheduling with Cron
1. `crontab -e`
2. add `0 5 1 * * root /root/data-engineering-zoomcamp/cohorts/2023/week_2_workflow_orchestration/etl_web_to_gcs.py`

Answer: `0 5 1 * *`


### Question 3. Loading data to BigQuery
1. `prefect deployment build ./full_run:etl_parent_flow -n "Parameterized Flow"`
2. `prefect deployment apply ./etl_parent_flow-deployment.yaml`
3. `prefect agent start -q 'default'`
4. Start the flow

Answer: `14851920`


### Question 4. Github Storage Block
1. move to the repo root
2. `prefect deployment build -n "github-flow" -sb github/zoom-github cohorts/2023/week_2_workflow_orchestration/etl_web_to_gcs.py:etl_web_to_gcs --apply`

Answer: `88605`


### Question 5. Email or Slack notifications
Answer: `514392`


### Question 6. Secrets
Answer: `8`
