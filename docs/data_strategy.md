# AI-Powered Job Market Intelligence Platform

## Data Strategy

---

# 1. Data Sources

The project will use **modern job posting data collected from public job APIs** to ensure that the dataset reflects current market trends and technologies.

## Primary Data Source – Job APIs

Job postings will be collected using job search APIs that provide access to real-time job market data. Possible APIs include:

* **Adzuna Jobs API**
* **JSearch API**
* **RapidAPI Job APIs**
* **USAJobs API (optional for government roles)**

These APIs allow programmatic access to job postings that contain fields such as job title, company, location, salary information, and job descriptions.

## Why APIs Instead of Static Datasets

Using APIs ensures that:

* the dataset contains **modern and continuously updated job postings**
* the project simulates **real-world data engineering workflows**
* the pipeline can be **extended to run automatically**
* the project demonstrates **API integration and data ingestion pipelines**

This approach better reflects how real companies build job market analytics platforms.

---

# 2. Target Dataset Schema

The final dataset will contain structured information extracted from job postings collected through APIs.

| Column            | Description                                           |
| ----------------- | ----------------------------------------------------- |
| job_id            | Unique identifier for the job posting                 |
| job_title         | Title of the job role                                 |
| company_name      | Name of the company                                   |
| location          | Job location (city/state)                             |
| country           | Country where the job is located                      |
| employment_type   | Full-time, part-time, contract, internship            |
| seniority_level   | Junior, Mid, Senior, Lead                             |
| salary_min        | Minimum salary                                        |
| salary_max        | Maximum salary                                        |
| salary_avg        | Average salary derived from min and max               |
| salary_currency   | Currency of salary                                    |
| salary_period     | Salary period (yearly/monthly/hourly)                 |
| job_description   | Full job description text                             |
| posting_date      | Date the job was posted                               |
| job_source        | Source API                                            |
| remote_flag       | Remote / hybrid / onsite                              |
| skills_extracted  | Skills extracted from job description                 |
| normalized_skills | Standardized skill names                              |
| role_category     | Broad category such as Data Scientist or Data Analyst |
| experience_years  | Required experience if mentioned                      |

### Critical Fields

The most important columns for downstream analysis are:

* `job_title`
* `job_description`
* `salary_min`
* `salary_max`
* `location`
* `skills_extracted`
* `normalized_skills`

These fields enable the main project tasks:

* skill extraction (NLP)
* salary prediction
* role clustering
* market insights

---

# 3. Expected Dataset Size

The dataset is expected to grow continuously as the API pipeline collects new job postings.

Initial target:

* **10,000 – 30,000 job postings**

This size is sufficient for:

* exploratory data analysis
* NLP skill extraction
* clustering models
* salary prediction models
* interactive dashboards

The dataset can grow over time as the API ingestion pipeline continues collecting data.

---

# 4. Data Storage Strategy

The project will use **PostgreSQL as the primary data storage system**.

## PostgreSQL Database

All collected job postings will be stored in a PostgreSQL database. PostgreSQL is chosen because it:

* is widely used in production systems
* supports complex SQL queries
* integrates well with Python and SQLAlchemy
* allows scalable storage for growing datasets

Example database structure:

```
Database: job_market_db
```

Main table:

```
job_postings
```

This table will store all raw job posting information collected from APIs.

---

# 5. Data Pipeline Architecture

The data pipeline will follow this structure:

```
Job API
   ↓
Data Ingestion Script (Python)
   ↓
PostgreSQL Database
   ↓
Data Cleaning & Processing
   ↓
Feature Engineering
   ↓
Machine Learning Models
   ↓
Dashboard (Streamlit)
```

This pipeline simulates a realistic **data engineering + data science workflow**.

---

# 6. Data Quality Considerations

Job posting data commonly contains inconsistencies such as:

* missing salary values
* inconsistent salary currencies
* duplicate job postings
* different naming conventions for the same skill
* noisy or unstructured job descriptions
* missing metadata such as experience level

These issues will be addressed during the **data cleaning and preprocessing phase**.

---

# 7. Expected Outcome

By collecting real job postings through APIs and storing them in PostgreSQL, this project will build a continuously growing dataset that reflects real labor market trends.

This dataset will enable the development of:

* NLP-based skill extraction
* salary prediction models
* job role clustering
* interactive dashboards for job market insights
