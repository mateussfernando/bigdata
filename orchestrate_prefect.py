from prefect import flow, task, get_run_logger
from dotenv import load_dotenv
from src.extract import Extract
from src.load import Load

load_dotenv()


@task(retries=3, retry_delay_seconds=10)
def extract(country: str) -> list[dict]:
    logger = get_run_logger()
    extractor = Extract()
    data = extractor.extract_data(country)
    logger.info(f"{len(data)} registros extraídos de {country}")
    return data


@task
def load_data(universities, db_name: str, collection_name: str):
    logger = get_run_logger()
    loader = Load()
    loader.load_data_atlas(universities, db_name, collection_name)
    logger.info(f"{len(universities)} registros inseridos em {db_name}.{collection_name}")


@flow(name="ETL Universities Prefect", log_prints=True)
def etl_universities_flow(country: str = "Brazil"):
    data = extract(country)
    load_data(data, "universidades", "universidades_brazil")


if __name__ == "__main__":
    etl_universities_flow()
