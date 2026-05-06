-- Create standardized job title dataset
DROP TABLE IF EXISTS clean_job_posting_v2;

CREATE TABLE clean_job_posting_v2 AS
SELECT *
FROM (
    SELECT 
        CASE 
            WHEN clean_job_title LIKE '%data analyst%' 
              OR clean_job_title LIKE '%data analysis%' 
            THEN 'data analyst'

            WHEN clean_job_title LIKE '%data scientist%' 
              OR clean_job_title LIKE '%data science%' 
            THEN 'data scientist'

            ELSE NULL 
        END AS standardized_job_title,
        clean_job_title,
        company_name,
        job_country,
        employment_type,
        is_remote,
        job_description,
        job_source,
        posted_at_utc
    FROM clean_job_posting
) x
WHERE standardized_job_title IS NOT NULL;