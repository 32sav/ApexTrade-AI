from typing import Literal

from pydantic import BaseModel, Field


class Order(BaseModel):
    symbol: str = Field(..., min_length=1, max_length=10)
    side: Literal["buy", "sell"]
    quantity: int = Field(..., gt=0)
    price: float = Field(..., gt=0)


def calculate_order_value(order: Order) -> float:
    return order.quantity * order.price
class InsufficientFundsError(Exception):
    pass


def check_affordability(order: Order, cash_balance: float) -> None:
    cost = calculate_order_value(order)
    if cost > cash_balance:
        raise InsufficientFundsError(
            f"Insufficient funds: order costs {cost:.2f}, balance is {cash_balance:.2f}"
        )
def apply_order(order: Order, cash_balance: float) -> float:
    cost = calculate_order_value(order)
    if order.side == "buy":
        check_affordability(order, cash_balance)
        return cash_balance - cost
    return cash_balance + cost
class Portfolio:
    def __init__(self, cash: float):
        self.cash = cash
        self.positions: dict[str, int] = {}

    def apply_order(self, order: Order) -> None:
        held = self.positions.get(order.symbol, 0)

        if order.side == "buy":
            self.cash = apply_order(order, self.cash)
            self.positions[order.symbol] = held + order.quantity
        else:
            if order.quantity > held:
                raise ValueError(
                    f"Cannot sell {order.quantity} {order.symbol}: only {held} held"
                )
            self.cash = apply_order(order, self.cash)
            self.positions[order.symbol] = held - order.quantity