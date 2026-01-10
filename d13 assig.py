# library management system classses: book, library,.
# Add methods to add_book, remove_book, search_boook.
# use inheritance for different book types(eg. Ebook).

class Book:
    def __init__(self,book_name,author_name):
        self.book_name = book_name
        self.author_name = author_name
    def display(self):
        print(f"Name of Book:{self.book_name}")
        print(f"Author name:{self.author_name}")

class Ebook(Book):
    def __init__(self, book_name, author_name):
        super().__init__(book_name, author_name)
    def display(self):
        print(f"Name of Book:{self.book_name}")
        print(f"Author:{self.author_name}")

class Library:
    books =[]

    def add_book(self,book):
        self.books.append(book)
        print("Book added successfully")
    def remove_book(self,book_name):
        for book in self.books:
            if book.book_name ==book_name:
                self.books.remove(book)
                print("removed successfully")
            else:
                print("Book not found")
    def search_book(self,book_name):
        for book in self.books:
            if book_name == book_name:
                book.display()
            else:
                print("book not found")
    def display_books(self):
        if not  self.books:
            print("no books in library")
        else:
            for book in self.books:
                book.display()

library = Library()

while True:
    choice = int(input("1 for add book, 2 for add Ebook, 3 for remove book , 4 for search book, 5 for display books, 6 for exit:"))
    match choice:
        case 1:
            book_name = input("Enter book name:")
            author_name = input("Enter author name:")
            book = Book(book_name,author_name)
            library.add_book(book)
        case 2:
            book_name = input("Enter book name:")
            author_name = input("Enter author name:")
            EBook = Ebook(book_name,author_name)
            library.add_book(EBook)
        case 3:
            book_name = input("Enter book name:")
            library.remove_book(book_name)
        case 4:
            book_name = input("Enter book name:")
            library.search_book(book_name)
        case 5:
            library.display_books()
        case 6:
            print("exit")
            break
        case _:
            print("invalid choice")
            

        