import os

def show_menu():
    print("\nExpense Tracker")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Exit")

def add_expense():
    expense = float(input("Enter the expense amount: "))
    with open("expenses.txt", "a") as file:
        file.write(f"{expense}\n")
    print("Expense added successfully!")

def view_expenses():
    if not os.path.exists("expenses.txt"):
        print("No expenses found.")
        return

    with open("expenses.txt", "r") as file:
        expenses = file.readlines()

    total = sum(float(expense) for expense in expenses)
    print("\nExpenses:")
    for expense in expenses:
        print(f"  - ${float(expense):.2f}")

    print(f"\nTotal Expenses: ${total:.2f}")

def main():
    while True:
        show_menu()
        choice = input("\nEnter your choice (1/2/3): ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            print("Exiting the Expense Tracker.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
