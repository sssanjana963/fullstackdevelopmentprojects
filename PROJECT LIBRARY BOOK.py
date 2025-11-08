import os
import ast

class Library:
    def __init__(self, filename='library_data.txt'):
        self.filename = filename
        # Load the library data from file (if it exists)
        self.library_data = self.load_data()

    def load_data(self):
        # Load the book data from the text file as a dictionary
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                content = file.read()
                if content:
                    return ast.literal_eval(content)  # Safely convert string to dictionary
        return {}

    def save_data(self):
        # Save the dictionary back to the text file
        with open(self.filename, 'w') as file:
            file.write(str(self.library_data))

    def add_book(self, book_id, title, author, year, isbn):
        if book_id in self.library_data:
            print("Book ID already exists.")
        else:
            self.library_data[book_id] = {
                "Title": title,
                "Author": author,
                "Year": year,
                "ISBN": isbn
            }
            self.save_data()
            print("Book added successfully.")

    def change_book_details(self, book_id, title=None, author=None, year=None, isbn=None):
        if book_id in self.library_data:
            if title:
                self.library_data[book_id]["Title"] = title
            if author:
                self.library_data[book_id]["Author"] = author
            if year:
                self.library_data[book_id]["Year"] = year
            if isbn:
                self.library_data[book_id]["ISBN"] = isbn
            self.save_data()
            print("Book details updated successfully.")
        else:
            print("Book not found.")

    def delete_book(self, book_id):
        if book_id in self.library_data:
            del self.library_data[book_id]
            self.save_data()
            print("Book deleted successfully.")
        else:
            print("Book not found.")

    def display_all_books(self):
        if not self.library_data:
            print("No books available.")
            return
        for book_id, details in self.library_data.items():
            print(f"ID: {book_id} | Title: {details['Title']} | Author: {details['Author']} | Year: {details['Year']} | ISBN: {details['ISBN']}")

    def display_specific_book(self, book_id):
        if book_id in self.library_data:
            details = self.library_data[book_id]
            print(f"ID: {book_id} | Title: {details['Title']} | Author: {details['Author']} | Year: {details['Year']} | ISBN: {details['ISBN']}")
        else:
            print("Book not found.")

def main():
    library = Library()

    while True:
        print("\nLibrary Menu:")
        print("1. Add a Book")
        print("2. Change Book Details")
        print("3. Delete a Book")
        print("4. Display All Books")
        print("5. Display a Specific Book")
        print("6. Exit")

        choice = input("Choose an option (1-6): ")

        if choice == '1':
            book_id = input("Enter book ID: ")
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            year = input("Enter publication year: ")
            isbn = input("Enter ISBN: ")
            library.add_book(book_id, title, author, year, isbn)

        elif choice == '2':
            book_id = input("Enter book ID to change: ")
            title = input("Enter new title (leave empty to skip): ")
            author = input("Enter new author (leave empty to skip): ")
            year = input("Enter new publication year (leave empty to skip): ")
            isbn = input("Enter new ISBN (leave empty to skip): ")
            library.change_book_details(book_id, title or None, author or None, year or None, isbn or None)

        elif choice == '3':
            book_id = input("Enter book ID to delete: ")
            library.delete_book(book_id)

        elif choice == '4':
            library.display_all_books()

        elif choice == '5':
            book_id = input("Enter book ID to display: ")
            library.display_specific_book(book_id)

        elif choice == '6':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()