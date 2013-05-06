#bankaccount.py

class Account():
    """ Bank account super class """
	
    def __init__(self, account_no, balance):
        """ constructor method """
        #something to store and process
        self.__account_no = account_no
        self.__balance = balance
        
        #stuff that starts with _underscore is private
    def get_account_no(self):
        """accessor method to retrieve account number """
        return self.__account_no

    def get_account_balance(self):
        """accessor method to retrieve account number """
        return self.__balance

##    def set_balance(self, new_balance):
##        """ modifier/mutator method to update balance """
##        self.__balance = new_balance

    def deposit(self, amount):
        self.__balance += amount

    def withdrawal(self,amount):
        self.__balance -= amount
        
    def display(self):
        """ helper/supprt method to show account info """
        print("Account No:", self.__account_no)
        print("Balance:", self.__balance)

class SavingsAccount(Account):
    """Savings account subclass """
    def __init__(self, account_no, balance, interest):
        """subclass constructor method"""
        super().__init__(account_no, balance)
        self.__interest = interest

    def calc_interest(self):
        """helper/support method to show savings account info"""
        self.deposit

class CurrentAccount(Account):
    def __init__(self, account_no, balance, overdraft):
        """subclass constructor method"""
        super().__init__(account_no, balance)
        self.__overdraft = overdraft

    def withdraw(self, amount): #overrides superclass withdrawn
        """helper/support method """
#main
acct1 = Account("C01", 0)
##print(acct1.get_account_no())
##print(acct1.get_account_balance())
acct1.deposit(500)
acct1.display()
