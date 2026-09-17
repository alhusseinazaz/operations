from models import Book

def find_book(books, book_id):
    for book in books:
        if book.book_id == book_id:
            return book
    return None


def add_book(books, new_book):
   
    if find_book(books, new_book.book_id) is not None:
        return "Error: A book with this ID already exists."

    books.append(new_book)
    return "The book was added."


def borrow_book(books, book_id):
    book = find_book(books, book_id)

    if book is None:
        return "Error: Book not found."

    if not book.is_available:
        return "Sorry, this book is already borrowed."

   
    book.is_available = False
    return f"Successfully borrowed '{book.title}'."


def return_book(books, book_id):
    book = find_book(books, book_id)

    if book is None:
        return "Error: Book not found."

    if book.is_available:
        return "This book was not borrowed."

 
    book.is_available = True
    return "Thank you for returning the book."


def count_available(books):
    count = 0
    for book in books:
        if book.is_available:
            count += 1
    return count


def show_all_books(books):

    if not books:
        print("There are no books in the library yet.")
    else:
     
        for book in books:
            book.show()