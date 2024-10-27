#Define a Book class
class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}"

#Define a Library class to manage books
class Library:
    def __init__(self):
        self.books = []
        self.load_books_from_file()  # Load books when the library is created

    def add_book(self, book):
        self.books.append(book)
        print(f"Book '{book.title}' by {book.author} added to the library.")
        self.save_books_to_file()

    def remove_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                self.books.remove(book)
                print(f"Book '{title}' removed from the library.")
                self.save_books_to_file()
                return
        print(f"Book '{title}' not found in the library.")

    def search_by_title(self, title):
        results = [book for book in self.books if title.lower() in book.title.lower()]
        if results:
            print("Books found:")
            for book in results:
                print(book)
        else:
            print(f"No books found with title containing '{title}'.")

    def search_by_author(self, author):
        results = [book for book in self.books if author.lower() in book.author.lower()]
        if results:
            print("Books found:")
            for book in results:
                print(book)
        else:
            print(f"No books found by author '{author}'.")

    def save_books_to_file(self):
        with open("library_books.txt", "w") as file:
            for book in self.books:
                file.write(f"{book.title},{book.author},{book.isbn}\n")

    def load_books_from_file(self):
        try:
            with open("library_books.txt", "r") as file:
                for line in file:
                    title, author, isbn = line.strip().split(",")
                    self.books.append(Book(title, author, isbn))
        except FileNotFoundError:
            print("No previous book records found. Starting with an empty library.")

#Demonstrate the Library Management System
if __name__ == "__main__":
    # Create an instance of the Library class
    library = Library()

    # Add books to the library
    book1 = Book("Atomic Habits", "James Clear", "1234567890")
    library.add_book(book1)

    book2 = Book("The 48 Laws of Power", "Robert Greene", "2345678901")
    library.add_book(book2)

    # Search for a book by title
    library.search_by_title("Atomic Habits")

    # Search for a book by author
    library.search_by_author("James Clear")

    # Remove a book by title
    library.remove_book("The 48 Laws of Power")

    # Try to remove a non-existing book
    library.remove_book("Non-Existing Book")
