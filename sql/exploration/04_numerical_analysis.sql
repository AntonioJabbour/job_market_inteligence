-- Salary min/max/avg analysis
SELECT
    MIN(salary_min) AS min_salary_min,
    MAX(salary_min) AS max_salary_min,
    AVG(salary_min) AS avg_salary_min,
    MIN(salary_max) AS min_salary_max,
    MAX(salary_max) AS max_salary_max,
    AVG(salary_max) AS avg_salary_max
FROM raw_job_postings;

-- Count missing salary values
SELECT
    COUNT(*) FILTER (WHERE salary_min IS NULL) AS salary_min_nulls,
    COUNT(*) FILTER (WHERE salary_max IS NULL) AS salary_max_nulls,
    COUNT(*) FILTER (WHERE salary_currency IS NULL) AS salary_currency_nulls,
    COUNT(*) FILTER (WHERE salary_period IS NULL) AS salary_period_nulls
FROM raw_job_postings;