-- Count rows in final standardized dataset
SELECT COUNT(*) AS final_row_count
FROM clean_job_posting_v2;

-- Validate standardized job title distribution
SELECT 
    COUNT(*) AS job_count,
    standardized_job_title
FROM clean_job_posting_v2
GROUP BY standardized_job_title
ORDER BY job_count DESC;