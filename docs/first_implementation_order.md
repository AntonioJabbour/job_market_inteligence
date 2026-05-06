# First Implementation Order

## 1. Purpose

The purpose of this document is to define the correct implementation order for the first version of the ingestion pipeline.

The project should be built in small, testable steps so that each layer is verified before the next one is added. This reduces debugging complexity and makes the development process more reliable.

The first implementation goal remains:

JSearch API → Python ingestion pipeline → PostgreSQL `raw_job_postings`

---

## 2. Recommended Build Order

The first implementation should follow this order:

1. `src/utils/logger.py`
2. `src/data/db.py`
3. `src/data/jsearch_client.py`
4. `src/data/ingest_jobs.py`

This order is recommended because:

- logging is needed everywhere
- database connectivity should be validated early
- API client should be isolated and testable
- orchestration should be built only after the lower-level pieces exist

---

## 3. Step 1 — Implement Logging First

The first file to implement should be:

- `src/utils/logger.py`

This file should define the project logging behavior so that all later files can use consistent logs.

### What this file should do

- define a reusable logger
- use a readable log format
- respect the configured log level
- support console output for development

### What to verify before moving on

- the logger can be imported
- log messages appear correctly
- log level behavior works as expected

Logging should be working before writing database or API logic.

---

## 4. Step 2 — Implement Database Layer

The second file to implement should be:

- `src/data/db.py`

This file should establish the PostgreSQL connection and support raw table creation and insert operations.

### What this file should do

- load database configuration
- create database connection logic
- define raw table creation logic
- define insertion logic for raw job postings
- support a simple validation query

### What to verify before moving on

- the application can connect to PostgreSQL
- the `raw_job_postings` table can be created
- a test record can be inserted manually
- a simple query can confirm the inserted record exists

The database layer should work before connecting to the external API.

---

## 5. Step 3 — Implement API Client

The third file to implement should be:

- `src/data/jsearch_client.py`

This file should handle communication with the JSearch API.

### What this file should do

- load API key
- construct request headers
- construct query parameters
- send requests to the JSearch API
- validate the response
- extract job posting data from the response
- return structured records for ingestion

### What to verify before moving on

- the API key is loaded correctly
- the request succeeds for a basic query
- the response contains job records
- the returned records can be inspected in Python
- the client handles empty or failed responses safely

The API client should work independently before integrating with the database insert workflow.

---

## 6. Step 4 — Implement Ingestion Orchestration

The fourth file to implement should be:

- `src/data/ingest_jobs.py`

This file should orchestrate the end-to-end workflow.

### What this file should do

- initialize logging
- load environment variables
- define the first search query
- call the API client
- map records to the raw schema
- insert them into PostgreSQL
- log the final ingestion summary

### What to verify before considering Step 9 complete

- the script runs end to end
- job postings are fetched successfully
- records are inserted into `raw_job_postings`
- the inserted records can be queried in PostgreSQL
- logs clearly show what happened during the run

This is the first full pipeline milestone.

---

## 7. First Test Sequence

The first build-and-test sequence should be:

1. test logger output
2. test PostgreSQL connection
3. create `raw_job_postings`
4. insert one manual test row
5. test one API call for `data scientist`
6. inspect one sample API response
7. run the ingestion script
8. confirm real records exist in PostgreSQL

This sequence ensures that issues are found early and in the correct layer.

---

## 8. Scope Control

To avoid confusion, the first implementation should remain intentionally small.

### Do not add yet

- multiple roles
- multiple countries
- scheduling
- retry frameworks
- advanced deduplication
- full preprocessing
- dashboard integration

### Focus only on

- one role
- one country
- one page
- one table
- one successful end-to-end run

This small scope will make the first implementation much easier to debug.

---

## 9. Success Definition for This Phase

This implementation phase is successful when:

- the logger works
- the database connection works
- the raw table exists
- the JSearch API client works
- the ingestion script fetches real job postings
- those records are inserted into PostgreSQL
- the inserted data can be inspected manually

At that point, the project will have its first operational data pipeline.

---

## 10. Expected Outcome

At the end of this phase, the project will have a minimal but functioning ingestion architecture with a clear implementation sequence.

This will provide the foundation for the next phase, which is validating the raw data and preparing the first data inspection workflow.