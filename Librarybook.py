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





        


