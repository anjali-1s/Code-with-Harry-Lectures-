class Library:
     def __init__(self):
          self.no_Books = 0
          self.books = []

     def addbooks(self,book):
          self.no_Books = len(self.books)
          self.books.append(book)

     def showInfo(self):
          print(f"The library has {self.no_Books} books and the books are :")

          for book in self.books:
               print(book)

l1 = Library()
l1.addbooks("Harry Potter1")
l1.showInfo()
l1.addbooks("Harry Potter2")
l1.showInfo()
l1.addbooks("Harry Potter3")
l1.showInfo()


