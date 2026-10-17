
from src.calculator import check_budget


def recommend_meals(candidates, budget):
    """
    Rank meal combinations using verified candidate prices.

    Each candidate is a list of item dictionaries.
    """
    recommendations = []

    for items in candidates:
        try:
            result = check_budget(items, budget)
        except (ValueError, TypeError):
            continue

        if result["within_budget"]:
            recommendations.append({
                "items": items,
                "total": result["total"],
                "remaining": result["remaining"],
            })

    recommendations.sort(
        key=lambda meal: (
            meal["total"],
            -meal["remaining"],
        )
    )

    return recommendations
