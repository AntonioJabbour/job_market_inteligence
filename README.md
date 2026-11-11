# Job Market Intelligence

**End-to-end analytics pipeline that turns raw Data & AI job postings into clean, BI-ready tables of roles and skills.**

![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?logo=postgresql&logoColor=white)
![pandas](https://img.shields.io/badge/pandas-150458?logo=pandas&logoColor=white)
![Power BI](https://img.shields.io/badge/Power%20BI-F2C811?logo=powerbi&logoColor=black)

Job postings are collected from the JSearch API, loaded into PostgreSQL, cleaned and standardized with SQL, and analyzed in Python. The output is a related **jobs** and **skills** table pair ready for Power BI.

## Key results

| Metric | Result |
|---|---:|
| Job postings analyzed | **1,044** |
| Standardized role categories | **9** |
| Job–skill records prepared for Power BI | **5,865** |
| Postings matched to at least one programming language | **793 (76%)** |
| Largest role category in the sample | AI Engineer (224 postings) |
| Postings flagged remote | 49 (4.7%) |

**Data quality findings:** 94% of postings had no city-level location, 30% had no posting timestamp, and 6% had no country. These gaps are documented so that country and time filters in reports can account for them rather than silently dropping records.

## Business questions

- Which technical skills are most often mentioned for each data role?
- How do role mix and remote availability vary across the sample?
- Which data quality issues could distort comparisons, and how should a report handle them?
- How should job and skill data be modeled for interactive reporting?

## Pipeline

```
JSearch API ──► PostgreSQL (raw) ──► SQL cleaning & title mapping ──► Python EDA & skill extraction ──► Power BI tables
```

1. **Collect:** Python API client with ingestion into PostgreSQL ([`src/data/`](src/data)).
2. **Clean:** SQL normalizes text and maps free-text job titles to 9 standard roles ([`sql/cleaning/`](sql/cleaning)), followed by validation queries ([`sql/validation/`](sql/validation)).
3. **Analyze:** Data quality checks plus regex/dictionary skill extraction across 8 skill categories ([EDA notebook](notebooks/01_initial_eda.ipynb)).
4. **Model for BI:** One-to-many jobs → skills tables with relationship checks ([Power BI prep notebook](notebooks/02_powerbi_preparation.ipynb)).

## Explore it in 2 minutes (no API key needed)

The processed outputs are included:

- [`notebooks/jobs_table.csv`](notebooks/jobs_table.csv): one row per job
- [`notebooks/skills_table.csv`](notebooks/skills_table.csv): one row per job–skill mention
- [`notebooks/processed_job_data.csv`](notebooks/processed_job_data.csv): full cleaned dataset

**Power BI:** import both tables and relate `jobs_table[job_id]` → `skills_table[job_id]` (one-to-many). Use `DISTINCTCOUNT(job_id)` for job-level measures, because counting skill rows would inflate posting counts. Measure definitions and DAX examples are in the [data dictionary](docs/data_dictionary.md).

To rerun the full pipeline (API key and PostgreSQL required), follow the [setup guide](docs/getting_started.md). Credentials go in a local `.env` file, which is git-ignored.

## Repository structure

| Path | Purpose |
|---|---|
| `src/data/` | API client, database access, ingestion, SQL runner |
| `sql/exploration/` · `sql/cleaning/` · `sql/validation/` | Profiling, cleaning and validation queries |
| `notebooks/` | EDA, Power BI preparation, CSV exports |
| `docs/` | Setup guide, data dictionary, schema design, data quality report |
| `tests/` | Manual API and database checks |

## Limitations & next steps

- The sample reflects API search queries and collection timing, not the full job market, so results describe the sample rather than overall hiring demand.
- Dictionary matching captures skill *mentions*, not verified requirements; extraction accuracy still needs a manual audit.
- Next: stable source IDs and deduplication on ingestion, an extraction-quality audit, and a published Power BI dashboard.

## Author

**Antonio Jabbour**, Data Analyst · [GitHub](https://github.com/AntonioJabbour)
