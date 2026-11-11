import os

import psycopg

DATABASE_URL = os.environ.get("DATABASE_URL")
if not DATABASE_URL:
    raise RuntimeError("Set the DATABASE_URL environment variable before starting the app.")


def get_connection() -> psycopg.Connection:
    return psycopg.connect(DATABASE_URL)
def create_portfolio(cash: float) -> int:
    with get_connection() as conn:
        row = conn.execute(
            "INSERT INTO portfolios (cash) VALUES (%s) RETURNING id", (cash,)
        ).fetchone()
        return row[0]