from inventory import load_inventory, add_book, view_books, search_book, update_stock, save_inventory
from book import Book

def main():
    inventory = load_inventory()

    while True:
        print("\n--- Bookstore Inventory ---")
        print("1. Add Book")
        print("2. View Books")
        print("3. Search Book")
        print("4. Update Stock")
        print("5. Exit")
        choice = input("Choose an option (1-5): ")

        if choice == "1":
            title = input("Enter book title: ")
            author = input("Enter author: ")
            try:
                price = float(input("Enter price: "))
                stock = int(input("Enter stock quantity: "))
                book = Book(title, author, price, stock)
                add_book(book, inventory)
                print("Book added!")
            except ValueError:
                print("Invalid price or stock quantity. Please enter numbers.")

        elif choice == "2":
            view_books(inventory)

        elif choice == "3":
            search_book(inventory)

        elif choice == "4":
            update_stock(inventory)

        elif choice == "5":
            print("Goodbye!")
            save_inventory(inventory)
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
