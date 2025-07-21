# main.py

from inventory import load_inventory, add_book, view_books
from book import Book

def main():
    inventory = load_inventory()

    while True:
        print("\n--- Bookstore Inventory ---")
        print("1. Add Book")
        print("2. View Books")
        print("3. Exit")
        choice = input("Choose an option (1-3): ")

        if choice == "1":
            title = input("Enter book title: ")
            author = input("Enter author: ")
            price = input("Enter price: ")
            stock = input("Enter stock quantity: ")
            book = Book(title, author, price, stock)
            add_book(book, inventory)
            print("Book added!")

        elif choice == "2":
            view_books(inventory)

        elif choice == "3":
            search_book(inventory)
            break

        elif choice == "3":
            print("Goodbye!")


        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
