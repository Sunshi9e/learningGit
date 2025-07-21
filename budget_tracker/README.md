# Personal Budget Tracker 🧾

A simple command-line Python app to help you track personal expenses by category and date. Data is saved in a local JSON file.

## Features

- Add daily transactions with category and amount
- View transaction history and category-wise summaries
- JSON-based persistent storage
- Clean separation of logic with reusable utility modules

## File Structure

```
├── main.py # Entry point of the app
├── transaction.py # Transaction class definition
├── budget_utils.py # Utility functions (summary, save/load, grouping)
└── transactions.json # Auto-generated data file for storage
```

## Requirements

- Python 3.6+

## How to Run

```bash
python main.py
```

## Sample Usage

* 1. Add a Transaction

```
Input date in YYYY-MM-DD or press Enter for today's date

Enter category (e.g., Food, Transport)

Enter amount

```

* 2. View Summary
```
 Displays a list of all transactions

 Shows total spent per category
```

* 3. Exit

```
Quit the app safely
```
### Example

```
=== Personal Budget Tracker ===
1. Add transaction
2. View summary
3. Exit
Enter choice (1-3): 1
Enter date (YYYY-MM-DD) or press Enter for today: 
Enter category (e.g., Food, Transport): Food
Enter amount: 10.5
Transaction added!
```

### Data Format

Transactions are saved to transactions.json in this format:
```
[
  {
    "date": "2025-07-21",
    "category": "Food",
    "amount": 10.5
  }
]

```