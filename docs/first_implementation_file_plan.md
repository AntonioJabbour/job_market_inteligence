# First Implementation File Plan

## 1. Purpose

The purpose of this document is to define the first set of Python files needed to implement the initial ingestion pipeline for the AI-Powered Job Market Intelligence Platform.

These files should provide a clean separation of concerns so that API access, database connection, ingestion logic, and utility functions remain modular and maintainable.

The first implementation should focus only on the raw ingestion flow:

JSearch API → Python pipeline → PostgreSQL raw_job_postings table

---

## 2. Initial Files to Create

The first implementation should include the following files:

- `src/data/ingest_jobs.py`
- `src/data/jsearch_client.py`
- `src/data/db.py`
- `src/utils/logger.py`
- `src/utils/helpers.py`

These files are enough for the first end-to-end ingestion workflow.

---

## 3. File Responsibilities

### `src/data/ingest_jobs.py`

This file should act as the main entry point for the ingestion process.

Its responsibilities should include:

- loading environment variables
- starting the ingestion run
- defining the initial search parameters
- calling the JSearch API client
- calling the database insertion logic
- logging the ingestion summary
- handling the first end-to-end workflow

This should be the first script you run manually during development.

---

### `src/data/jsearch_client.py`

This file should be responsible for all interactions with the JSearch API.

Its responsibilities should include:

- building request headers
- building request parameters
- sending API requests
- validating API responses
- extracting job posting records from the response
- returning structured results to the ingestion pipeline

This keeps the API-specific logic isolated from the rest of the project.

---

### `src/data/db.py`

This file should be responsible for database connectivity and database operations related to raw ingestion.

Its responsibilities should include:

- establishing PostgreSQL connections
- creating the `raw_job_postings` table if needed
- inserting records into the raw table
- running simple validation queries after insertion

This separates database logic from ingestion orchestration.

---

### `src/utils/logger.py`

This file should centralize logging behavior for the project.

Its responsibilities should include:

- defining logging format
- setting logging level
- creating reusable project loggers
- ensuring that ingestion events are consistently logged

This will make the pipeline easier to debug and monitor.

---

### `src/utils/helpers.py`

This file should contain small reusable helper functions that do not belong directly to the API or database layers.

Possible responsibilities include:

- timestamp generation
- safe value extraction
- field cleaning helpers
- simple normalization helpers used during raw ingestion

This avoids cluttering the main pipeline script.

---

## 4. Optional Files for Later

These files are not required for the first ingestion run, but may be added soon after:

- `src/data/schema.sql`
- `src/data/validate_ingestion.py`
- `tests/test_jsearch_client.py`
- `tests/test_db.py`

These will become more useful after the first end-to-end ingestion run works.

---

## 5. Execution Order

The expected implementation flow should be:

1. define logging setup
2. define database connection utilities
3. define JSearch API client
4. define ingestion orchestration script
5. run the first ingestion for one role and one country
6. inspect the inserted records in PostgreSQL

This order reduces confusion because each layer depends on the previous one.

---

## 6. First Manual Run Target

The first manual pipeline execution should aim to:

- search for `data scientist`
- use country = `us`
- request page `1`
- insert the returned records into `raw_job_postings`
- confirm that the data exists in PostgreSQL

The first run should prioritize correctness over complexity.

---

## 7. Design Principles for the First Implementation

The first implementation should follow these principles:

1. keep the logic simple
2. avoid premature optimization
3. separate API logic from database logic
4. make logging clear and readable
5. preserve raw data for traceability
6. design for future expansion to multiple roles and countries

These principles will help keep the project maintainable as it grows.

---

## 8. Expected Outcome

At the end of the first implementation phase, the project should have a minimal but complete ingestion pipeline structure with clearly defined Python files.

This structure will support the first successful ingestion run and prepare the project for the next phase: database validation and raw data inspection.