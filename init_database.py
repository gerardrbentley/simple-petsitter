from pathlib import Path

from src.db import execute_query

def main() -> None:
    """First Pass Database Initialize Script
    Create todo Table in the database if it doesn't already exist"""
    for query_file in (
        "init_tables.sql",
        "trigger_update_timestamp.sql",
        "apply_update_timestamp.sql",
        "seed_row.sql",
    ):
        query_path = Path("postgres") / query_file
        query =  query_path.read_text()
        print(query)
        execute_query(query)

if __name__ == "__main__":
    main()
