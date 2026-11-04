# Job Market Intelligence

**A Data Analyst portfolio project using Python, PostgreSQL, and Power BI-ready data to explore skills mentioned in Data and AI job postings.**

The project turns API job listings into standardized roles, extracts technical terms from descriptions, and prepares related jobs and skills tables for business intelligence reporting.

## Business questions

- Which skills are mentioned in the collected postings?
- How do role counts and remote flags vary within the sample?
- Which data quality issues could affect comparisons?
- How can job and skill records be modeled for interactive reporting?

**Tools:** Python · SQL · PostgreSQL · pandas · regular expressions · scikit-learn · Power BI data preparation

## Start here

| Resource | What it shows |
|---|---|
| [Exploratory analysis](notebooks/01_initial_eda.ipynb) | Data quality checks, role and country counts, remote flags, and dictionary-based skill extraction |
| [Power BI preparation](notebooks/02_powerbi_preparation.ipynb) | Jobs and skills tables with relationship checks |
| [Setup guide](docs/getting_started.md) | Explore the included CSVs or run the database workflow |
| [Data dictionary and KPIs](docs/data_dictionary.md) | Table grain, relationships, field definitions, and reporting measures |
| [SQL cleaning](sql/cleaning) | Normalization and role standardization |
| [Original project definition](docs/project_definition.md) | Longer-term objectives, including features not yet delivered |

## Snapshot from saved analysis

These figures come from **saved notebook outputs**, not a fresh API collection or independent re-execution of the database pipeline.

| Measure | Saved result | Interpretation |
|---|---:|---|
| Analyzed job records | 1,044 | Size of the cleaned sample, not total market vacancies |
| Standardized role categories | 9 | Includes Data Analyst, Data Scientist, Data Engineer, and AI roles |
| Data Analyst records | 150 | Count within the sampled listings |
| AI Engineer records | 224 | Largest role category in this sample |
| Records flagged remote | 49 | About 4.69% of all 1,044 records; a false flag does not prove a role is on-site |
| Skill records prepared for Power BI | 5,865 | Job–skill–category records, not distinct jobs |
| Jobs with a programming-language dictionary match | 793 (75.96%) | Extraction coverage, not extraction accuracy |

**Business implication:** The sample can help prioritize a deeper review of skills for a chosen role. It cannot establish overall hiring demand or a market trend without representative sampling and comparable collection periods.

## Data quality findings

The saved EDA reports:

- **62 missing country values** (5.94%).
- **981 missing location values** (93.97%).
- **308 missing posting timestamps** (29.50%).
- **7 missing employment types** (0.67%).
- No full-row duplicates in the analyzed cleaned table.

Country and time filters therefore need explicit missing-data handling. The [initial raw-data quality report](docs/data_quality_report.md) also records unusable salary fields in that earlier assessment; salary benchmarking is not a demonstrated result of this version.

## Workflow and delivery status

1. **Collect:** JSearch client and PostgreSQL ingestion scripts.
2. **Clean:** SQL normalizes text and maps titles to role categories.
3. **Analyze:** The EDA notebook checks quality and extracts terms across eight skill categories.
4. **Prepare reporting:** The Power BI notebook exports jobs and skills tables.
5. **Explore modeling:** An older notebook compares job-role classifiers on a different, smaller dataset.

| Component | Current status |
|---|---|
| Python ingestion and SQL scripts | Included; require API access, PostgreSQL, and setup |
| Processed data and Power BI CSV exports | Included in `notebooks/` |
| Interactive Power BI report | No `.pbix` file or published dashboard is included |
| Machine-learning experiment | Legacy 54-record experiment; incompatible with the current extracted-column schema without adaptation |
| Salary prediction and role clustering | Longer-term objectives, not completed features demonstrated here |

## Explore without an API key

The included exports let you inspect the project without collecting new data:

- [Processed job data](notebooks/processed_job_data.csv)
- [Jobs table](notebooks/jobs_table.csv)
- [Skills table](notebooks/skills_table.csv)

For Power BI, import the jobs and skills CSVs and create a **one-to-many** relationship from `jobs_table[job_id]` to `skills_table[job_id]`. Use distinct job counts for job-level measures; counting skill rows inflates posting counts.

See the [data dictionary](docs/data_dictionary.md) for metric definitions and DAX examples, and the [setup guide](docs/getting_started.md) to regenerate the exports.

## Repository guide

| Path | Purpose |
|---|---|
| `src/data/` | API client, database access, ingestion, and SQL runner |
| `src/utils/` | Logging |
| `sql/exploration/` | Raw-data profiling queries |
| `sql/cleaning/` | Cleaning and title mapping scripts |
| `sql/validation/` | Post-cleaning checks |
| `notebooks/` | Analysis, reporting preparation, and CSV exports |
| `data/reference/` | Country reference data and inspection notebook |
| `models/` | Artifacts from the legacy classifier experiment |
| `docs/` | Setup, definitions, quality assessment, and original plans |
| `tests/` | Manual API/database checks; some call external services and write data |

## Limitations and next steps

- API search queries, pagination, provider coverage, and repeated listings affect sample composition.
- Dictionary matching detects mentions rather than verified requirements or skill proficiency. Aliases, context, and punctuation-sensitive terms need validation.
- The ingestion layer does not enforce a unique source-job constraint; repeated runs can add duplicates.
- Exported `job_id` values are generated from row order and are not stable source identifiers.
- The legacy classifier's small test set is not evidence of production performance.
- Next priorities: audit extraction quality, retain stable posting identifiers, improve deduplication, record collection provenance, and build the Power BI report.

Configuration belongs in a local `.env`; the tracked [.env.example](.env.example) contains blank credential fields. A non-empty example was replaced during repository cleanup. Any previously exposed credentials must be rotated, since historical commits may retain them.

## Author

**Antonio Jabbour** — Data Analyst portfolio
