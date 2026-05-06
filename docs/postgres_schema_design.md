# PostgreSQL Schema Design

## 1. Database Choice

The project will use PostgreSQL as the primary database for storing job posting data collected from the JSearch API.

PostgreSQL is selected because it is reliable, production-oriented, supports strong SQL capabilities, integrates well with Python and SQLAlchemy, and can scale as the project grows.

---

## 2. Raw Table Purpose

The first database table will be named `raw_job_postings`.

This table will serve as the landing zone for raw job posting records collected directly from the JSearch API before any major cleaning, transformation, or feature engineering takes place.

The purpose of this table is to:

- preserve the original API response in structured form
- support reproducibility
- allow inspection of raw data quality
- serve as the source for downstream cleaning and modeling tables

---

## 3. Initial Table Columns

| Column Name | Data Type | Purpose |
|------|------|------|
| id   | BIGSERIAL PRIMARY KEY | Internal database identifier |
| source_job_id | TEXT | Original job identifier from API |
| search_query | TEXT | Search term used to retrieve the posting |
| job_title | TEXT | Job title |
| company_name | TEXT | Employer name |
| company_website | TEXT | Employer website |
| job_city | TEXT | City |
| job_state | TEXT | State or region |
| job_country | TEXT | Country |
| employment_type | TEXT | Employment type |
| is_remote | BOOLEAN | Remote flag |
| posted_at_utc | TIMESTAMP | Posting timestamp in UTC |
| apply_link | TEXT | Job application URL |
| job_description | TEXT | Full job description |
| salary_min | NUMERIC | Minimum salary |
| salary_max | NUMERIC | Maximum salary |
| salary_currency | TEXT | Salary currency |
| salary_period | TEXT | Salary period |
| job_source | TEXT | Source platform or provider |
| api_response_json | JSONB | Raw API payload for traceability |
| ingested_at | TIMESTAMP | Timestamp of ingestion |

---

## 4. Primary Key Strategy

The table will use an internal surrogate key:

- `id` as `BIGSERIAL PRIMARY KEY`

This is preferred because external job IDs from APIs may not always be globally unique or stable across sources.

The original API job identifier will still be stored separately in:

- `source_job_id`

This allows the pipeline to preserve source-level identity while keeping a reliable internal database key.

---

## 5. Deduplication Strategy

Duplicate job postings may appear because:

- the same query is run multiple times
- the same job appears across pages
- the API returns overlapping results

The first deduplication strategy will rely on a combination of fields such as:

- `source_job_id`
- `job_title`
- `company_name`
- `posted_at_utc`

If `source_job_id` is consistently available and reliable, it will become the main field used for deduplication. Otherwise, duplicate detection will use a composite matching strategy during the cleaning phase.

---

## 6. Initial Index Strategy

To support efficient querying, the following columns should be considered for indexing:

- `source_job_id`
- `job_title`
- `job_country`
- `posted_at_utc`
- `search_query`

These indexes will help with:

- duplicate checks
- filtering by role
- filtering by geography
- time-based analysis
- query tracking

---

## 7. JSON Storage Decision

In addition to storing selected structured fields, the project will store the original API response in a `JSONB` column named:

- `api_response_json`

This is useful because it:

- preserves the raw source data
- supports traceability
- allows recovery of fields not initially modeled
- makes schema evolution easier if new fields are needed later

---

## 8. Initial Load Strategy

The ingestion pipeline will first load records into the `raw_job_postings` table.

This load step should:

1. call the JSearch API
2. parse the response
3. map the required fields
4. insert records into PostgreSQL
5. capture ingestion timestamp
6. preserve the raw JSON payload

At this stage, the goal is raw ingestion correctness, not final cleaned analytics-ready structure.

---

## 9. Future Schema Extension

After the raw ingestion table is stable, the schema may be extended with additional tables such as:

- `cleaned_job_postings`
- `job_skills`
- `normalized_skills`
- `salary_features`
- `model_features`

This layered design will keep the raw source data separate from cleaned and engineered datasets.