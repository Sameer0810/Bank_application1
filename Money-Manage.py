import json
from datetime import datetime

DATA_FILE = "data.json"

# Load existing data or initialize
try:
    with open(DATA_FILE, "r") as f:
        transactions = json.load(f)
except FileNotFoundError:
    transactions = []

# Function to add transaction
def add_transaction():
    type_ = input("Type (income/expense): ").lower()
    amount = float(input("Amount: "))
    category = input("Category (e.g., Food, Salary, Rent): ")
    date = input("Date (YYYY-MM-DD) [Leave blank for today]: ")
    if not date:
        date = datetime.today().strftime('%Y-%m-%d')
    
    transaction = {
        "type": type_,
        "amount": amount,
        "category": category,
        "date": date
    }
    transactions.append(transaction)
    print("Transaction added successfully!")

# Function to show all transactions
def show_transactions():
    if not transactions:
        print("No transactions yet.")
        return
    for t in transactions:
        print(f"{t['date']} | {t['type'].capitalize()} | {t['category']} | ${t['amount']}")

# Function to show summary
def show_summary():
    income = sum(t['amount'] for t in transactions if t['type'] == 'income')
    expense = sum(t['amount'] for t in transactions if t['type'] == 'expense')
    print(f"\nTotal Income: ${income}")
    print(f"Total Expense: ${expense}")
    print(f"Balance: ${income - expense}\n")

# Function to save data
def save_data():
    with open(DATA_FILE, "w") as f:
        json.dump(transactions, f, indent=4)
    print("Data saved!")

# Main menu
def main():
    while True:
        print("\n--- Personal Finance Manager ---")
        print("1. Add Transaction")
        print("2. Show Transactions")
        print("3. Show Summary")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            add_transaction()
        elif choice == "2":
            show_transactions()
        elif choice == "3":
            show_summary()
        elif choice == "4":
            save_data()
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()
