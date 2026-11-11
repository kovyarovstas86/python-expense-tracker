APP_TITLE = "Учёт расходов"
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


def validate_expense(amount):
    return amount > 0


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
            try:
                amount = float(input("Сумма: "))

                if not validate_expense(amount):
                    print("Сумма должна быть больше нуля")
                    continue

                category = input("Категория: ")
                add_expense(expenses, amount, category)
                print("Расход добавлен!")

            except ValueError:
                print("Ошибка: введите сумму числом")

        elif choice == "2":
            show_expenses(expenses)

        elif choice == "3":
            print("Всего:", calculate_total(expenses))

        elif choice == "0":
            break

        else:
            print("Неверный выбор")