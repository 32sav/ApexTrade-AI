import pytest
from fastapi.testclient import TestClient

from main import app
from trading import Order, InsufficientFundsError, calculate_order_value, check_affordability

client = TestClient(app)

ORDER = Order(symbol="AAPL", side="buy", quantity=10, price=150.5)


def test_order_value():
    assert calculate_order_value(ORDER) == 1505.0


def test_invalid_side_rejected():
    with pytest.raises(ValueError):
        Order(symbol="AAPL", side="hold", quantity=10, price=150.5)


def test_zero_quantity_rejected():
    with pytest.raises(ValueError):
        Order(symbol="AAPL", side="buy", quantity=0, price=150.5)


def test_affordable_when_balance_covers_order():
    check_affordability(ORDER, 2000)


def test_affordable_at_exact_balance():
    check_affordability(ORDER, 1505)


def test_insufficient_funds_raises():
    with pytest.raises(InsufficientFundsError):
        check_affordability(ORDER, 1000)


def test_endpoint_affordable():
    response = client.post(
        "/orders/check",
        json={"order": {"symbol": "AAPL", "side": "buy", "quantity": 10, "price": 150.5}, "cash_balance": 2000},
    )
    assert response.status_code == 200
    assert response.json() == {"affordable": True, "order_value": 1505.0}


def test_endpoint_insufficient_funds():
    response = client.post(
        "/orders/check",
        json={"order": {"symbol": "AAPL", "side": "buy", "quantity": 10, "price": 150.5}, "cash_balance": 1000},
    )
    assert response.status_code == 400
    assert "Insufficient funds" in response.json()["detail"]