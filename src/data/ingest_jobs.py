from dotenv import load_dotenv
from src.utils.logger import get_logger
from src.data.jsearch_client import fetch_jobs_from_api
from src.data.db import get_db_connection, create_raw_table, insert_jobs

load_dotenv()

logger = get_logger(__name__)


def initialize_workflow(roles, countries, page, num_pages):
    conn = None

    try:
        logger.info("Connect to the Database")
        conn = get_db_connection()
        logger.info("Connected Successfully")

        logger.info("Creating the table")
        create_raw_table(conn)
        logger.info("Created Successfully")

        for role in roles:
            for country in countries:
                search_query = f"{role} in {country}"
                logger.info(f"Processing query: {search_query}")

                try:
                    jobs = fetch_jobs_from_api(search_query, page, num_pages)

                    if not jobs:
                        logger.warning(f"No jobs returned for query: {search_query}")
                        continue

                    logger.info(f"Start inserting data for query: {search_query}")
                    insert_jobs(conn, jobs, search_query)
                    logger.info(f"Inserted successfully for query: {search_query}")

                except Exception as e:
                    logger.error(f"Error while processing query '{search_query}': {e}")
                    continue

    except Exception as e:
        logger.error(f"Workflow failed: {e}")

    finally:
        if conn:
            conn.close()
            logger.info("Connection closed")


if __name__ == "__main__":
    roles = [
        "Data Analyst",
        "Data Scientist",
        "Data Engineer",
        "Machine Learning Engineer",
        "AI Engineer",
        "Business Intelligence Analyst",
        "Analytics Engineer",
        "MLOps Engineer",
        "Data Architect"
    ]

    countries = [
        "USA",
        "Canada",
        "UK",
        "Germany",
        "France",
        "Netherlands",
        "India",
        "Singapore",
        "Australia",
        "Saudi Arabia",
        "Qatar",
        "Kuwait",
        "Bahrain",
        "Oman"
    ]

    page = 1
    num_pages = 3

    initialize_workflow(roles, countries, page, num_pages)
