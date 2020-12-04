class Account():
    '''simple account class with balance'''
    
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        print(f"Account created for {self.name}")
        
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
        else:
            print("Amount must be greater than 0 and must not exceed your balance")
            self.show_balance()
            
    def show_balance(self):
        print(f"Your balance is {self.balance}")
        
if __name__ == '__main__':
    Adam = Account('Adam', 0)
    print(f'{Adam.balance}')
    
    Adam.deposit(100)
    Adam.show_balance()
    
    Adam.withdraw(50)
    Adam.show_balance()
    
    Adam.withdraw(500)