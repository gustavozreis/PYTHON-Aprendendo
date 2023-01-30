from pessoa import Client
from conta import ContaPoupanca
from bank import Bank

itau = Bank('Itau')

my_ac = ContaPoupanca(123, 234, 10000)
itau.add_account(my_ac._ac_num)


gustavo = Client('Gustavo', 15, my_ac)
itau.add_client(gustavo)

