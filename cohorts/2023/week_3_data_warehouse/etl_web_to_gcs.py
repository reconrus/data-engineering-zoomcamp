#!/usr/bin/env python
# coding: utf-8

import requests
from prefect import flow, task
from prefect.filesystems import GCS


@task(retries=3)
def fetch(dataset_url: str) -> bytes:
    """Read taxi data from web into pandas DataFrame"""
    response = requests.get(dataset_url)
    print(f'Downloaded {dataset_url}')
    return response.content


@task()
def write_gcs(path: str, content: bytes) -> None:
    """Upload local parquet file to GCS"""
    gcs_block = GCS.load("zoom-gcs")
    gcs_block.write_path(path=path, content=content)
    print(f'Put to {path}')
    return


@flow()
def etl_web_to_gcs(year: int, month: int, color: str) -> None:
    """The main ETL function"""
    dataset_file = f"{color}_tripdata_{year}-{month:02}"
    dataset_url = f"https://github.com/DataTalksClub/nyc-tlc-data/releases/download/{color}/{dataset_file}.csv.gz"
    content = fetch(dataset_url)
    path = f"data/{color}/{dataset_file}.csv.gz"
    write_gcs(path, content)


@flow()
def etl_parent_flow(
    months: list[int], year: int, color: str
):
    for month in months:
        etl_web_to_gcs(year, month, color)


if __name__ == "__main__":
    color = "fhv"
    year = 2019
    months = list(range(1, 13))
    etl_parent_flow(months, year, color)
