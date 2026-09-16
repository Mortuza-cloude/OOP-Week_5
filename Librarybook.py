class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def borrow (self):
        if self.is_borrowed:
            print(f" {self.title} is already borrwed")
            return
        self.is_borrwed = True
        print (f" {self.title} borrwed successfully")

    def return_book(self):
        if not self.is_borrowed:
            print(f"{self.title} was not borrwed")
            self.is_borrwed =False
            print(f'" {self.title}" returned successflly.')

class Library:
    def __init__(self):
        self.books =[]
    def add_books(self, book):
        self.books.append(book)

    def find_book(self,title):
        for b in self.books:
            if b.title ==title:
                return b
            return None
    def main():
        library = Library()
        count = int (input("How many books do you want to add"))
        for _ in range (count):
            title =input ("Book title: ")
            author = input ("Author:")
            library .add_book(Book(title,author))

            
            





        


