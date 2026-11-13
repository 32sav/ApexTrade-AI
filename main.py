from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, Field

from database import create_portfolio, load_portfolio, save_portfolio
from trading import (
    InsufficientFundsError,
    Order,
    calculate_order_value,
    check_affordability,
)

app = FastAPI(title="ApexTrade AI")
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/ui", include_in_schema=False)
def ui():
    return FileResponse("static/index.html")


class AffordabilityRequest(BaseModel):
    order: Order
    cash_balance: float = Field(..., ge=0)


class PortfolioCreate(BaseModel):
    cash: float = Field(..., ge=0)


@app.get("/")
def read_root():
    return {"status": "ok", "app": "ApexTrade AI"}


@app.post("/orders/check")
def check_order(request: AffordabilityRequest):
    try:
        check_affordability(request.order, request.cash_balance)
    except InsufficientFundsError as e:
        raise HTTPException(status_code=400, detail=str(e))
    return {"affordable": True, "order_value": calculate_order_value(request.order)}


@app.post("/portfolios", status_code=201)
def new_portfolio(body: PortfolioCreate):
    portfolio_id = create_portfolio(body.cash)
    return {"id": portfolio_id, "cash": body.cash, "positions": {}}


@app.get("/portfolios/{portfolio_id}")
def get_portfolio(portfolio_id: int):
    try:
        portfolio = load_portfolio(portfolio_id)
    except LookupError as e:
        raise HTTPException(status_code=404, detail=str(e))
    return {"id": portfolio_id, "cash": portfolio.cash, "positions": portfolio.positions}


@app.post("/portfolios/{portfolio_id}/orders")
def place_order(portfolio_id: int, order: Order):
    try:
        portfolio = load_portfolio(portfolio_id)
    except LookupError as e:
        raise HTTPException(status_code=404, detail=str(e))
    try:
        portfolio.apply_order(order)
    except (InsufficientFundsError, ValueError) as e:
        raise HTTPException(status_code=400, detail=str(e))
    save_portfolio(portfolio_id, portfolio)
    return {"id": portfolio_id, "cash": portfolio.cash, "positions": portfolio.positions}