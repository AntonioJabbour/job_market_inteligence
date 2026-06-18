-- Create standardized job title dataset
DROP TABLE IF EXISTS clean_job_posting_v2;

CREATE TABLE clean_job_posting_v2 AS
WITH matched_titles AS (
    SELECT
        c.*,
        m.standardized_job_title,
        m.pattern,
        m.priority,
        ROW_NUMBER() OVER (
            PARTITION BY c.clean_job_title, c.company_name, c.job_country, c.posted_at_utc
            ORDER BY m.priority ASC, LENGTH(m.pattern) DESC
        ) AS match_rank
    FROM clean_job_posting c
    JOIN job_title_mapping m
        ON c.clean_job_title LIKE '%' || m.pattern || '%'
)

SELECT
    standardized_job_title,
    clean_job_title,
    company_name,
    job_country,
    employment_type,
    is_remote,
    job_description,
    job_source,
    posted_at_utc
FROM matched_titles
WHERE match_rank = 1;