-- Job title frequency before cleaning
SELECT 
    COUNT(*) AS job_count,
    job_title
FROM raw_job_postings
GROUP BY job_title
ORDER BY job_count DESC;

-- Compare original job title with normalized job title
SELECT 
    TRIM(LOWER(job_title)) AS normalized_job_title,
    job_title
FROM raw_job_postings;

-- Job title frequency after basic normalization
SELECT  
    COUNT(*) AS job_count,
    TRIM(LOWER(job_title)) AS normalized_job_title
FROM raw_job_postings
GROUP BY TRIM(LOWER(job_title))
ORDER BY job_count DESC;