import json


def check_refund_policy(days_since_delivery: int, reason: str) -> str:
    """Check refund eligibility. Refunds need a damaged/broken/defective item reported within 7 days of delivery."""
    if days_since_delivery <= 7 and any(
        w in reason.lower() for w in ["broken", "damaged", "defective"]
    ):
        return "ELIGIBLE: damaged item within the 7-day window."
    return "NOT ELIGIBLE: outside the 7-day window or reason does not qualify."


def execute_refund(order_id: str) -> str:
    """Refund an order. Only the UI may call this, after human approval."""
    with open("orders.json") as f:
        db = json.load(f)
    oid = order_id.upper().strip()
    if oid not in db:
        return "Order not found."
    if db[oid]["status"].startswith("REFUNDED"):
        return "Already refunded."
    amount = db[oid]["amount"]  # amount comes from the database, not the AI
    db[oid]["status"] = f"REFUNDED (₹{amount})"
    with open("orders.json", "w") as f:
        json.dump(db, f, indent=2)
    return f"Refunded ₹{amount} for {oid}."