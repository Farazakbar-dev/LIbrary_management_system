from datetime import date
import json
# class Book 
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

# class Member 
class Member(): 
    def __init__(self, name, member_id = None):
        self.name = name.strip().title()
        self.member_id = member_id
        
    def print_member(self): 
        print(f"Member ID: {self.member_id}")
        print(f"Name: {self.name}")
        
# class Library 
class Library:
    def __init__(self):
        self.books = []
        self.members = []
        self.book_counter = 0
        self.member_counter = 0
        self.loans = []

    def add_book(self, book):
        book.book_id = len(self.books) + 1
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
                print("Book returned!")
                return
        print("Book is not issued!")  
  
class Loan: 
    def __init__(self, book, member):
        self.book = book
        self.member = member
        self.issued_date = date.today()
             
my_library = Library()

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
    for member in my_library.members: 
        if member.member_id == usr_member_id: 
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

# define print_all_books()
def print_all_books():
    for book in my_library.books: 
        print(f"Book ID: {book.book_id} Title: {book.title} Author: {book.author} Is available: {book.is_available}")
        
# function for saving books
def write_books_file():
    l = my_library.books
    new_list = []
    for book in l: 
        my_dict = {
            "book_id": book.book_id,
            "title": book.title, 
            "author": book.author, 
            "is_available": book.is_available
        }
        new_list.append(my_dict)
        
    with open('books.json', 'w') as file: 
        json.dump(new_list, file, indent=4)
        
# unction for saving members
def write_members_file():
    l = my_library.members
    new_list = []
    for member in l: 
        my_dict = {
            "member_id": member.member_id,
            "name": member.name, 
        }
        new_list.append(my_dict)
    with open('members.json', 'w') as file: 
        json.dump(new_list, file, indent=4)
            
# function for saving loans (issued books)
def write_loans_file():
    l = my_library.loans
    new_list = []
    for loan in l: 
        my_dict = {
            "member_id": loan.member.member_id,
            "book_id": loan.book.book_id, 
        }
        new_list.append(my_dict)
    with open('loans.json', 'w') as file: 
        json.dump(new_list, file, indent=4)

# Load all books to books list
def load_books(): 
    try:
        with open('books.json', 'r') as file: 
            loaded_json = json.load(file)
            list_of_loaded_books = [{k: v for k, v in item.items()} for item in loaded_json]
            for my_dict in list_of_loaded_books: 
                book = Book(my_dict["title"], my_dict["author"], my_dict["is_available"], my_dict["book_id"])
                my_library.books.append(book)
    except FileNotFoundError: 
        print("File doesn't exist!") 
             
def load_members(): 
    try: 
        with open('members.json', 'r') as file: 
            loaded_json = json.load(file)
            list_of_loaded_members = [{k: v for k, v in item.items()} for item in loaded_json]
            for my_dict in list_of_loaded_members: 
                member = Member(my_dict["name"], my_dict["member_id"])
                my_library.members.append(member)
    except FileNotFoundError: 
        print("File doesn't exist!")
        
def load_loans(): 
    try:    
        with open('loans.json', 'r') as file: 
            loaded_json = json.load(file)
            list_of_loaded_loans = [{k: v for k, v in item.items()} for item in loaded_json]

            for my_dict in list_of_loaded_loans: 
                my_member = None
                my_book = None
                # loop through books
                for book in my_library.books: 
                    if book.book_id == my_dict["book_id"]: 
                        my_book = book
                        break
                # loop through members
                for member in my_library.members: 
                    if member.member_id == my_dict["member_id"]: 
                        my_member = member  
                        break 
                if my_book is not None and my_member is not None: 
                    loan = Loan(my_book, my_member)
                    my_library.loans.append(loan)
    except FileNotFoundError : 
        print("File doesn't exist!")
        
# menu function
def menu():
    load_books()
    load_members() 
    load_loans()
    while True:
        print("\nSelect an option from below: ")
        options = {
            1: "Add a book", 
            2: "Add a member", 
            3: "Issue a book", 
            4: "Return a book",
            5: "View all books",
            6: "Exit"
        }
        for key, value in options.items(): 
            print(f"{key}: {value}")
        
        num = int(input(f"Enter any number between 1 - {len(options)}: "))
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
        elif num == 5: 
            print_all_books()
        elif num == 6: 
            print("Exiting...")
            write_books_file()
            write_members_file()
            write_loans_file()
            break
        else: 
            print("Invalid option..")
               
menu()
        