from prefect import flow

from etl_gcs_to_bq import etl_gcs_to_bq
from etl_web_to_gcs import etl_web_to_gcs


@flow()
def etl_parent_flow(
    months: list[int], year: int, color: str
):
    rows_inserted_count = 0
    for month in months:
        etl_web_to_gcs(year, month, color)
        rows_inserted_count += etl_gcs_to_bq(year, month, color)
    print(f'Loaded {rows_inserted_count} rows for year {year}, months {months}, color `{color}`')


if __name__ == "__main__":
    color = "yellow"
    months = [2, 3]
    year = 2019
    etl_parent_flow(months, year, color)
