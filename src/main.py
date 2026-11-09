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

def largest_expense(expenses):
    if not expenses:
        return None

    return max(expenses, key=lambda x: x["amount"])
if __name__ == "__main__":
    expenses = []

    while True:
        print("\n=== УЧЁТ РАСХОДОВ ===")
        print("1. Добавить расход")
        print("2. Показать расходы")
        print("3. Общая сумма")
        print("0. Выход")

        choice = input("Выберите действие: ")

        if choice == "1":
            amount = float(input("Сумма: "))
            category = input("Категория: ")
            add_expense(expenses, amount, category)

        elif choice == "2":
            show_expenses(expenses)

        elif choice == "3":
            print("Всего:", calculate_total(expenses))

        elif choice == "0":
            break

        else:
            print("Неверный выбор")