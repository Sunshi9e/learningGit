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
