# Getting Started

## Choose a workflow

| Goal | API key | PostgreSQL | Entry point |
|---|---|---|---|
| Inspect saved results | No | No | Open the notebooks on GitHub |
| Build a Power BI report from included exports | No | No | Import the two CSV tables |
| Regenerate jobs and skills exports | No | No | Run `02_powerbi_preparation.ipynb` |
| Rebuild EDA from the cleaned database | No new API call required | Yes | Prepare database tables, then run `01_initial_eda.ipynb` |
| Collect new job listings | Yes | Yes | Configure and explicitly run ingestion |

## Local Python environment

From the repository root:

```bash
python -m venv .venv
# macOS/Linux:
source .venv/bin/activate
# Windows PowerShell:
# .venv\Scripts\Activate.ps1

python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -m jupyterlab
```

The requirements file records an existing environment, rather than a tested minimal dependency set. Its Windows terminal dependency is conditional on Windows. The frozen versions still need validation in a fresh environment; this documentation does not certify all platform/version combinations.

## Regenerate the Power BI tables

1. Open `notebooks/02_powerbi_preparation.ipynb`.
2. Run the cells in order. The notebook locates the project from either the repository root or the `notebooks/` directory.
3. It reads the included `notebooks/processed_job_data.csv`.
4. It exports `notebooks/jobs_table.csv` and `notebooks/skills_table.csv`, replacing those files if present.
5. Review the validation cell before using the exports.

The snapshot's saved outputs report 1,044 jobs, 5,865 skill records, unique job IDs, no missing skill names, and no duplicate job–skill–category records. Recheck those conditions after regenerating data.

## Power BI relationship

Import both CSV exports. Set `job_id` to a whole number in both tables and `is_remote` to True/False in the jobs table.

Create a one-to-many relationship:

- One: `jobs_table[job_id]`
- Many: `skills_table[job_id]`
- Cross-filter direction: Single, from jobs to skills

Role and country slicers from the jobs table will filter skill records. A skill slicer from the skills table will not automatically filter the jobs table with this relationship; use measures on the skills table for skill-filtered counts.

See [Data dictionary and KPIs](data_dictionary.md) for formulas. A report file is not included; importing these tables does not itself create a dashboard.

## Database and API workflow

The existing SQL pipeline expects additional setup. Use a dedicated development database because cleaning scripts drop and rebuild derived tables.

1. Create a PostgreSQL database.
2. Create a local `.env` file in the repository root. Add the following variable names and supply your own values:

   ```dotenv
   JSEARCH_API_KEY=
   DB_HOST=localhost
   DB_PORT=5432
   DB_NAME=job_market_db
   DB_USER=postgres
   DB_PASSWORD=
   APP_ENV=development
   LOG_LEVEL=INFO
   ```
3. Set `DB_HOST`, `DB_PORT`, `DB_NAME`, `DB_USER`, and `DB_PASSWORD`. Set `JSEARCH_API_KEY` only if collecting new listings.
4. Before ingestion, review `src/data/ingest_jobs.py`: it currently loops over 9 roles and 14 countries with `num_pages=3`. Reduce scope for a first run and check your provider quota.
5. Explicitly run collection from the repository root:

```bash
python -m src.data.ingest_jobs
```

This calls an external API and inserts rows into `raw_job_postings`. Repeating it can insert duplicate source jobs.

6. Import `data/reference/country_reference.csv` into a database table named `country_reference` with compatible `country_name` and `country_code` columns. The SQL runner does not create or import this table.
7. Create title mappings **before** the version 2 cleaning query. The current runner sorts filenames and would run `02` before `03` on a fresh database. Until that runner is corrected, execute the files explicitly in this order in your PostgreSQL client:

   1. `sql/cleaning/03_create_job_title_mapping.sql`
   2. `sql/cleaning/01_create_clean_job_posting.sql`
   3. `sql/cleaning/02_create_clean_job_posting_v2.sql`
   4. `sql/validation/01_validate_clean_job_posting.sql`
   5. `sql/validation/02_validate_clean_job_posting_v2.sql`

The country backfill query can fail if multiple reference country names match one location. Inspect ambiguous matches before running it. Validation queries report checks; they do not constitute a fully automated test suite.

8. Open the EDA notebook with its working directory set to `notebooks/`; it imports the project from its parent directory and reads `clean_job_posting_v2`.
9. Run the notebook in order. Its export writes `processed_job_data.csv` relative to the notebook working directory.
10. Run the Power BI preparation notebook to regenerate both related tables together.

The API/database workflow has not been rerun for this repository presentation update. A successful script exit alone does not guarantee success: some existing scripts log errors and continue.

## Legacy machine-learning notebook

`03_machine_learning.ipynb` contains saved results from an older 54-record, two-role dataset with `extracted_skills`, `extracted_tools`, and `extracted_technologies` columns.

The current processed CSV uses eight differently named extracted columns, so the legacy notebook is **not a compatible next step** after the current Power BI workflow. It also needs plotting imports restored before a clean execution. Review its historical outputs separately until it is migrated and evaluated on a suitable dataset.

## Credentials and data usage

Keep credentials in the ignored local `.env`; do not commit environment files. The previously tracked environment example has been removed. Rotate any credentials that were previously committed; deleting a file does not erase Git history.

The repository's `LICENSE` file is currently empty, so it does not grant an explicit open-source license. An owner-selected license and confirmation of API/data redistribution terms are still needed.
