-- Check missing or empty job descriptions
SELECT COUNT(*) AS missing_or_empty_descriptions
FROM raw_job_postings
WHERE job_description IS NULL
   OR TRIM(job_description) = '';

-- Analyze job description length
SELECT  
    MIN(LENGTH(job_description)) AS min_length,
    AVG(LENGTH(job_description)) AS avg_length,
    MAX(LENGTH(job_description)) AS max_length
FROM raw_job_postings;