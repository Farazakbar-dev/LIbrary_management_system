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
        book.book_id = len(self.books) + 1
        with open('books.txt', 'a') as f: 
            f.write(f"Book ID: {book.book_id}, Title: {book.title}, Author: {book.author}")
        self.books.append(book)
        self.book_counter += 1
        
        
    def add_member(self, member): 
        member.member_id = len(self.members) + 1
        self.members.append(member)
        self.member_counter += 1
        
    def issue_book(self, book, member): 
        if member in self.members: 
            if book in self.books: 
                if book.is_available: 
                    loan = Loan(book, member)
                    self.loans.append(loan) 
                    book.is_available = False
                    print("Book issued!")
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
member_3 = Member("Bibity bop")
my_library.add_member(member_1)
my_library.add_member(member_2)
my_library.add_member(member_3)

# my_library.issue_book(book_1, member_1)
# my_library.issue_book(book_2, member_1)

# my_library.return_book(book_3)

# menu function
def menu(): 
    print("\nSelect an option from below: ")
    options = {
        1: "Add a book", 
        2: "Add a member", 
        3: "Issue a book", 
        4: "Return a book",
        5: "Exit"
    }
    for key, value in options.items(): 
        print(f"{key}: {value}")
    
    num = int(input("Enter any number between 1 - 5: "))
    if num == 1: 
        print("Add book selected!\n")
        my_library.add_book(add_a_book())
    elif num == 2: 
        print("Add member selected!\n")
        my_library.add_member(add_a_member())
    elif num == 3: 
        print("Issue book selected!")
        a,b = issue_a_book()
        my_library.issue_book(a,b)
    elif num == 4: 
        print("Return book selected!") 
        my_library.return_book(return_a_book())
    else: 
        print("Exiting...")
        

def add_a_book(): 
    title = input("Enter book's title: ")
    author = input("Enter book's author: ")
    book = Book(title, author)
    return book

def add_a_member(): 
    name = input("Enter member's name: ")
    member = Member(name)
    return member

# define issue_a_book()
def issue_a_book(): 
    usr_member_id = int(input("Enter your member ID: "))
    book_id = int(input("Enter the book id you want to borrow: "))
    # member object
    for member in my_library.members: 
        if member.member_id == usr_member_id: 
            # book object
            for book in my_library.books: 
                if book_id == book.book_id: 
                    return book, member
                
            return None, None
        
    return None, None
    

  # define return_a_book()  
def return_a_book(): 
    # book object
    book_id = int(input("Enter book ID that you want to return: "))
    for book in my_library.books: 
        if book.book_id == book_id: 
            return book
    return None

menu()
for loan in my_library.loans: 
    print(f"The book with book id: {loan.book.book_id} is issued to member with member id: {loan.member.member_id}")



# for book in my_library.books: 
#     print(f"Book ID: {book.book_id} Title: {book.title} Author: {book.author} Is available: {book.is_available}")
    
# for member in my_library.members: 
#     print(f"Member ID: {member.member_id} Name: {member.name} ")
    

