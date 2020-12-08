import datetime
import pytz
from _datetime import date


class Account():
    '''simple account class with balance'''
    
    #staticmethods are called using class name call made on lines 29 and 34
    @staticmethod
    def _current_time():
        utc_time = datetime.datetime.utcnow()
        return pytz.utc.localize(utc_time)
    
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.transaction_list = [(Account._current_time(), balance)]
        print(f"Account created for {self.name}")
        
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            #call to method from within a method using self!!!!
            self.show_balance()
            #appending transactions to transaction_list
            #self.transaction_list.append((pytz.utc.localize(datetime.datetime.utcnow()), amount))
            #we can use static method to append datetime to transaction_list like below line 28
            self.transaction_list.append((Account._current_time(), amount))
            
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.transaction_list.append((Account._current_time(), -amount))#note - amount here!
        else:
            print("Amount must be greater than 0 and must not exceed your balance")
            #call to method from within a method using self!!!!
        self.show_balance()
            
    def show_balance(self):
        print(f"Your balance is {self.balance}")
        
    def show_transactions(self):
        for date, amount in self.transaction_list:
            if amount > 0:
                tran_type = "deposited"
            else:
                tran_type = "withdrawn"
                amount *= -1 #to show negative number
            print(f"{amount:6} {tran_type} on {date} local time was {date.astimezone()}")
        
        
if __name__ == '__main__':
    Adam = Account('Adam', 0)
    print(f'{Adam.balance}')
    
    Adam.deposit(100)
    Adam.show_balance()
    
    Adam.withdraw(50)
    Adam.show_balance()
    
    Adam.withdraw(500)
    Adam.show_transactions()
    
    print("-" * 30)
    
    Emma = Account("Emma", 800)
    Emma.deposit(100)
    Emma.withdraw(200)
    Emma.show_transactions()
    
    
    
    
    
    
    