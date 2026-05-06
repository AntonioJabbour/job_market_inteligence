# Project Configuration Specification

## 1. Purpose

This document defines the configurable settings and configuration design for the AI-Powered Job Market Intelligence Platform.

The goal of this configuration layer is to separate environment-specific settings from project-level constants so that the project remains reproducible, maintainable, and scalable.

Configuration management is an important part of production-grade data science systems because it allows the pipeline to run consistently across different environments such as local development, testing, and production.

---

# 2. Environment Variables

Sensitive configuration values should not be stored in source code. Instead, they should be placed in environment variables managed through a `.env` file.

The repository should include a `.env.example` template that lists the required variables without exposing secrets.

### API Configuration

- `JSEARCH_API_KEY`

This key allows the ingestion pipeline to authenticate with the JSearch API and retrieve job postings.

---

### Database Configuration

- `DB_HOST`
- `DB_PORT`
- `DB_NAME`
- `DB_USER`
- `DB_PASSWORD`

These variables define how the project connects to the PostgreSQL database.

Example configuration:

- DB_HOST = localhost
- DB_PORT = 5432
- DB_NAME = job_market_db

---

### Application Environment

- `APP_ENV`
- `LOG_LEVEL`

APP_ENV may contain values such as:

- development
- staging
- production

LOG_LEVEL defines the verbosity of logs produced by the pipeline.

Possible values include:

- DEBUG
- INFO
- WARNING
- ERROR

---

# 3. Project Constants

Some configuration values do not need to be secret but should still be centralized to avoid hardcoding values across multiple files.

These constants may later be placed inside configuration modules within the codebase.

### API and Ingestion Constants

Examples include:

- API request timeout
- API page size
- maximum number of pages per ingestion run
- retry attempts for failed requests
- ingestion batch size

These parameters help control the behavior of the ingestion pipeline.

---

### Data Constants

Examples include:

- raw table name
- cleaned table name
- supported salary currencies
- employment type categories
- remote work labels

These constants help standardize data across the pipeline.

---

### Modeling Constants

Examples include:

- random seed for reproducibility
- train/test split ratio
- salary prediction target column
- clustering parameters

These constants ensure that experiments remain reproducible.

---

# 4. Default Search Roles

The ingestion pipeline will start by collecting job postings for the following roles:

- Data Scientist
- Data Analyst
- Machine Learning Engineer
- Analytics Engineer
- Business Intelligence Analyst
- AI Engineer

These roles represent the most common positions within the data science and analytics ecosystem.

---

# 5. Geographic Scope

The initial geographic scope for job collection will include the following regions.

### North America

- United States

### Europe

- United Kingdom

### Gulf Region

- United Arab Emirates
- Saudi Arabia
- Qatar
- Kuwait
- Bahrain
- Oman

### Remote Roles

- Global remote positions when available.

This selection allows comparison between mature technology markets and emerging technology hubs.

---

# 6. Logging Requirements

The ingestion pipeline should generate logs for the following events:

- API request start
- API request completion
- search query used
- number of records returned
- number of records inserted into the database
- duplicate detection results
- ingestion errors and retries

Logging is essential for monitoring, debugging, and ensuring pipeline reliability.

---

# 7. Configuration Design Principles

The configuration system for this project follows several principles:

1. Secrets must not be stored in the codebase.
2. Environment-dependent values must remain configurable.
3. Configuration should be centralized whenever possible.
4. Default values should be documented.
5. Configuration should support future scaling of the project.

---

# 8. Expected Outcome

By clearly separating environment variables and configuration constants, the project becomes easier to maintain, deploy, and extend.

This design will support future development phases including:

- automated ingestion pipelines
- machine learning training workflows
- dashboard deployment
- production environment integration.