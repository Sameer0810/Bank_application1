class Bank:
    bankname = 'icici'
    
    def __init__(self, name, bal=0):
        self.name = name
        self.bal = bal

    def deposit(self, amt):
        self.bal += amt
        print(f'The initial balance is 0Rs/- and after depositing {amt}Rs/- the current balance is {self.bal}Rs/-')

    def withdraw(self, amt):
        if amt > self.bal:
            print('Insufficient Balance')
        else:
            self.bal -= amt
            print(f'{amt}Rs/- has been withdrawn. Current balance: {self.bal}Rs/-')

    def check_balance(self):
        print(f'Current balance is {self.bal}Rs/-')

    @classmethod
    def change_bank_name(cls, newname):
        cls.bankname = newname
        print(f'The new bank name is {cls.bankname}')

    @staticmethod
    def bank_policy():
        print('Minimum balance should be 1000Rs/-')

print('Welcome to Most Trusted Bank ')
n = input('Enter Your Sweet Name: ')
b = int(input('Enter the Initial balance: '))
s1 = Bank(n, b)

while True:
    print('\n1.Deposit \n2.Withdraw \n3.Check balance \n4.Bank Policy \n5.Change Bank name \n6.Exit')
    choice = int(input('Enter Your choice: '))
    
    match choice:
        case 1:
            a = int(input('Enter the amount to deposit: '))
            s1.deposit(a)
        case 2:
            a = int(input('Enter the amount to withdraw: '))
            s1.withdraw(a)
        case 3:
            s1.check_balance()
        case 4:
            s1.bank_policy()
        case 5:
            new = input('Enter the new bank name: ')
            Bank.change_bank_name(new)
        case 6:
            print('Thank You, visit again!')
            break
        case _:
            print('Invalid Choice')

