class OrderNotFoundError(Exception):
    pass


def lookup_order(orders, order_id):
    if not isinstance(order_id, str) or not order_id:
        raise ValueError("order_id must be a non-empty string")
    for order in orders:
        if order.get("order_id") == order_id:
            return order
    raise OrderNotFoundError(f"Order {order_id} not found")


def describe_order(orders, order_id):
    try:
        order = lookup_order(orders, order_id)
    except OrderNotFoundError:
        return f"Order {order_id} not found"
    return f"{order['status']} order {order['order_id']} totaling {order['total']}"


def raises_not_found(orders, order_id):
    try:
        lookup_order(orders, order_id)
    except OrderNotFoundError:
        return True
    except Exception:
        return False
    return False


def _raise_value():
    try:
        lookup_order([], '')
    except ValueError:
        return True
    except NotImplementedError:
        return False
    return False
