# class Bank:
#     rate_of_interest = 4.01
#     def __init__(self):
#         self.customer_name = None
#         self.account_number = None
#         self.initial_balance = 1000
#         self.contact_number = None
#         self.address_field = None
#
#     def createAccount(self,customer_name,account_number,initial_balance,contact_number,address_field):
#                 self.customer_name = customer_name
#                 self.account_number = account_number
#                 self.initial_balance+=initial_balance
#                 self.contact_number = contact_number
#                 self.address_field = address_field
#
#     def deposit(self,amount):
#         self.initial_balance = self.initial_balance+amount
#         print("Your Amount deposited Successfully")
#         print("Your total balance is",self.initial_balance)
#
#     def withdraw(self ,amount):
#         if self.initial_balance>=amount:
#             self.initial_balance-=amount
#             print("Amount wthdrawn successfully")
#             print("Your total balance is",self.initial_balance)
#         else:
#             print("No sufficient Balance")
#
#
#     def compute_Interest(self,year):
#         return self.initial_balance*Bank.rate_of_interest*year/100
#
#
#
#
#
#
#
# name = input("Enter your name: ")
# contact = input("Enter contact no: ")
# address = input("Enter address: ")
# initialBal = int(input("Enter your balance: "))
# b = Bank()
# b.createAccount(name, contact, address, initialBal)
# while option != 5:
#     print("1. Deposit money.")
#     print("2. Withdraw money.")
#     print("3. Compute interest.")
#     print("5. EXIT.")
#
#     option = int(input("Enter your option"))
#     if option == 1:
#         deposit_amount = int(input("Enter amount to be deposited"))
#         b.deposit(deposit_amount)
#         print(b.initial_balance)
#     elif option==2:
#         withdrawn_amount = int(input("Enter amount to be withdrawn"))
#         b.withdraw(withdrawn_amount)
#         print(b.initial_balance)
#     elif option==3:
#         print("Enter year")
#         year = int(input())
#         x = b.compute_Interest(year)
#         print("Your interest rate is",x)
#



# kwargs
# Classes objects
# decorator
# instance staticmethod static variables
#




class Calculator:

    def add(self, a, b):
        return a + b



function_name = 'add'
dummy = 0
print(Calculator._dict_["add"](dummy, 3, 1))
