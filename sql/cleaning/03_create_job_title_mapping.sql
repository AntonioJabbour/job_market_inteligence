DROP TABLE IF EXISTS job_title_mapping;

CREATE TABLE job_title_mapping (
    pattern TEXT,
    standardized_job_title TEXT,
    priority INTEGER
);

INSERT INTO job_title_mapping (
    pattern,
    standardized_job_title,
    priority
)
VALUES
-- Data Analyst
('data analyst', 'data analyst', 1),
('market data analyst', 'data analyst', 1),
('business data analyst', 'data analyst', 1),
('lead data analyst', 'data analyst', 1),
('senior data analyst', 'data analyst', 1),

-- Data Scientist
('data scientist', 'data scientist', 1),
('data science', 'data scientist', 2),
('senior data scientist', 'data scientist', 1),
('sr data scientist', 'data scientist', 1),
('data science manager', 'data scientist', 2),
('senior data science manager', 'data scientist', 2),

-- Data Engineer
('data engineer', 'data engineer', 1),
('senior data engineer', 'data engineer', 1),
('lead data engineer', 'data engineer', 1),
('big data engineer', 'data engineer', 1),
('junior data engineer', 'data engineer', 1),
('sr. data engineer', 'data engineer', 1),
('remote data engineer', 'data engineer', 1),

-- Machine Learning Engineer
('machine learning engineer', 'machine learning engineer', 1),
('senior machine learning engineer', 'machine learning engineer', 1),
('lead machine learning engineer', 'machine learning engineer', 1),
('ml engineer', 'machine learning engineer', 1),
('applied ml', 'machine learning engineer', 1),
('machine learning', 'machine learning engineer', 2),
('ai / machine learning engineer', 'machine learning engineer', 1),

-- AI Engineer
('ai engineer', 'ai engineer', 1),
('artificial intelligence engineer', 'ai engineer', 1),
('artificial intelligence', 'ai engineer', 2),
('ai/ml', 'ai engineer', 1),
('ai / ml', 'ai engineer', 1),
('ai & ml', 'ai engineer', 1),
('ai solutions engineer', 'ai engineer', 1),
('ai solution', 'ai engineer', 1),
('senior ai engineer', 'ai engineer', 1),
('ai software engineer', 'ai engineer', 2),
('ai software', 'ai engineer', 2),
('ai developer', 'ai engineer', 2),
('enterprise ai engineer', 'ai engineer', 1),
('agentic ai', 'ai engineer', 1),
('applied ai', 'ai engineer', 1),
('ai data engineer', 'ai engineer', 1),

-- Business Intelligence Analyst
('business intelligence analyst', 'business intelligence analyst', 1),
('business intelligence', 'business intelligence analyst', 1),
('bi analyst', 'business intelligence analyst', 2),
('power bi analyst', 'business intelligence analyst', 2),
('lead business intelligence', 'business intelligence analyst', 1),
('business intelligence lead', 'business intelligence analyst', 1),
('business intelligence engineer', 'business intelligence analyst', 2),
('bi engineer', 'business intelligence analyst', 2),

-- Analytics Engineer
('analytics engineer', 'analytics engineer', 1),
('analytics lead', 'analytics engineer', 2),

-- MLOps Engineer
('mlops engineer', 'mlops engineer', 1),
('mlops', 'mlops engineer', 1),

-- Data Architect
('data architect', 'data architect', 1);