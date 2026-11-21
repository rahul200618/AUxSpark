from dataclasses import dataclass
from enum import Enum


class Status(str, Enum):
    PLACED = "placed"
    SHIPPED = "shipped"
    DELIVERED = "delivered"


@dataclass(frozen=True)
class Order:
    order_id: str
    customer: str
    status: Status
    eta_days: int
