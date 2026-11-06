
class Book:
    def __init__(self, title, author, is_available=True, book_id = None):
        self.title = title.strip().title()
        self.author = author.strip().title()
        self.is_available = is_available
        self.book_id = book_id
    def print_book(self):
        print(f"Book ID: {self.book_id}")
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Availability: {self.is_available}")


class Library:
    def __init__(self):
        self.books = []
        self.members = []
        self.counter = 0

    def add_book(self, book):
        book.book_id = self.counter + 1
        self.books.append(book)
        self.counter += 1




my_library = Library()

book_1 = Book("alchemist", "paulo choelo")
book_2 = Book("the kite runner", "khalil jibran")
my_library.add_book(book_1)
my_library.add_book(book_2)

# print(my_library.books)
print(book_1.book_id)
print(book_2.book_id)
book_1.print_book()