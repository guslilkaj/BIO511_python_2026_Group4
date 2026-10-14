#creates a class 
class Book:
    def __init__(self, title, author, year):
        self.title = title  #attaches attribute to object
        self.author = author
        self.year = year 

book1 = Book("Python for dummies, absolute morons. Idiots", "A. Lindberg", "2026")