-- Check NULL count for every column in raw_job_postings
SELECT
    c.column_name,
    (
        SELECT COUNT(*)
        FROM raw_job_postings r
        WHERE to_jsonb(r) ->> c.column_name IS NULL
    ) AS null_count
FROM information_schema.columns c
WHERE c.table_name = 'raw_job_postings'
ORDER BY null_count DESC;