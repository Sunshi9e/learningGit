import os
import json
from book import Book
from math import ceil

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATABASE = os.path.join(BASE_DIR, "books.json")

def load_inventory():
    if not os.path.exists(DATABASE):
        return []

    try:
        with open(DATABASE, "r") as f:
            data = json.load(f)
            return [Book(**book) for book in data]
    except (json.JSONDecodeError, FileNotFoundError):
        print("Error loading inventory.")
        return []

def save_inventory(inventory):
    try:
        with open(DATABASE, "w") as f:
            json.dump([b.to_dict() for b in inventory], f, indent=2)
    except IOError:
        print("Error saving inventory.")

def add_book(book, inventory):
    inventory.append(book)
    save_inventory(inventory)

def view_books(inventory):
    if not inventory:
        print("No books in inventory.")
    for book in inventory:
        print(f"Title : {book.title}")
        print(f"Author: {book.author}")
        print(f"Price : ${book.price}")
        print(f"Stock : {book.stock}")
        print("-" * 20)
def search_book(inventory):
    title = input("Enter title to search: ").lower()
    found = False
    for b in inventory:
        if title in b.title.lower():
            print("-------------------------")
            print(f"Title : {b.title}")
            print(f"Author: {b.author}")
            print(f"Price : ${b.price:.2f}")
            print(f"Stock : {b.stock}")
            found = True
    if not found:
        print("No matching book found.")

def update_stock(inventory):
    title = input("Enter title to update stock: ").lower()
    for b in inventory:
        if title in b.title.lower():
            try:
                qty = int(input("Enter new stock quantity: "))
                if qty < 0:
                    print("Stock cannot be negative.")
                    return
                b.stock = qty
                print(f"Stock updated for '{b.title}'")
                return
            except ValueError:
                print("Invalid quantity.")
                return
    print("Book not found.")