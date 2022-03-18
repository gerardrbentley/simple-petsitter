import os
from typing import Optional, Type
from functools import cache

import psycopg
from psycopg.rows import class_row


@cache
def get_connection() -> psycopg.Connection:
    """Make a connection object to psycopg
    Postgres connection args:
    - https://www.postgresql.org/docs/9.1/libpq-connect.html
    """
    default_connection = "dbname=postgres host=localhost user=postgres password=mysecretpassword port=5432"
    database_url = os.getenv('DATABASE_URL', default_connection)
    connection = psycopg.connect(database_url, autocommit=True)
    return connection


def fetch_rows(
    query: str,
    args: Optional[dict] = None,
    dclass: Optional[Type] = None,
) -> list:
    """Given psycopg.Connection and a string query (and optionally necessary query args as a dict),
    Attempt to execute query with cursor, commit transaction, and return fetched rows"""
    connection = get_connection()
    if dclass is not None:
        cur = connection.cursor(row_factory=class_row(dclass))
    else:
        cur = connection.cursor()
    if args is not None:
        cur.execute(query, args)
    else:
        cur.execute(query)
    results = cur.fetchall()
    cur.close()
    return results


def execute_query(
    query: str,
    args: Optional[dict] = None,
) -> None:
    """Given psycopg.Connection and a string query (and optionally necessary query args as a dict),
    Attempt to execute query with cursor"""
    connection = get_connection()
    cur = connection.cursor()
    if args is not None:
        cur.execute(query, args)
    else:
        cur.execute(query)
    cur.close()
