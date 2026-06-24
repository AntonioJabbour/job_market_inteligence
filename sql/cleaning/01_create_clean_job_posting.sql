-- Create first cleaned table
DROP TABLE IF EXISTS clean_job_posting;

CREATE TABLE clean_job_posting AS
SELECT 
    job_title,
    TRIM(LOWER(job_title)) AS clean_job_title,
    TRIM(company_name) AS company_name,
    TRIM(job_country) AS job_country,
    TRIM(job_location) AS job_location,
    TRIM(LOWER(employment_type)) AS employment_type,
    is_remote,
    job_description,
    TRIM(LOWER(job_source)) AS job_source,
    posted_at_utc
FROM raw_job_postings;