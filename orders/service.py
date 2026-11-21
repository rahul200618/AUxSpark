import logging
from .models import Order, Status
from .errors import OrderNotFound

logger = logging.getLogger(__name__)

_STORE: dict[str, Order] = {
    "A-1001": Order("A-1001", "Dana", Status.SHIPPED, 2),
    "A-1002": Order("A-1002", "Omar", Status.DELIVERED, 0),
}


def lookup_order(order_id: str) -> Order:
    logger.info("lookup_order id=%s", order_id)
    order = _STORE.get(order_id)
    if order is None:
        logger.warning("order not found id=%s", order_id)
        raise OrderNotFound(order_id)
    return order
