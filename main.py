from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

from trading import Order, InsufficientFundsError, calculate_order_value, check_affordability

app = FastAPI(title="ApexTrade AI")


class AffordabilityRequest(BaseModel):
    order: Order
    cash_balance: float = Field(..., ge=0)


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