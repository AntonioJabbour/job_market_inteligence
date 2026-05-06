-- Compare row counts between raw and first cleaned table
SELECT 'raw_job_postings' AS table_name, COUNT(*) AS row_count
FROM raw_job_postings

UNION ALL

SELECT 'clean_job_posting' AS table_name, COUNT(*) AS row_count
FROM clean_job_posting;

-- Validate cleaned job title distribution
SELECT 
    COUNT(*) AS job_count,
    clean_job_title
FROM clean_job_posting
GROUP BY clean_job_title
ORDER BY job_count DESC;