def add_expense(expenses, amount, category):
    expenses.append({
        "amount": amount,
        "category": category
    })
    return expenses


def calculate_total(expenses):
    return sum(item["amount"] for item in expenses)


def calculate_average(expenses):
    if not expenses:
        return 0
    return calculate_total(expenses) / len(expenses)


def show_expenses(expenses):
    for item in expenses:
        print(item["category"], item["amount"])


if __name__ == "__main__":
    expenses = []

    add_expense(expenses, 1500, "Food")
    add_expense(expenses, 3000, "Transport")
    add_expense(expenses, 2000, "Shopping")

    print("Expense tracker")
    show_expenses(expenses)
    print("Total:", calculate_total(expenses))
    print("Average:", calculate_average(expenses))