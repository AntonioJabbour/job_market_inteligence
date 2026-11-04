# Data Dictionary and Reporting Measures

## Tables and grain

| Table | Grain | Key / relationship |
|---|---|---|
| `processed_job_data.csv` | One processed job record with list-like extracted-skill columns | Input to the Power BI preparation notebook |
| `jobs_table.csv` | One processed job record | Unique `job_id` in the saved export |
| `skills_table.csv` | One job–skill–category record | `job_id` references the jobs table |

The Power BI notebook assigns sequential IDs based on row order. Regenerate both exports together. Do not use these IDs as persistent keys across independently regenerated snapshots.

## Jobs fields

| Field | Meaning / handling |
|---|---|
| `job_id` | Export-specific integer surrogate key |
| `standardized_job_title` | Role category assigned by SQL pattern matching |
| `clean_job_title` | Normalized original title |
| `company_name` | Employer name from the listing |
| `job_country` | Country code where available; preserve a missing/unknown reporting category |
| `job_location` | Location text; mostly missing in the saved EDA |
| `employment_type` | Normalized source text, sometimes containing several types |
| `is_remote` | Source remote flag; false does not establish an on-site requirement |
| `job_description` | Original listing description |
| `job_source` | Normalized publisher/source |
| `posted_at_utc` | Source posting timestamp, when available |
| `normalized_job_description` | Lowercase text used for matching |

## Skills fields

| Field | Meaning |
|---|---|
| `job_id` | Foreign key to the job record |
| `skill` | Matched dictionary term |
| `category` | Dictionary category: programming languages, BI tools, databases, cloud, data engineering, machine learning, big data, or AI technologies |

A job can match many skills, so skill record count is not posting count. A dictionary match indicates a mention, not necessarily a mandatory requirement. Related terms such as abbreviations and full phrases can both match.

## KPI definitions

| KPI | Definition | Important caveat |
|---|---|---|
| Job records | Distinct `jobs_table[job_id]` in the current job context | Sample size, not total market demand |
| Remote-flag share | Jobs explicitly flagged true / all jobs in that context | Report unknown flags separately if present |
| Jobs mentioning selected skills | Distinct `skills_table[job_id]` after skill/category filters | Several selected skills produce a union, not an intersection |
| Skill mention share | Jobs mentioning selected skills / all jobs in the current role/country context | A job must count at most once in the numerator |
| Category extraction coverage | Jobs with at least one match in a category / all jobs in context | Coverage is not precision or recall |
| Missing posting date share | Jobs with no valid posting date / all jobs in context | Exclude undated records explicitly from time-series charts |

## Example Power BI measures

These formulas assume table names `jobs_table` and `skills_table`, a unique integer `job_id`, a Boolean remote column, and the single-direction relationship described in the [setup guide](getting_started.md).

```dax
Job Records =
DISTINCTCOUNT(jobs_table[job_id])

Remote Flagged Jobs =
CALCULATE(
    [Job Records],
    KEEPFILTERS(jobs_table[is_remote] == TRUE())
)

Remote Flag Share =
DIVIDE([Remote Flagged Jobs], [Job Records])

Jobs Mentioning Selected Skills =
DISTINCTCOUNT(skills_table[job_id])

Skill Mention Share =
DIVIDE([Jobs Mentioning Selected Skills], [Job Records])
```

Format the two shares as percentages. The skill share denominator retains the current jobs-table filters, such as role and country. With the specified relationship, filters on the skills table affect the numerator without reducing the denominator.

## Reporting suggestions

- Overview: job records, remote-flag share, and missing-data indicators.
- Role detail: skill mention share with the number of supporting job records.
- Geography: sample counts by country, with missing values visible.
- Quality page: missing dates, unmatched roles, duplicate source IDs, and extraction audit findings.

These are proposed report pages. No finished Power BI report is included.

## Interpretation boundaries

Counts reflect the selected API queries and snapshot. They are not population estimates. Trend claims require repeated, comparable collection windows; a snapshot and partially missing posting dates are insufficient. Salary comparisons require usable, comparable salary values and should not be inferred from this export.
