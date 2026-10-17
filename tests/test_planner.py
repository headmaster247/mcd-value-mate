
from src.planner import recommend_meals


def test_recommend_meals_filters_over_budget():
    candidates = [
        [{"name": "Meal A", "price": 20}],
        [{"name": "Meal B", "price": 40}],
        [{"name": "Meal C", "price": 25}],
    ]

    results = recommend_meals(candidates, 30)

    assert len(results) == 2
    assert [result["total"] for result in results] == [20, 25]


def test_recommend_meals_empty_candidates():
    assert recommend_meals([], 30) == []


def test_recommend_meals_skips_missing_prices():
    candidates = [
        [{"name": "Unknown item"}],
        [{"name": "Meal A", "price": 20}],
    ]

    results = recommend_meals(candidates, 30)

    assert len(results) == 1
    assert results[0]["total"] == 20
