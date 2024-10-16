import code



# Exercise 1 and 2

class InvalidBookError(Exception):
    def __init__(self, title, author, pages):
        message = f"Invalid book: title='{title}', author='{author}', pages={pages}"
        self.message = message

class BookNotFoundError(Exception):
    def __init__(self, title):
        message = f"Book '{title}' not found in the library"
        self.message = message

class Book():
    def __init__(self, title, author, pages):
        if not isinstance(title, str) or not title.strip():
            raise InvalidBookError(title, author, pages)
        if not isinstance(author, str) or not author.strip():
            raise InvalidBookError(title, author, pages)
        if not isinstance(pages, int) or pages <= 0:
            raise InvalidBookError(title, author, pages)
        self.title = title
        self.author = author
        self.pages = pages

    def get_title(self):
        return self.title

    def get_author(self):
        return self.author

    def get_pages(self):
        return self.pages

class Library():
    def __init__(self):
        self.books = []

    def add_books(self, book):
        self.books.append(book)

    def remove_book(self, title):
        for book in self.books:
            if book.get_title() == title:
                self.books.remove(book)
                return
        raise BookNotFoundError(title)

    def list_books(self):
        for book in self.books:
            print(book.get_title())

    def total_pages(self):
        total = 0
        for book in self.books:
            total += book.get_pages()
        return total
    

# Exercise 3
def sum_digits(n):
    if n == 0:  
        return 0
    else:
        last_digit = n % 10
        remaining_digits = n // 10
        return last_digit + sum_digits(remaining_digits)
    

code.interact(local=dict(globals(), **locals()))