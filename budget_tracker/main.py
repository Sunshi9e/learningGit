import os
import json
from datetime import datetime
from transaction import Transaction
from budget_utils import print_summary, load_transactions, save_transactions



def main():
    transactions = load_transactions()

    while True:
        print("\n=== Personal Budget Tracker ===")
        print("1. Add transaction")
        print("2. View summary")
        print("3. Exit")

        choice = input("Enter choice (1-3): ")

        if choice == "1":
            try:
                date_input = input("Enter date (YYYY-MM-DD) or press Enter for today: ").strip()
                date = date_input or datetime.now().strftime("%Y-%m-%d")
                category = input("Enter category (e.g., Food, Transport): ").strip()
                amount = float(input("Enter amount: "))
                transaction = Transaction(date, category, amount)
                transactions.append(transaction)
                save_transactions(transactions)
                print("Transaction added!")
            except ValueError as ve:
                print(f"Invalid input: {ve}")
            except Exception as e:
                print(f"An error occurred: {e}")
            
        elif choice == "2":
            print_summary(transactions)
        elif choice == "3":
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
