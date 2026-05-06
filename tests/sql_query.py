import os
import pandas as pd
from src.utils.logger import get_logger
from src.data.db import get_db_connection

logger = get_logger(__name__)

conn= get_db_connection()

selet_table = """SELECT * FROM raw_job_postings"""

# cursor = conn.cursor()
# # cursor.execute(selet_table)

# # data = cursor.fetchall()
# # # print(pd.DataFrame(data))


df = pd.read_sql(selet_table, conn)

# # # truncate_table = """Truncate table raw_job_postings"""
# # # cursor.execute(truncate_table)

# # # after_truncate = """select count(*) from raw_job_postings"""
# # # cursor.execute(after_truncate)

# # # count_2 = cursor.fetchone()[0]
# # # print(count_2)

# # cursor.close()
conn.close()

# print(df.isnull().sum())

print(df['salary_min'].isnull().sum())
print(df['job_description'].isnull().sum())
print(df['job_description'].str.len())
