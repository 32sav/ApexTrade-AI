import os

import psycopg

from trading import Portfolio

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


def load_portfolio(portfolio_id: int) -> Portfolio:
    with get_connection() as conn:
        row = conn.execute(
            "SELECT cash FROM portfolios WHERE id = %s", (portfolio_id,)
        ).fetchone()
        if row is None:
            raise LookupError(f"Portfolio {portfolio_id} not found")

        portfolio = Portfolio(cash=float(row[0]))
        rows = conn.execute(
            "SELECT symbol, quantity FROM positions WHERE portfolio_id = %s",
            (portfolio_id,),
        ).fetchall()
        portfolio.positions = {symbol: quantity for symbol, quantity in rows}
        return portfolio


def save_portfolio(portfolio_id: int, portfolio: Portfolio) -> None:
    with get_connection() as conn:
        conn.execute(
            "UPDATE portfolios SET cash = %s WHERE id = %s",
            (portfolio.cash, portfolio_id),
        )
        conn.execute("DELETE FROM positions WHERE portfolio_id = %s", (portfolio_id,))
        for symbol, quantity in portfolio.positions.items():
            if quantity > 0:
                conn.execute(
                    "INSERT INTO positions (portfolio_id, symbol, quantity) VALUES (%s, %s, %s)",
                    (portfolio_id, symbol, quantity),
                )