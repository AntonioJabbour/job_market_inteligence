# Data Quality Report

## Overview

This report summarizes the initial data exploration and quality assessment of the `raw_job_postings` dataset. The goal is to evaluate data readiness before proceeding to the data cleaning phase.

---

## 1. Dataset Structure

The dataset contains job posting records with a mix of:

* Categorical columns (e.g., job_title, job_city)
* Numerical columns (e.g., salary_min, salary_max)
* Text columns (e.g., job_description)

The overall structure is clear and suitable for analysis.

---

## 2. Missing Values

### Columns with Missing Data

The following columns contain NULL values:

* company_website
* job_city
* job_state
* posted_at_utc
* salary_min
* salary_max
* salary_currency
* salary_period

### Critical Issue

* `salary_min` and `salary_max` are completely NULL across all rows.
* These columns are currently unusable and will be ignored for now.

---

## 3. Categorical Data Quality

### Observations

* The `job_title` column contains inconsistencies such as:

  * Case differences (e.g., "Data Analyst" vs "data analyst")
  * Formatting variations
* This indicates the need for normalization and standardization.

---

## 4. Numerical Data Quality

### Observations

* Salary-related columns (`salary_min`, `salary_max`) contain no usable values.
* No statistical analysis could be performed due to missing data.

### Decision

* These columns will be temporarily ignored.
* They may be reconsidered if future data sources provide valid values.

---

## 5. Text Data Quality

### job_description

* No NULL or empty values detected.
* Text length analysis shows that descriptions are present and usable.

### Implication

* This column is suitable for further analysis and potential NLP tasks.

---

## 6. Summary of Issues

* Missing values in multiple columns
* Completely empty salary-related columns
* Inconsistent categorical values (job_title)

---

## 7. Next Steps

The following actions will be performed in the data cleaning phase:

* Standardize categorical columns (e.g., normalize job_title)
* Handle missing values appropriately
* Ignore or revisit salary-related fields
* Prepare text data for further analysis if needed

---

## Conclusion

The dataset is usable but requires cleaning and standardization before further analysis or modeling.
