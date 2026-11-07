from datetime import date

# class Book -> takes book's details and save them to a book object
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

# class Member -> takes member's details and save them to a member object
class Member(): 
    def __init__(self, name, member_id = None):
        self.name = name.strip().title()
        self.member_id = member_id
        
    def print_member(self): 
        print(f"Member ID: {self.member_id}")
        print(f"Name: {self.name}")
        
# class Library -> Takes book object and member object and add them to the books and members list
class Library:
    def __init__(self):
        self.books = []
        self.members = []
        self.book_counter = 0
        self.member_counter = 0
        self.loans = []

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
        
    def issue_book(self, book, member): 
        if member in self.members: 
            if book in self.books: 
                if book.is_available: 
                    loan = Loan(book, member)
                    self.loans.append(loan) 
                    book.is_available = False
                else: 
                    print("Book is already issued")
            else: 
                print("Book not found")
        else: 
            print("Member not found! Please register first.")
            
    def return_book(self, book): 
        for loan in self.loans: 
            if loan.book == book: 
                self.loans.remove(loan)
                book.is_available = True
        print("Book is not issued!")  

      

class Loan: 
    def __init__(self, book, member):
        self.book = book
        self.member = member
        self.issued_date = date.today()
        

        
        
        
my_library = Library()

book_1 = Book("alchemist", "paulo choelo")
book_2 = Book("the kite runner", "khalil jibran")
book_3 = Book("the brothers karamazove", "fyodor dostoevsky")
my_library.add_book(book_1)
my_library.add_book(book_2)
my_library.add_book(book_3)
member_1 = Member("faraz akbar")
member_2 = Member("Haji claude")
my_library.add_member(member_1)
my_library.add_member(member_2)
member_3 = Member("Bibity bop")
my_library.issue_book(book_1, member_1)
my_library.issue_book(book_2, member_1)
my_library.return_book(book_3)





