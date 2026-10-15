class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        self.available = False
        self.borrower = None
    
    def __str__(self):
        # The __str__ dunder method will be called when using print(book_obj)
        return f"The book is titled {self.title}, written by {self.author} in {self.year}."


class Library:
    def __init__(self):
        self.books = []

    def __str__(self):
        return("library")

    def add_book(self, book_obj):
        self.books.append(book_obj)
        book_obj.available = True


class Member:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, library_class, book_obj):
        bookentry = book_obj
        the_library = library_class
        if bookentry.available is True:
            
            print(f"{self.name} borrows '{bookentry.title}' from the {the_library}")
            the_library.books.remove(bookentry)
            self.borrowed_books.append(bookentry)
            bookentry.available = False
            bookentry.borrower = self
        else:
            print(f"{self.name} tries to borrow {bookentry.title} from the {the_library}, but it's not in.")

    def return_book(self, library_class, book_obj):
        the_library = library_class
        bookentry = book_obj
        if bookentry in self.borrowed_books:
            the_library.books.append(bookentry)
            self.borrowed_books.remove(bookentry)
            bookentry.available = True
            print(f"{self.name} returned ", bookentry.title, " to the", the_library)

# Example usage
book1 = Book("1984", "George Orwell", 1949)
book2 = Book("To Kill a Mockingbird", "Harper Lee", 1960)
library = Library()
library.add_book(book1)  # Should add book1 to the library and make it available for borrowing
print(book1.available)
member1 = Member("Alice")
member1.borrow_book(library, book1)  # Now the book should be borrowed by Alice
print("Available books:", [str(book) for book in library.books])