
# Library Management System ---------------------------------------------------

class Library:
    def __init__(self):
        self.noofbooks=0
        self.books=[]
    
    def addbook(self, book):
        self.books.append(book)
        self.noofbooks= len(self.books)
    
    def showinfo(self):
        print(f"The library has {self.noofbooks} books")
        print("the names of books in the Library are:")
        for book in self.books:
            print(book)

b1= Library()
b1.addbook("Harry potter")
b1.addbook("Spiderman")
b1.addbook("Superman")
b1.addbook("The Avengers")
b1.showinfo()