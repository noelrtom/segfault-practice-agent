import json


def check_order_db(order_id: str) -> dict:
    """Look up an order by ID (e.g. ORD-102). Returns customer, item, amount, status and days_since_delivery."""
    with open("orders.json") as f:
        db = json.load(f)
    return db.get(order_id.upper().strip(), {"error": f"Order {order_id} not found"})