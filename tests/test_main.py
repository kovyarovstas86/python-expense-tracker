from src.main import (
    add_expense,
    calculate_total,
    calculate_average,
    count_expenses
)
from src.main import (
    add_expense,
    calculate_total,
    calculate_average
)


def test_add_expense():
    data = []
    add_expense(data, 1000, "Food")
    assert len(data) == 1


def test_total():
    data = [
        {"amount": 1000, "category": "Food"},
        {"amount": 2000, "category": "Transport"}
    ]
    assert calculate_total(data) == 3000


def test_average():
    data = [
        {"amount": 1000, "category": "Food"},
        {"amount": 2000, "category": "Transport"}
    ]
    assert calculate_average(data) == 1500
from src.main import largest_expense


def test_largest_expense():
    data = [
        {"amount": 1000, "category": "Food"},
        {"amount": 5000, "category": "Shopping"}
    ]
    assert largest_expense(data)["amount"] == 5000
def test_count_expenses():
    expenses = [
        {"amount": 100, "category": "Food"},
        {"amount": 200, "category": "Transport"},
    ]

    assert count_expenses(expenses) == 2