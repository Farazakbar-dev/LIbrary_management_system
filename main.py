
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


class Member(): 
    def __init__(self, name, member_id = None):
        self.name = name.strip().title()
        self.member_id = member_id
        
    def print_member(self): 
        print(f"Member ID: {self.member_id}")
        print(f"Name: {self.name}")
        
        
class Library:
    def __init__(self):
        self.books = []
        self.members = []
        self.book_counter = 0
        self.member_counter = 0

    def add_book(self, book):
        book.book_id = self.book_counter + 1
        with open('books.txt', 'a') as f: 
            f.write(f"Book ID: {book.book_id}, Title: {book.title}, Author: {book.author}")
        self.books.append(book)
        self.book_counter += 1
        

        
    def add_member(self, member): 
        member.member_id = self.member_counter + 1
        self.members.append(member)
        self.member_counter += 1
        




my_library = Library()

book_1 = Book("alchemist", "paulo choelo")
book_2 = Book("the kite runner", "khalil jibran")
my_library.add_book(book_1)
my_library.add_book(book_2)

member_1 = Member("faraz akbar")
member_2 = Member("Haji claude")
my_library.add_member(member_1)
my_library.add_member(member_2)
# print(my_library.books)
# print(book_1.book_id)
# print(book_2.book_id)

# book_1.print_book()
# book_2.print_book()

# member_1.print_member()
# member_2.print_member()


with open('books.txt', 'r') as f: 
    print(f.read())