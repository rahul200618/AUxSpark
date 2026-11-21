class OrderLookupError(Exception):
    """Backend/transport failure while looking up an order."""


class OrderNotFound(OrderLookupError):
    """No order exists for the given id."""
