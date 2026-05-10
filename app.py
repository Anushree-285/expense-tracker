expenses = []

def add_expense(name, amount, category):
    expense = {
        "name": name,
        "amount": amount,
        "category": category
    }

    expenses.append(expense)
    print(f"{name} added successfully!")

def view_expenses():
    print("\nExpense List:")

    if not expenses:
        print("No expenses found.")
        return

    total = 0

    for expense in expenses:
        print(
            f"{expense['name']} | "
            f"{expense['category']} | "
            f"₹{expense['amount']}"
        )

        total += expense['amount']

    print(f"\nTotal Expense: ₹{total}")


def show_summary():
    total = 0

    for expense in expenses:
        total += expense["amount"]

    print("\nExpense Summary")
    print(f"Total Transactions: {len(expenses)}")
    print(f"Total Amount: ₹{total}")


add_expense("Groceries", 1500, "Food")
add_expense("Netflix", 499, "Entertainment")

print("Export feature coming soon...")

view_expenses()
show_summary()