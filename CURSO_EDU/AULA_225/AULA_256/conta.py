from abc import ABC, abstractmethod

class Account(ABC):
    
    def __init__(self,ag_num, ac_num, balance: float) -> None:
        super().__init__()
        self._ag_num = ag_num
        self._ac_num = ac_num
        self._balance = balance
    
    def deposit(self, amount):
        self._balance += amount
        print(f'Depositado R${amount}')
        print(f'Seu saldo agora é de R${self._balance}')
        print()
        
    @abstractmethod
    def withdraw(self, amount):
        ...
    
    @property    
    def balance(self):
        print(f'Seu saldo é de R${self._balance}.')
        print()
        
    @property
    def ac_number(self):
        return(self._ac_num)
        

class ContaPoupanca(Account):
    def withdraw(self, amount):
        if self._balance - amount <= 0:
            print('Saldo insuficiente.')
            print()
        else:
            self._balance -= amount
            print(f'Sacado R${amount}')
            print(f'Seu saldo é de R${self._balance}.')
            print()
            

class ContaCorrente(Account):
    def withdraw(self, amount):
        self._balance -= amount
        print(f'Sacado R${amount}')
        print(f'Seu saldo é de R${self._balance}.')
        print()
        
