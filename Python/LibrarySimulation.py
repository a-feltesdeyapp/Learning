# Libraries
import numpy as np

def list_book_availability():
    # List of books and availability
    file = open("List of Books Short.txt","r")   # "r" has to be in quotes to work
    list_books = file.readlines()
    book_availability = []

    for book in list_books:
        # Randomize book availability
        available = np.random.randint(0,2)
        # Save book and availability in list
        book_availability = book_availability + [[book.strip(), available]]
        # Convert availability into string format
        if available == 0:
            available = "Not Available"
        else:
            available = "Available"  
    return book_availability    # end function, export value

def print_books(book_availability):
    index = 1
    # Print list of books
    for item in book_availability:
        book, available = item
        print(f"{index}. {book.strip()}: {available}")
        index += 1    

# def borrow_book(book_number, book_availability):
#     # Does book exist?
#     while not book_number.isdigit() or not (1<= int(book_number) <= len(book_availability)) or not book_number == "r":
#         # Did user exit program?
#         if book_number == "r":
#             return  
#         book_number = input("Value not recognized. Please enter number of book you wish to borrow or press r to leave: ")
#     # Is book available
#     while book_availability[int(book_number)-1][1] == 0: 
#         book_number = input("Book is not available. Please choose a new book: ")
#     # Checkout book
#     print(f"{book_availability[int(book_number)-1][0]} has been checked out.")
#     book_availability[int(book_number)-1][1] = 0
#     return book_availability
    
# List books and availability
book_availability = list_book_availability()

# Ask user for name and age.
name = input("Enter your name: ")
age = input("Enter your age: ")
while not age.isdigit() or not (0 < int(age) and int(age) < 99):
    age = input("Age not recognized. Enter your age: ")
checkout = 2
book_number = ""

# Verify user is age 12+
if int(age) >= 12:
    while checkout > 0 and book_number != "r":
        print(f"\nWelcome {name}. You may borrow up to {checkout} books.")
        book_number = input("Enter the number of the book you wish to borrow or press r to leave: ")
        book_availability = borrow_book(book_number, book_availability)
        checkout -= 1
    print(f"Now leaving. Goodbye {name}.")
else:
    print(f"\n{name} is unable to checkout books. Now leaving. Goodbye {name}.")
