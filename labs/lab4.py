# import code 

class book(object):
    def __init__(self, i,t,a,c):
        self.id = i
        self.title = t
        self.author = a
        self.checkout = c
    def  __str__(self):
        return f"{self.title} by  {self.author}, checkedout : {self.checkout}"
    def __repr__(self):
        return f"book('{self.id}','{self.title}','{self.author}','{self.checkout}'"

book1  = book(1,"Python Programming","John Doe",False)
book2  = book(2,"Data Science","Jane Doe",True)


class library (object):
    def __init__(self,n):
        self.name = n
        self.books = []
    
    def  add_book(self,book):
        self.books.append(book)
    
    def checkOutBook(self):
        for b in self.books:
            if b.id == book.id:
                book.checkout = True

    def  checkInBook(self):
        for b in self.books:
            if b.id == book.id:
                book.checkout = False



lib = library ("Depaul University")
lib.add_book(book1)
lib.add_book(book2)
for b in  lib.books:
    print(b)



# code.interact(local=dict(globals(), **locals()))