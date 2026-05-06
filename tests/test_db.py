import os
from src.utils.logger import get_logger
from src.data.db import get_db_connection, create_raw_table, insert_jobs
from src.data.jsearch_client import fetch_jobs_from_api

logger = get_logger(__name__)

def test_db_connection():
    try:
        
        conn= get_db_connection()

        create_raw_table(conn)
        
        search_query = "Data Scientist"
        jobs = fetch_jobs_from_api(search_query)
        insert_jobs(conn, jobs, search_query)
        
        conn.close()
    except Exception as e:
        logger.error(f" failed: {e}")
        

if __name__ == "__main__":
    test_db_connection()
