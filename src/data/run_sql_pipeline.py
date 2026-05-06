from pathlib import Path
from src.utils.logger import get_logger
from src.data.db import get_db_connection

logger = get_logger(__name__)


def read_sql_file(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()


def run_sql_file(file_path, fetch_results=False):
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        sql_query = read_sql_file(file_path)
        cursor.execute(sql_query)

        if fetch_results:
            results = cursor.fetchall()

            print(f"\nResults from: {file_path}")
            for row in results:
                print(row)
        else:
            conn.commit()
            print(f"Executed successfully: {file_path}")

    except Exception as error:
        conn.rollback()
        print(f"Error executing: {file_path}")
        print(error)

    finally:
        cursor.close()
        conn.close()


def run_sql_folder(folder_path, fetch_results=False):
    folder = Path(folder_path)
    sql_files = sorted(folder.glob("*.sql"))

    for sql_file in sql_files:
        run_sql_file(sql_file, fetch_results=fetch_results)


if __name__ == "__main__":

    print("Running cleaning pipeline...")
    run_sql_folder("sql/cleaning", fetch_results=False)

    print("\nRunning validation pipeline...")
    run_sql_folder("sql/validation", fetch_results=True)

    print("\nPipeline completed.")