class Book:
    def __init__(self, title, author, is_checked_out):
        self.title = title
        self.author = author
        self._is_checked_out = False

    def title(self):
        title = self.title
    def author(self):
        author = self.author

    def _is_check_out(self):
        self._is_checked_out = True
        

    # def check_in(self):
    #     self._is_checked_out = False

class Library:
    def __init__(self):
        self._books=[]
    def add_book(self, book):
        self._books.append(book)
    
    def check_out_book(self, title):
        for book in self._books:
            if book.title == title:
                book.check_out_book()
            
    def list_available_books(self):
        for book in self._books:
            if book._is_checked_out == False:
                print(f"{book.title} by {book.author}")

    def return_book(self, title):
        for book in self._books:
            if book.title == title:
                book.return_book()
