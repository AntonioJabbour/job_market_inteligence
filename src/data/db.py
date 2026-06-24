import os
import psycopg2
import json
from datetime import datetime, timezone
from psycopg2.extras import Json
from dotenv import load_dotenv
from src.utils.logger import get_logger

#to load the environment where the variable of the database is saved
load_dotenv()

logger = get_logger(__name__)


def get_db_connection():
    """
    Establish a connection to the PostgreSQL database
    using environment variables.
    """

    logger.info("Connecting to PostgreSQL")

    try:
        conn = psycopg2.connect(
            host=os.getenv("DB_HOST"),
            port=int(os.getenv("DB_PORT")),
            dbname=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD")
        )

        logger.info("PostgreSQL connection established")
        return conn

    except Exception as e:
        logger.error(f"Failed to connect to PostgreSQL: {e}")
        raise

def create_raw_table(conn):
    logger.info("Creating the table")

    try:
        create_table = """
            CREATE TABLE IF NOT EXISTS raw_job_postings (
                id BIGSERIAL PRIMARY KEY,
                source_job_id TEXT,
                search_query TEXT,
                job_title TEXT,
                company_name TEXT,
                company_website TEXT,
                job_city TEXT,
                job_state TEXT,
                job_country TEXT,
                job_location TEXT,
                employment_type TEXT,
                is_remote BOOLEAN,
                posted_at_utc TIMESTAMPTZ,
                apply_link TEXT,
                job_description TEXT,
                salary_min NUMERIC,
                salary_max NUMERIC,
                salary_currency TEXT,
                salary_period TEXT,
                job_source TEXT,
                api_response_json JSONB,
                ingested_at TIMESTAMPTZ
            );
            """    
        
        cursor = conn.cursor()
        cursor.execute(create_table)
        logger.info("Table created successfully")
        conn.commit()
        cursor.close()

    except Exception as e:
        logger.error(f"Failed to create the table: {e}")
        raise

def insert_jobs(conn, jobs, search_query):

    logger.info("Starting job insertion into raw_job_postings...")

    insert_query = """
        INSERT INTO raw_job_postings (
            source_job_id,
            search_query,
            job_title,
            company_name,
            company_website,
            job_city,
            job_state,
            job_country,
            job_location,
            employment_type,
            is_remote,
            posted_at_utc,
            apply_link,
            job_description,
            salary_min,
            salary_max,
            salary_currency,
            salary_period,
            job_source,
            api_response_json,
            ingested_at
        )
        VALUES (
            %s, %s, %s, %s, %s,
            %s, %s, %s, %s, %s,
            %s, %s, %s, %s, %s,
            %s, %s, %s, %s, %s,
            %s
        );
    """

    try:
        with conn.cursor() as cursor:
            for job in jobs:
                ingested_at = datetime.now(timezone.utc)

                values = (
                    job.get("job_id"),                         
                    search_query,                              
                    job.get("job_title"),                      
                    job.get("employer_name"),                
                    job.get("employer_website"),             
                    job.get("job_city"),                       
                    job.get("job_state"),                      
                    job.get("job_country"),    
                    job.get("job_location"),               
                    job.get("job_employment_type"),           
                    job.get("job_is_remote"),                  
                    job.get("job_posted_at_datetime_utc"),     
                    job.get("job_apply_link"),                
                    job.get("job_description"),           
                    job.get("job_min_salary"),                 
                    job.get("job_max_salary"),                
                    None,                                      
                    job.get("job_salary_period"),              
                    job.get("job_publisher"),                  
                    Json(job),                                 
                    ingested_at                            
                )

                cursor.execute(insert_query, values)

        conn.commit()
        logger.info(f"Successfully inserted {len(jobs)} job(s) into raw_job_postings_new.")

    except Exception as e:
        conn.rollback()
        logger.error(f"Error inserting jobs into raw_job_postings: {e}")
        raise