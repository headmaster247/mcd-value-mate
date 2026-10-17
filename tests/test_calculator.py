
import pytest

from src.calculator import calculate_total, check_budget


def test_calculate_total():
    items = [
        {"name": "Item A", "price": 10, "quantity": 2},
        {"name": "Item B", "price": 5, "quantity": 1},
    ]

    assert calculate_total(items) == 25.0


def test_check_budget_within_budget():
    items = [{"name": "Item A", "price": 20, "quantity": 1}]

    result = check_budget(items, 30)

    assert result["within_budget"] is True
    assert result["remaining"] == 10.0


def test_check_budget_exceeded():
    items = [{"name": "Item A", "price": 20, "quantity": 2}]

    result = check_budget(items, 30)

    assert result["within_budget"] is False
    assert result["remaining"] == -10.0


def test_missing_price_is_rejected():
    with pytest.raises(ValueError):
        calculate_total([{"name": "Unknown item"}])


def test_negative_price_is_rejected():
    with pytest.raises(ValueError):
        calculate_total([{"name": "Item A", "price": -5}])


def test_invalid_budget_is_rejected():
    with pytest.raises(ValueError):
        check_budget([], -1)
