class Employee:
    def __init__ (self,name, salary):
        self.name = name
        self.salary = salary

    def gibe_raise(self,amount):
        if amount <= 0:
            print("Invalid raise amount: must be positive.")
            return
        self.__salary +=amount
        print (f"Rasie applied. New salary : ${ self .__salary}")

    def view_payslip(self):
        print (f"Payslip - {self.name}: $ {self.__salary}")