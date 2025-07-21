# 📚 Bookstore Inventory Manager

A simple Python CLI application to manage a bookstore inventory using JSON for persistent data storage. Add, view, search, and update book records effortlessly.

## 🧰 Tech Stack

- **Language**: Python 3.x
- **Storage**: JSON file
- **Modules Used**:
  - `os`
  - `json`
  - `math` (ceil)
  - Custom `Book` class

---

### Requirements
* Python 3.x

* No external libraries needed

## 📌 Notes

The JSON file (books.json) is auto-created in the project directory if not found.


## 📂 Project Structure

```
bookstore/
│
├── book.py
├── inventory.py
├── main.py 
├── books.json 
└── README.md
``` 



###  Features

- ➕ Add new books to the inventory
- 📖 View all books with full details
- 🔍 Search for books by title (case-insensitive)
- 🔁 Update the stock quantity of existing books
- 💾 Persistent storage using a JSON file
- 📉 Input validation for price and stock

---

###  Getting Started

### 1. Clone the Repo

```bash
git clone https://github.com/Sunshi9e/learningGit.git
cd bookstore-inventory
```

### 2. Run the App

```
python main.py

```

---

### 🛠 Usage Guide

You'll see a menu like:
```
--- Bookstore Inventory ---
1. Add Book
2. View Books
3. Search Book
4. Update Stock
5. Exit
```

### 1. Add Book

You’ll be prompted to enter:

```
Book Title

Author Name

Price (float)

Stock Quantity (integer)
```

Example:
```
Enter book title: Clean Code
Enter author: Robert C. Martin
Enter price: 45.99
Enter stock quantity: 10
```
### 2. View Books
Displays all books in the current inventory with their title, author, price, and stock.

### 3. Search Book

Enter part or full title (case-insensitive).

Example:
```
Enter title to search: clean
```
### 4. Update Stock

Update stock quantity for a book. Negative values are not accepted.

### 5. Exit

Saves the current inventory state to books.json and exits the app.

Example books.json
```
[
  {
    "title": "Atomic Habits",
    "author": "James Clear",
    "price": 23.50,
    "stock": 12
  },
  {
    "title": "The Pragmatic Programmer",
    "author": "Andy Hunt",
    "price": 42.00,
    "stock": 8
  }
]
```
---

### shut Down & Cleanup

To safely exit and persist your data:
```
Choose option 5 from the CLI menu
```
### To delete all saved data:
```
rm books.json

```




