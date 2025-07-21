from collections import defaultdict
import os
import json
from transaction import Transaction

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATABASE = os.path.join(BASE_DIR, "transactions.json")


def load_transactions():
    if not os.path.exists(DATABASE):
        return []
    try:
        with open(DATABASE, "r") as f:
            data = json.load(f)
            return [Transaction(d["date"], d["category"], d["amount"]) for d in data]
    except (json.JSONDecodeError, FileNotFoundError):
        print("Error loading transactions. Starting with an empty record.")
        return []


def save_transactions(transactions):
    try:
        with open(DATABASE, "w") as f:
            json.dump([t.to_dict() for t in transactions], f, indent=2)
    except IOError:
        print("Error saving transactions.")

def group_by_category(transactions):
    totals = {}
    for t in transactions:
        if t.category not in totals:
            totals[t.category] = 0.0
        try:
            totals[t.category] += float(t.amount)
        except (ValueError, TypeError):
            print(f"Invalid amount for transaction: {t.amount}")
    return totals

def calculate_totals(transactions):
    totals = defaultdict(float)
    for t in transactions:
        totals[t.category] += t.amount
    return totals

def print_summary(transactions):
    print("\n--- Transactions ---")
    for t in transactions:
        print(f"{t.date} - {t.category}: ${t.amount:.2f}")

    print("\n--- Summary by Category ---")
    totals = group_by_category(transactions)
    for category, total in totals.items():
        print(f"{category}: ${total:.2f}")
