expenses = []

def add_expense(name, amount):
    expense = {
        "name": name,
        "amount": amount
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
        print(f"{expense['name']} - ₹{expense['amount']}")
        total += expense['amount']

    print(f"\nTotal Expense: ₹{total}")

add_expense("Groceries", 1500)
add_expense("Internet Bill", 999)

view_expenses()