# Data Acquisition Plan

## 1. Objective

The project will collect modern job posting data using the JSearch API. The goal of the acquisition step is to retrieve structured job listings related to Data Science and store them in a PostgreSQL database for downstream analysis, preprocessing, NLP, and machine learning tasks.

The first version of the pipeline will focus on roles such as Data Scientist, Data Analyst, Machine Learning Engineer, Analytics Engineer, Business Intelligence Analyst, and AI Engineer.

---

## 2. Initial Target Roles

The initial data collection phase will focus on the following job roles:

- Data Scientist
- Data Analyst
- Machine Learning Engineer
- Analytics Engineer
- Business Intelligence Analyst
- AI Engineer

These roles were selected because they are highly relevant to the project objective and contain overlapping but distinct skill requirements that are useful for salary analysis, skill extraction, and clustering.

---

## 3. Geographic Scope

The initial version of the project will collect job postings from a limited geographic scope to keep the ingestion pipeline manageable and to reduce noise in salary and market comparisons.

Recommended initial scope:

North America
- United States

Europe
- United Kingdom

Middle East (Gulf Region)
- United Arab Emirates
- Saudi Arabia
- Qatar
- Kuwait

Remote Roles
- Global remote positions when available

This scope can be expanded later after the first version of the pipeline is stable.

---

## 4. Initial Fields to Collect

The first ingestion version should collect the following fields from the API response whenever available:

- job_id
- job_title
- employer_name
- employer_website
- job_city
- job_state
- job_country
- job_employment_type
- job_is_remote
- job_posted_at_datetime_utc
- job_apply_link
- job_description
- job_min_salary
- job_max_salary
- job_salary_currency
- job_salary_period
- job_source
- search_query

These fields are sufficient for the first phase of database ingestion and later preprocessing.

---

## 5. Environment Variables

Sensitive credentials and configuration values will be stored in a `.env` file and exposed through an `.env.example` template.

Planned environment variables:

- JSEARCH_API_KEY
- DB_HOST
- DB_PORT
- DB_NAME
- DB_USER
- DB_PASSWORD

---

## 6. Initial Database Target

The first version of the pipeline will load API results into a PostgreSQL table named:

- raw_job_postings

This table will act as the landing zone for raw ingested records before cleaning and transformation.

Later stages may introduce additional tables such as:

- cleaned_job_postings
- extracted_skills
- model_features

---

## 7. First Acquisition Milestone

The first milestone of data acquisition is to successfully:

1. connect to the JSearch API
2. retrieve job postings for one role, starting with "Data Scientist"
3. store the returned records in PostgreSQL
4. verify that the expected fields are populated
5. inspect the raw data quality

The initial objective is not scale, but correctness and reproducibility.

---

## 8. Initial Data Quality Checks

After the first ingestion run, the following checks should be performed:

- confirm records were inserted successfully
- inspect missing values
- inspect duplicate job postings
- check salary field availability
- verify that job descriptions are present
- verify that posting dates are correctly captured
- confirm the search query used to retrieve the records