# Ingestion Pipeline Design

## 1. Purpose

The purpose of the first ingestion pipeline is to collect live job postings from the JSearch API and load them into the PostgreSQL database.

This first version is focused on correctness, reproducibility, and clarity rather than scale. The pipeline should successfully retrieve job postings for selected roles and geographic regions, map the API response into the raw schema, and insert the records into the `raw_job_postings` table.

---

## 2. First Pipeline Scope

The first version of the ingestion pipeline will:

- connect to the JSearch API
- retrieve job postings for a single role in a single country
- parse the API response
- map the required fields
- insert the records into PostgreSQL
- log ingestion results
- preserve the original API payload

To keep the first run simple, the initial test case should use:

- role: `Data Scientist`
- country: `us`
- page: `1`
- num_pages: `1`

This limited scope makes debugging easier before expanding to more roles and countries.

---

## 3. Initial Search Parameters

The first ingestion run should use the following initial search settings:

- query = `data scientist`
- country = `us`
- page = `1`
- num_pages = `1`
- date_posted = `all`

Later runs can expand to additional roles, pages, and countries once the initial ingestion is validated.

---

## 4. Pipeline Workflow

The first ingestion workflow should follow these steps:

1. load environment variables
2. establish database connection
3. construct API request parameters
4. send request to the JSearch API
5. validate response status
6. extract job records from the response payload
7. map selected fields to the raw schema
8. attach metadata such as:
   - search query
   - ingestion timestamp
   - raw JSON payload
9. insert records into the `raw_job_postings` table
10. log the number of records inserted
11. perform a basic post-ingestion validation query

This workflow should be implemented clearly so that it can later be reused in larger ingestion runs.

---

## 5. Fields to Map During Ingestion

The first ingestion pipeline should map the following API fields into the raw database table:

- source_job_id
- search_query
- job_title
- company_name
- company_website
- job_city
- job_state
- job_country
- employment_type
- is_remote
- posted_at_utc
- apply_link
- job_description
- salary_min
- salary_max
- salary_currency
- salary_period
- job_source
- api_response_json
- ingested_at

This mapping should be kept simple and explicit in the first version.

---

## 6. First Success Criteria

The first ingestion pipeline will be considered successful if it can:

- authenticate with the JSearch API
- retrieve at least one page of job postings
- connect to PostgreSQL successfully
- insert the records into `raw_job_postings`
- preserve the raw JSON response for each record
- log the ingestion result without crashing

The objective of the first run is not large-scale ingestion, but a reliable end-to-end proof of concept.

---

## 7. Initial Failure Cases to Watch

The pipeline should be designed while keeping these possible failure cases in mind:

- invalid or expired API key
- empty API response
- missing expected fields in the response
- database connection failure
- insertion errors due to nulls or type mismatch
- duplicate job postings
- API rate limit issues

These should be handled later through validation, logging, and retry logic.

---

## 8. Logging Expectations

At minimum, the first version of the pipeline should log:

- start of ingestion run
- search query used
- country used
- API request status
- number of records returned
- number of records inserted
- any failed records
- end of ingestion run

These logs will make debugging much easier during development.

---

## 9. Future Pipeline Expansion

After the first ingestion run is validated, the pipeline can be expanded to support:

- multiple job roles
- multiple countries
- multiple pages per run
- scheduled ingestion
- duplicate handling during insert
- incremental loading
- ingestion statistics tables

This phased approach reduces risk and makes the system easier to test.

---

## 10. Expected Outcome

At the end of this step, the project should have a clearly defined ingestion workflow that can be implemented in Python to fetch real job postings from the JSearch API and store them in PostgreSQL.

This will be the first fully connected data pipeline in the project and will serve as the foundation for cleaning, NLP, modeling, and dashboard development.