import logging
import sys
from .service import lookup_order
from .errors import OrderNotFound


def main(argv: list[str]) -> int:
    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(name)s %(message)s")
    order_id = argv[1] if len(argv) > 1 else "A-1001"
    try:
        order = lookup_order(order_id)
    except OrderNotFound as exc:
        print(f"No such order: {exc}", file=sys.stderr)
        return 1
    print(f"{order.order_id} {order.status.value} eta={order.eta_days}d")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
