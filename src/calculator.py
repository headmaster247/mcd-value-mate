
def calculate_total(items):
    """
    Calculate the total price of a meal combination.

    Each item must contain:
    - name
    - price
    - quantity
    """
    total = 0.0

    for item in items:
        price = item.get("price")
        quantity = item.get("quantity", 1)

        if price is None:
            raise ValueError(
                f"Missing price for item: {item.get('name', 'unknown')}"
            )

        if isinstance(price, bool) or not isinstance(price, (int, float)):
            raise ValueError("Price must be a number.")

        if price < 0:
            raise ValueError("Price cannot be negative.")

        if isinstance(quantity, bool) or not isinstance(quantity, int):
            raise ValueError("Quantity must be an integer.")

        if quantity < 1:
            raise ValueError("Quantity must be at least 1.")

        total += price * quantity

    return round(total, 2)


def check_budget(items, budget):
    """Return whether the meal combination fits the budget."""
    if isinstance(budget, bool) or not isinstance(budget, (int, float)):
        raise ValueError("Budget must be a number.")

    if budget < 0:
        raise ValueError("Budget cannot be negative.")

    total = calculate_total(items)

    return {
        "total": total,
        "remaining": round(budget - total, 2),
        "within_budget": total <= budget,
    }
